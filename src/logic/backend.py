import asyncio
from datetime import datetime
from typing import List, Iterator, Dict, Any, Optional, Iterable

import numpy as np

from common.constants import C
from common.tools import tiktoken_len
from model.fragment import Fragment
from model.hit import Hit
from storage import projects
from storage.database import Database
from storage.fragments import Fragment as DbFragment, search_in_project
from storage.projects import Project
from storage.pubsub import PubSub, ChannelName
from storage.scheduler import Scheduler, Task, Operation, TaskState


class BackendError(Exception):
    pass


TInfo = Dict[str, Any]


def fragment_from_db_fragment(path: str, dbf: DbFragment) -> Fragment:
    return Fragment(
        uuid=str(dbf.id),
        path=path,
        lineno=dbf.lineno,
        depth=dbf.depth,
        type=dbf.category,
        name=dbf.name,
        text=dbf.body,
        tokens=dbf.tokens,
    )


def combine_fragments(fragments: Iterable[Fragment], max_tokens: Optional[int] = None) -> Iterator[Fragment]:
    combined: Optional[Fragment] = None
    combined_texts = []
    for fragment in fragments:
        if combined is None:
            combined = fragment
            combined_texts.append(fragment.text)
            continue

        if (fragment.path == combined.path and
                fragment.type == combined.type and
                fragment.name == combined.name and
                combined.lineno <= fragment.lineno and
                combined.tokens + fragment.tokens <= max_tokens):
            combined_texts.append(fragment.text)
            combined.tokens += fragment.tokens
            continue

        combined.text = ''.join(combined_texts)
        yield combined

        combined = fragment
        combined_texts.clear()
        combined_texts.append(fragment.text)

    if combined is not None:
        combined.text = ''.join(combined_texts)
        yield combined


