import asyncio
import random
import sqlite3
from sqlite3 import Cursor
from typing import List, Tuple, Iterator, Dict, Any, Optional

import numpy as np

from common.constants import C, RX
from common.timer import timer
from common.tools import tiktoken_len
from model.fragment import Fragment
from model.hit import Hit
from storage import projects, archives
from storage.database import Database
from storage.projects import Project
from storage.pubsub import PubSub, ChannelName
from storage.scheduler import Scheduler, Task, Operation, TaskState


class BackendError(Exception):
    pass


TInfo = Dict[str, Any]


class Backend:
    def __init__(self, db: Database, project: Project) -> None:
        self.db = db
        self.project = project
        self.pubsub = PubSub(self.db)
        self.scheduler = Scheduler(self.db)

    @classmethod
    async def ensure_project(cls, db: Database, uid: str, project_name: str) -> Optional["Backend"]:
        async with db.transaction() as conn:
            project = await projects.find_by_name(conn, uid, project_name)
            if project is None:
                project = await projects.create(conn, uid, project_name)
        return Backend(db, project)

    async def download(self, url: Optional[str], *, timeout: float = 30.0 if C.PRODUCTION else 999999.0) -> TInfo:
        task: Task = Task(
            operation=Operation.DownloadArchive,
            params=dict(url=url, project_id=self.project)
        )

        async with self.pubsub.listen(ChannelName.DownloadCompleted.name):
            await self.scheduler.schedule(task)
            try:
                await self.pubsub.receive_with_timeout(timeout, predicate=lambda event: event.params.get('url') == url)
            except asyncio.TimeoutError:
                pass

        task = await self.scheduler.get_task(task.created)
        if task.state == TaskState.failed:
            return dict(
                status=f'Failed to download archive: {task.message}',
                hint='Try the download URL in a private browser. Does it work?',
                support_site='https://askyourcode.ai',
            )
        if task.state == TaskState.crashed:
            return dict(
                status='Internal error while downloading archive.',
                hint='Please try again later. The backend is monitored and we will fix this.',
                support_site='https://askyourcode.ai',
            )
        if task.state != TaskState.completed:
            return dict(
                status='The download is still in progress, please try to get a project summary later.'
            )
        return dict(status='Archive downloaded')

    async def delete(self):
        pass

    async def search(self, *, path: str = '', tail: str = '', name: str = '', text: str = '', limit: int = 1) -> List[Hit]:
        for _ in range(5):
            try:
                return await self.search_inner(path=path, tail=tail, name=name, text=text, limit=limit)
            except sqlite3.OperationalError:
                await asyncio.sleep(0.1 + 0.4 * random.random())

        return await self.search_inner(path=path, tail=tail, name=name, text=text, limit=limit)

    async def search_inner(self, *, path: str, tail: str, name: str, text: str, limit: int) -> List[Hit]:
        with self.cursor() as cursor:
            if text:
                fragments: List[Fragment] = self.search_by_path_tail_name_unlimited(cursor, path, tail, name)
            else:
                fragments: List[Fragment] = self.search_by_path_tail_name(cursor, path, tail, name, limit)

        # FIXME: Integrate this into the query
        fragments = [fragment for fragment in fragments if fragment.category != 'summary']

        if not text:
            # Ordering and limit was already applied in SQL
            count = len(fragments)
            return [Hit.from_fragment(1.0 - i / count, fragment)
                    for i, fragment in enumerate(fragments)]

        # Full text search
        fts_uuids = await self.free_text_search(text, 1000 + limit if fragments else limit)
        if not fts_uuids:
            return []

        if fragments:
            # Consider only the fragments selected by name, tail or path
            fragment_map = {fragment.uuid: fragment for fragment in fragments}
            fts_uuids = [uuid for uuid in fts_uuids if uuid in fragment_map]
        else:
            # Pull the fragments referenced from the full text search uuids
            with self.cursor() as cursor:
                fragments = self.list_fragments_by_uuid(cursor, fts_uuids)
            fragment_map = {fragment.uuid: fragment for fragment in fragments}

        # Combine into hits, preserve full text search fts_uuids sort order
        count = len(fts_uuids)
        hits = [Hit.from_fragment(1.0 - i / count, fragment_map[uuid]) for i, uuid in enumerate(fts_uuids[:limit])]
        return hits

    """ FTS query expression syntax:
    <phrase>    := string [*]
    <phrase>    := <phrase> + <phrase>
    <neargroup> := NEAR ( <phrase> <phrase> ... [, N] )
    <query>     := [ [-] <colspec> :] [^] <phrase>
    <query>     := [ [-] <colspec> :] <neargroup>
    <query>     := [ [-] <colspec> :] ( <query> )
    <query>     := <query> AND <query>
    <query>     := <query> OR <query>
    <query>     := <query> NOT <query>
    <colspec>   := colname
    <colspec>   := { colname1 colname2 ... }

    Phrases are escaped by double quotes.
    See: https://www.sqlite.org/fts5.html
    """

    async def free_text_search(self, query: str, limit: int) -> List[str]:
        def edq(s):
            return s.replace('"', '""')

        query = ' '.join(f'"{edq(s)}"' for s in query.split() if s.strip())

        if not query:
            return []

        print(f'FTS Query: {query}')

        try:
            with self.cursor() as cursor:
                return [row[0] for row in cursor.execute('SELECT uuid FROM FragText WHERE text MATCH ? ORDER BY rank LIMIT ?', (query, limit))]
        except sqlite3.OperationalError as e:
            raise BackendError(f'Failed to search the project with SQLite FTS5 query {query!r}. Reason: {e}')

    async def summarize(self, *, path: str = '', tail: str = '', name: str = '', token_limit: int = 0) -> str:
        for _ in range(5):
            try:
                return await self.summarize_inner(path=path, tail=tail, name=name, token_limit=token_limit)
            except sqlite3.OperationalError:
                await asyncio.sleep(0.1 + 0.4 * random.random())

        return await self.summarize_inner(path=path, tail=tail, name=name, token_limit=token_limit)

    async def summarize_inner(self, *, path: str, tail: str, name: str, token_limit: int) -> str:
        with self.cursor() as cursor:
            fragments: List[Fragment] = self.search_by_path_tail_name_unlimited(cursor, path, tail, name)

        if fragments:
            summary = '\n'.join(self.summarize_fragments(path, fragments))
        else:
            if tail or name:
                return ''
            with self.cursor() as cursor:
                fragments: List[Fragment] = self.search_by_path_tail_name_unlimited(cursor, '/', '', '')
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
            if fragment.category == 'summary':
                strip_text = fragment.body.strip('\n')
                file_summaries.append(f'{strip_text}\n\n')

        if file_summaries:
            yield ''.join(file_summaries)

        if subdir_hit_counts:
            subdir_info = [f'Matches under subdirectories:\n']
            for subdir, count in sorted(subdir_hit_counts.items()):
                subdir_info.append(f'  {subdir}: {count}\n')
            yield ''.join(subdir_info)

    def get_all_fragments(self, cursor: Cursor) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT uuid, path, lineno, depth, type, name, text FROM Fragment ORDER BY path, lineno')]

    def get_fragments_to_embed(self, cursor: Cursor, limit: int) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE embedded=0 ORDER BY path, lineno LIMIT ?', (limit,))]

    def get_fragments_by_paths(self, cursor: Cursor, paths: List[str], limit: int) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE path IN (?) ORDER BY path, lineno LIMIT ?', (paths, limit))]

    def get_fragments_by_path_tail(self, cursor: Cursor, tail: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE path LIKE ?', (f'%{tail}',))]

    def get_fragments_by_name_tail(self, cursor: Cursor, tail: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE name LIKE ?', (f'%{tail}',))]

    def get_fragments_by_path_name(self, cursor: Cursor, path: str, name: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE path LIKE ? AND name LIKE ?', (f'%{path}', f'{name}%'))]

    def get_fragments_by_path(self, cursor: Cursor, path: str, name: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE path LIKE ?', (f'%{path}',))]

    def get_fragments_by_name(self, cursor: Cursor, path: str, name: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE path LIKE ?', (f'{name}%',))]

    def get_fragments_by_path_ext(self, cursor: Cursor, path: str, ext: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE path LIKE ? AND path LIKE ?', (f'{path}%', f'%{ext}'))]

    def get_fragments_by_name_ext(self, cursor: Cursor, name: str, ext: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE name LIKE ? AND path LIKE ?', (f'%{name}', f'%{ext}'))]

    def get_inserted_fragment_keys(self, cursor: Cursor):
        return [tuple(row) for row in cursor.execute('SELECT path, type, lineno FROM Fragment')]

    def search_by_ext_path(self, cursor: Cursor, ext: str, path: str, limit: int = 1) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute("SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE path LIKE ? AND path LIKE ? ORDER BY LENGTH(path) - LENGTH(REPLACE(path, '/', '')), path, lineno LIMIT ?", (f'%{ext}', f'{path}%', limit))]

    def search_by_ext_name(self, cursor: Cursor, ext: str, name: str, limit: int = 1) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute("SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE name LIKE ? AND path LIKE ? ORDER BY LENGTH(path) - LENGTH(REPLACE(path, '/', '')), path, lineno LIMIT ?", (f'%{ext}', f'%{name}', limit))]

    def search_by_ext(self, cursor: Cursor, ext: str, limit: int = 1) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute("SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE name LIKE ? ORDER BY LENGTH(path) - LENGTH(REPLACE(path, '/', '')), path, lineno LIMIT ?", (f'%{ext}', limit))]

    def search_by_path_tail_name(self, cursor: Cursor, path: str, tail: str, name: str, limit: int = 1) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute("SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE path LIKE ? AND path LIKE ? AND name LIKE ? ORDER BY LENGTH(name), path, lineno LIMIT ?", (f'{path}%', f'%{tail}', f'%{name}', limit))]

    def search_by_path_tail_name_unlimited(self, cursor: Cursor, path: str, tail: str, name: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute("SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE path LIKE ? AND path LIKE ? AND name LIKE ? ORDER BY LENGTH(name), path, lineno", (f'{path}%', f'%{tail}', f'%{name}'))]

    def get_distinct_paths_ordered(self, cursor: Cursor):
        return [row[0] for row in cursor.execute("SELECT DISTINCT path FROM Fragment ORDER BY path")]

    def list_fragments_by_uuid(self, cursor: Cursor, uuids: List[str]) -> List[Fragment]:
        if not uuids:
            return []
        placeholders = ','.join('?' for _ in uuids)
        fragments = [Fragment(*row) for row in cursor.execute(f'SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE uuid IN ({placeholders})', tuple(uuids))]
        return fragments

    def count_fragments(self) -> int:
        with self.cursor() as cursor:
            for row in cursor.execute('SELECT COUNT(1) FROM Fragment'):
                return row[0] or 0
            return 0

    def count_embedded_fragments(self) -> Tuple[int, int]:
        with self.cursor() as cursor:
            for row in cursor.execute("SELECT COUNT(1), SUM(embedded) FROM Fragment WHERE type == 'documentation'"):
                return (row[0] or 0), (row[1] or 0)
            return 0, 0
