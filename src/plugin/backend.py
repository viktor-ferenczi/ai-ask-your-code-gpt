import asyncio
from typing import List, Iterator, Dict, Any, Optional

import numpy as np

from common.constants import C
from common.tools import tiktoken_len
from model.fragment import Fragment
from model.hit import Hit
from storage import projects
from storage.database import Database
from storage.fragments import search_by_path_tail_name_unlimited, search_by_path_tail_name, list_fragments_by_id, Fragment as DbFragment
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
    )


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

        for _ in range(10):
            task = await self.scheduler.get_task(task.created)
            if task.state != TaskState.pending:
                break
            await asyncio.sleep(0.05)

        if task.state == TaskState.failed:
            return dict(
                status=f'Failed to download archive: {task.message}',
                hint='Try the download URL in a private browser. Does it work?',
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

    async def delete(self):
        pass

    async def search(self, *, path: str = '', tail: str = '', name: str = '', text: str = '', limit: int = 1) -> List[Hit]:
        async with self.db.connection() as conn:
            if text:
                pairs = await search_by_path_tail_name_unlimited(conn, self.project.id, path, tail, name)
            else:
                pairs = await search_by_path_tail_name(conn, self.project.id, path, tail, name, limit)

        fragments = [fragment_from_db_fragment(*pair) for pair in pairs]

        # FIXME: Integrate this into the query
        fragments = [fragment for fragment in fragments if fragment.type != 'summary']

        if not text:
            # Ordering and limit was already applied in SQL
            count = len(fragments)
            return [Hit.from_fragment(1.0 - i / count, fragment)
                    for i, fragment in enumerate(fragments)]

        # Full text search
        fts_ids = await self.free_text_search(text, 1000 + limit if fragments else limit)
        if not fts_ids:
            return []

        if fragments:
            # Consider only the fragments selected by name, tail or path
            fragment_map = {fragment.uuid: fragment for fragment in fragments}
            fts_ids = [uuid for uuid in fts_ids if uuid in fragment_map]
        else:
            # Pull the fragments referenced from the full text search uuids
            async with self.db.connection() as conn:
                pairs = await list_fragments_by_id(conn, self.project.id, list(map(int, fts_ids)))

            fragments = [fragment_from_db_fragment(*pair) for pair in pairs]
            fragment_map = {fragment.uuid: fragment for fragment in fragments}

        # Combine into hits, preserve full text search fts_uuids sort order
        count = len(fts_ids)
        hits = [Hit.from_fragment(1.0 - i / count, fragment_map[uuid]) for i, uuid in enumerate(fts_ids[:limit])]
        return hits

    async def free_text_search(self, query: str, limit: int) -> List[str]:
        sql = '''
            SELECT s.id, ts_rank_cd(to_tsvector(s.body), query) AS rank
            FROM (
                SELECT c.id, c.body
                FROM file AS f
                INNER JOIN fragment AS c ON c.partition_key = left(f.document_cs, 2) AND c.document_cs = f.document_cs
                WHERE f.project_id = $1
            ) AS s, phraseto_tsquery($2) query 
            WHERE s.body @@ query
            ORDER BY rank DESC
            LIMIT $3
        '''
        async with self.db.connection() as conn:
            return [str(row[0]) for row in await conn.fetch(sql, self.project.id, query, limit)]

    async def summarize(self, *, path: str = '', tail: str = '', name: str = '', token_limit: int = 0) -> str:
        async with self.db.connection() as conn:
            pairs = await search_by_path_tail_name(conn, self.project.id, path, tail, name, 1000)

        fragments = [fragment_from_db_fragment(*pair) for pair in pairs]

        if fragments:
            summary = '\n'.join(self.summarize_fragments(path, fragments))
        else:
            if tail or name:
                return ''
            async with self.db.connection() as conn:
                pairs = await search_by_path_tail_name_unlimited(conn, self.project.id, '/', '', '')
                fragments = [fragment_from_db_fragment(*pair) for pair in pairs]
            if not fragments:
                return ''
            return 'No file matched the summary query. Discover the directory structure of the project by summarizing path=/\n'

        summary = summary.split('\n')

        extensions = ' '.join(sorted(set('.' + fragment.path.rsplit('.', 1)[-1] for fragment in fragments if fragment.path and '.' in fragment.path.replace('/.', '/'))))
        if extensions:
            if len(extensions) > 1:
                summary.insert(0, f'File extensions: {extensions}\n')
            else:
                summary.insert(0, f'File extension: {extensions}\n')

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

    def summarize_fragments(self, path_query: str, fragments: List[Fragment]) -> Iterator[str]:
        if not fragments:
            return

        fragments.sort(key=lambda fragment: (fragment.path.count('/'), fragment.path, fragment.lineno))

        min_slash_count = path_query.rstrip('/').count('/')

        subdir_hit_counts = {}
        file_summaries = []
        for fragment in fragments:
            extra_slashes = fragment.path.count('/') - min_slash_count
            if extra_slashes > 1:
                subdir_name = fragment.path.split('/')[min_slash_count + 1]
                subdir_hit_counts[subdir_name] = subdir_hit_counts.get(subdir_name, 0) + 1
                continue
            if fragment.type == 'summary':
                strip_text = fragment.text.strip('\n')
                file_summaries.append(f'{strip_text}\n\n')

        if file_summaries:
            yield ''.join(file_summaries)

        if subdir_hit_counts:
            subdir_info = [f'Relevant subdirectories:\n']
            max_count = max(subdir_hit_counts.values())
            for subdir, count in sorted(subdir_hit_counts.items(), reverse=True, key=lambda pair: pair[1]):
                subdir_info.append(f"  {subdir}: {int(100.0 * count / max_count)}%\n")
            yield ''.join(subdir_info)