class Backend:
    def __init__(self, db: Database, project: Project) -> None:
        self.db = db
        self.project = project
        self.pubsub = PubSub(self.db)
        self.scheduler = Scheduler(self.db)

    @classmethod
    async def ensure_project(cls, db: Database, uid: str, project_name: str) -> Optional["Backend"]:
        async with db.transaction() as conn:
            project = await projects.find_by_uid_and_name(conn, uid, project_name)
            if project is None:
                project = await projects.create(conn, uid, project_name)
        return Backend(db, project)

    async def download(self, url: Optional[str], *, timeout: float = 30.0 if C.PRODUCTION else 999999.0) -> TInfo:
        task: Task = Task(
            operation=Operation.DownloadArchive,
            params=dict(url=url, project_id=self.project.id)
        )

        async with self.pubsub.listen(ChannelName.DownloadCompleted.name):
            await self.scheduler.schedule(task)
            try:
                await self.pubsub.receive_with_timeout(timeout, predicate=lambda event: event.params.get('url') == url)
            except asyncio.TimeoutError:
                pass

        task = await self.scheduler.wait_task_leave_state(task.id, TaskState.pending)

        if task.state == TaskState.failed:
            return dict(
                status=f'Failed to download archive: {task.message}',
                hint='Try the download URL in a private browser. Does it work? Try to strip down the archive to be smaller and contain less files.',
                support='https://askyourcode.ai',
            )

        if task.state == TaskState.crashed:
            return dict(
                status='Internal error while downloading archive.',
                hint='Please try again later. The backend is monitored and we will fix this.',
                support='https://askyourcode.ai',
            )

        if task.state == TaskState.pending:
            return dict(
                status='The download is still in progress.',
                hint='Try to request a project summary later.',
                support='https://askyourcode.ai',
            )

        assert task.state == TaskState.completed
        return dict(status='Archive downloaded')

    async def search(self, *, path: str = '', tail: str = '', name: str = '', text: str = '', limit: int = 1) -> List[Hit]:
        await self.update_project_accessed()

        async with self.db.connection() as conn:
            triplets = await search_in_project(conn, self.project.id, path, tail, name, text, False, limit)

        if not triplets:
            return []

        fragments = list(combine_fragments((fragment_from_db_fragment(*pair) for pair in triplets), max_tokens=C.MAX_TOKENS_PER_SEARCH_RESULT))

        hit_tokens = np.array([fragment.tokens for fragment in fragments])
        cum_tokens = np.cumsum(hit_tokens)
        keep = np.sum(cum_tokens <= C.MAX_TOKENS_PER_SEARCH_RESPONSE)
        assert keep

        fragments = fragments[:keep]

        count = len(fragments)
        return [Hit.from_fragment(1.0 - i / count, fragment)
                for i, fragment in enumerate(fragments)]

    async def summarize(self, *, path: str = '', tail: str = '', name: str = '', token_limit: int = 0) -> str:
        await self.update_project_accessed()

        async with self.db.connection() as conn:
            pairs = await search_in_project(conn, self.project.id, path, tail, name, '', True, 10_000)

        fragments: List[Fragment] = [fragment_from_db_fragment(*pair) for pair in pairs]

        if fragments:
            summary = ''.join(self.merge_summaries(path, fragments))
        else:
            if tail or name:
                return ''
            async with self.db.connection() as conn:
                pairs = await search_in_project(conn, self.project.id, '/', '', '', '', True, 10_000)
                fragments = [fragment_from_db_fragment(*pair) for pair in pairs]
            if not fragments:
                return ''
            return 'No file matched the query. Explore the project by summarizing path=/\n'

        summary = summary.split('\n')

        summary.insert(0, '')

        extensions = ' '.join(sorted(set('.' + fragment.path.rsplit('.', 1)[-1] for fragment in fragments if fragment.path and '.' in fragment.path.replace('/.', '/'))))
        if extensions:
            if len(extensions) > 1:
                summary.insert(0, f'File extensions: {extensions}')
            else:
                summary.insert(0, f'File extension: {extensions}')

        if tail:
            summary.insert(0, f"Summary of file(s): {path}*{tail}")
        else:
            summary.insert(0, f"Summary of path: {path or '/'}")

        if not token_limit:
            token_limit = 2000

        summary = np.array(summary, dtype=object)
        line_lengths = np.array([tiktoken_len(line) for line in summary], dtype=np.int32)
        keep_lines = np.array([bool(line) and not line.startswith(' ') for line in summary], dtype=np.bool_)

        while summary.size and np.sum(line_lengths) > token_limit:

            max_length = np.max(line_lengths)
            if max_length < 1:
                break

            keep = np.logical_or(keep_lines, line_lengths < max_length)
            if np.all(keep == 1):
                break

            summary = summary[keep]
            line_lengths = line_lengths[keep]
            keep_lines = keep_lines[keep]

        total = np.sum(line_lengths)
        if total > token_limit:
            summary = summary[:summary.size * token_limit // total]

        return '\n'.join(summary)

    def merge_summaries(self, path_query: str, fragments: List[Fragment]) -> Iterator[str]:
        if not fragments:
            return

        min_slash_count = path_query.rstrip('/').count('/')

        subdir_hit_counts = {}
        file_summaries = []
        for fragment in fragments:
            extra_slashes = fragment.path.count('/') - min_slash_count
            if extra_slashes > 1:
                subdir_name = fragment.path.split('/')[min_slash_count + 1]
                subdir_hit_counts[subdir_name] = subdir_hit_counts.get(subdir_name, 0) + 1
                continue
            file_summaries.append(f'{fragment.path}:\n{fragment.text}\n\n')

        if file_summaries:
            yield ''.join(file_summaries)

        if subdir_hit_counts:
            subdir_info = [f'Relevant subdirectories:\n']
            max_count = max(subdir_hit_counts.values())
            for subdir, count in sorted(subdir_hit_counts.items(), reverse=True, key=lambda pair: pair[1]):
                subdir_info.append(f"  {subdir}: {int(100.0 * count / max_count)}%\n")
            yield ''.join(subdir_info)

    async def update_project_accessed(self):
        now = datetime.utcnow()
        if self.project.accessed < now - C.PROJECT_ACCESS_UPDATE_INTERVAL:
            async with self.db.transaction() as conn:
                await projects.update_accessed(conn, self.project.id, now)
