import asyncio
import json
import os
import random
import shutil
import sqlite3
from contextlib import contextmanager
from sqlite3 import Cursor
from typing import List, ContextManager, Tuple, Iterator

import aiohttp
from aiohttp import ClientError

from common.constants import C, RX
from common.text import decode_replace
from common.timer import timer
from common.tools import tiktoken_len
from model.fragment import Fragment
from model.hit import Hit
from project.inventory import Inventory

DOWNLOADER_URL = os.environ.get('DOWNLOADER_URL', 'http://127.0.0.1:40001')


class ProjectError(Exception):
    pass


class Project:
    dirname = 'projects'

    def __init__(self, project_id: str) -> None:
        self.project_id: str = project_id

        self.data_dir: str = os.path.join(C.DATA_DIR, self.dirname, self.project_id[:2], self.project_id[2:4], self.project_id)
        os.makedirs(self.data_dir, exist_ok=True)

        self.archive_path: str = os.path.join(self.data_dir, 'archive.zip')
        self.db_path: str = os.path.join(self.data_dir, 'project.sqlite')

    @contextmanager
    def cursor(self) -> ContextManager[Cursor]:
        with sqlite3.connect(self.db_path) as db:
            yield db.cursor()
            db.commit()

    @property
    def exists(self):
        return os.path.exists(self.db_path)

    async def get_progress(self):
        if not self.exists:
            return 0

        for _ in range(5):
            try:
                inventory = Inventory()
                if inventory.has_project_embedded(self.project_id):
                    return 100

                # fragment_count, embedded_count = self.count_embedded_fragments()
                # return int(round(fragment_count / embedded_count)) if embedded_count else 0
            except sqlite3.OperationalError:
                await asyncio.sleep(0.1 + 0.4 * random.random())

        return 0

    async def create_database(self):
        if os.path.exists(self.db_path):
            return

        with self.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE Fragment(
                    uuid TEXT PRIMARY KEY,
                    path TEXT NOT NULL,
                    lineno INTEGER NOT NULL,
                    depth INTEGER NOT NULL,
                    type TEXT NOT NULL,
                    name TEXT,
                    text TEXT NOT NULL,
                    embedded INTEGER DEFAULT 0 NOT NULL
                )
            ''')

    async def drop_database(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def index_by_path(self, cursor: Cursor):
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_fragment_path ON Fragment(path)')

    def index_by_lineno(self, cursor: Cursor):
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_fragment_lineno ON Fragment(lineno)')

    def index_by_name(self, cursor: Cursor):
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_fragment_name ON Fragment(name)')

    def insert_fragment(self, cursor: Cursor, fragment: Fragment):
        cursor.execute('INSERT INTO Fragment(uuid, path, lineno, depth, type, name, text, embedded) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                       (fragment.uuid, fragment.path, fragment.lineno, fragment.depth, fragment.type, fragment.name, fragment.text, fragment.type != 'documentation'))

    def mark_fragments_embedded(self, cursor: Cursor, uuids: List[str]):
        if not uuids:
            return
        placeholders = ','.join('?' for _ in uuids)
        cursor.execute(f'UPDATE Fragment SET embedded=1 WHERE uuid IN ({placeholders})', tuple(uuids))

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

    async def delete(self):
        inventory = Inventory()
        inventory.delete_project(self.project_id)

        await self.drop_db_dir()

    async def cleanup(self):
        inventory = Inventory()
        inventory.mark_project_cleaned(self.project_id)

        await self.drop_db_dir()

    async def drop_db_dir(self):
        await self.drop_database()

        if os.path.isdir(self.data_dir):
            shutil.rmtree(self.data_dir)

    @classmethod
    async def download(cls, url: str, *, timeout: float = 30.0 if C.PRODUCTION else 999999.0) -> str:
        try:
            with timer(f'Downloaded {url!r}'):
                async with aiohttp.ClientSession() as session:
                    data = json.dumps(dict(url=url))
                    async with session.post(f'{DOWNLOADER_URL}/download', data=data, headers={'Accept': 'text/json'}, timeout=timeout) as response:
                        content: bytes = await response.content.read()
                        if response.status != 200:
                            reason = decode_replace(content).strip()
                            print(f'Failed to download archive {url!r}: {reason}')
                            raise ProjectError(reason)
                        project_id = content.decode('utf-8').strip()
                        assert RX.GUID.match(project_id)
                        print(f'Project ID is {project_id}')
                        return project_id
        except ClientError as e:
            raise ProjectError(f'Failed to download archive {url!r}: [{e.__class__.__name__}] {e}')

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
        fragments = [fragment for fragment in fragments if fragment.type != 'summary']

        if not text:
            # Ordering and limit was already applied in SQL
            count = len(fragments)
            return [Hit.from_fragment(1.0 - i / count, fragment)
                    for i, fragment in enumerate(fragments)]

        # Full text search
        fts_uuids = await self.free_text_search(text, 1000 + limit if fragments else limit)
        if not fts_uuids:
            raise ProjectError('No hits with this search expression. Try to pass an SQLite FTS5 full-text query expression in the `text` parameter instead. Always prepend `?FTS5:` before FTS5 search expressions.')

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
        if query.startswith('?FTS5:'):
            query = query[6:].strip()
        else:
            def edq(s):
                return s.replace('"', '""')
            query = ' '.join(f'"{edq(s)}"' for s in query.split() if s.strip())

        if not query:
            return []

        print(f'FTS5 query: {query}')

        try:
            with self.cursor() as cursor:
                return [row[0] for row in cursor.execute('SELECT uuid FROM FragText WHERE text MATCH ? ORDER BY rank LIMIT ?', (query, limit))]
        except sqlite3.OperationalError as e:
            raise ProjectError(f'Failed to search the project with SQLite FTS5 query {query!r}. Reason: {e}')

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
            summary = '\n'.join(self.summarize_fragments(fragments))
        else:
            if tail or name:
                return ''
            summary = [
                'No directory or file matched the summary query.\n',
                'Path of all files in the project:\n'
            ]
            with self.cursor() as cursor:
                summary.extend(f'{p}\n' for p in self.get_distinct_paths_ordered(cursor))
            summary = ''.join(summary)

        summary = summary.split('\n')

        extensions = ' '.join(sorted(set('.' + fragment.path.rsplit('.', 1)[-1] for fragment in fragments if fragment.path and '.' in fragment.path.replace('/.', '/'))))
        if extensions:
            if len(extensions) > 1:
                summary.insert(0, f'File extensions: {extensions}\n')
            else:
                summary.insert(0, f'File extension: {extensions}\n')

        if not token_limit:
            token_limit = 2000 if not path and not name else 1000

        if sum(tiktoken_len(line) for line in summary) > token_limit:
            summary = [line for line in summary if not line.lstrip().startswith('Usage')]

        if sum(tiktoken_len(line) for line in summary) > token_limit:
            summary = [line for line in summary if not line.lstrip().startswith('Variable')]

        if sum(tiktoken_len(line) for line in summary) > token_limit:
            summary = [line for line in summary if not line.lstrip().startswith('Method')]

        total = sum(tiktoken_len(line) for line in summary)
        if total > token_limit:
            summary = summary[:len(summary) * token_limit // total]

        return '\n'.join(summary)

    def summarize_fragments(self, fragments: List[Fragment]) -> Iterator[str]:
        fragments.sort(key=lambda fragment: (fragment.path.count('/'), fragment.path, fragment.lineno))
        for fragment in fragments:
            if fragment.type == 'summary':
                yield fragment.text
