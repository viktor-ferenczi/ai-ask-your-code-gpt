import json
import os
import shutil
import sqlite3
from contextlib import contextmanager
from sqlite3 import Cursor
from typing import List, ContextManager, Optional, Tuple, Iterator

import aiohttp
from qdrant_client import QdrantClient

import parsers
from common.constants import C, RX
from common.timer import timer
from common.tools import tiktoken_len
from embed.embedder_client import EmbedderClient, QUERY_EMBEDDERS
from model.fragment import Fragment
from model.hit import Hit
from model.tools import uuid_of_fragments
from project.collection import Collection
from project.inventory import Inventory

DOWNLOADER_URL = os.environ.get('DOWNLOADER_URL', 'http://127.0.0.1:40001')

EMBEDDER_CLIENT = EmbedderClient(QUERY_EMBEDDERS)

QDRANT_LOCATION = os.environ.get('QDRANT_LOCATION', 'localhost')
QDRANT_HTTP_PORT = int(os.environ.get('QDRANT_HTTP_PORT', '6333'))
QDRANT_GRPC_PORT = int(os.environ.get('QDRANT_GRPC_PORT', '6334'))


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

        self.__collection: Optional[Collection] = None

    @property
    def collection(self) -> Collection:
        if self.__collection is None:
            database = QdrantClient(location=QDRANT_LOCATION, port=QDRANT_HTTP_PORT, grpc_port=QDRANT_GRPC_PORT, prefer_grpc=True)
            self.__collection = Collection(database, self.project_id)
        return self.__collection

    @contextmanager
    def cursor(self) -> ContextManager[Cursor]:
        with sqlite3.connect(self.db_path) as db:
            yield db.cursor()
            db.commit()

    @property
    def exists(self):
        return os.path.exists(self.db_path)

    @property
    def progress(self):
        inventory = Inventory()
        if inventory.has_project_embedded(self.project_id):
            return 100

        fragment_count, embedded_count = self.count_embedded_fragments()
        return int(round(fragment_count / embedded_count)) if embedded_count else 0

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

        await self.collection.create()

    async def drop_database(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        try:
            await self.collection.delete()
        except KeyboardInterrupt:
            raise
        except:
            pass

    def index_by_path(self, cursor: Cursor):
        cursor.execute('CREATE INDEX idx_fragment_path ON Fragment(path)')

    def index_by_lineno(self, cursor: Cursor):
        cursor.execute('CREATE INDEX idx_fragment_lineno ON Fragment(lineno)')

    def index_by_name(self, cursor: Cursor):
        cursor.execute('CREATE INDEX idx_fragment_name ON Fragment(name)')

    def insert_fragment(self, cursor: Cursor, fragment: Fragment):
        cursor.execute('INSERT INTO Fragment(uuid, path, lineno, depth, type, name, text) VALUES (?, ?, ?, ?, ?, ?, ?)',
                       (fragment.uuid, fragment.path, fragment.lineno, fragment.depth, fragment.type, fragment.name, fragment.text))

    def mark_fragments_embedded(self, cursor: Cursor, uuids: List[str]):
        if not uuids:
            return
        placeholders = ','.join('?' for _ in uuids)
        cursor.execute(f'UPDATE Fragment SET embedded=1 WHERE uuid IN ({placeholders})', tuple(uuids))

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

    def search_by_ext_path(self, cursor: Cursor, ext: str, path: str, limit: int = 1) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute("SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE path LIKE ? AND path LIKE ? ORDER BY LENGTH(path) - LENGTH(REPLACE(path, '/', '')), path, lineno LIMIT ?", (f'%{ext}', f'{path}%', limit))]

    def search_by_ext_name(self, cursor: Cursor, ext: str, name: str, limit: int = 1) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute("SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE name LIKE ? AND path LIKE ? ORDER BY LENGTH(path) - LENGTH(REPLACE(path, '/', '')), path, lineno LIMIT ?", (f'%{ext}', f'%{name}', limit))]

    def search_by_ext(self, cursor: Cursor, ext: str, limit: int = 1) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute("SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE name LIKE ? ORDER BY LENGTH(path) - LENGTH(REPLACE(path, '/', '')), path, lineno LIMIT ?", (f'%{ext}', limit))]

    def search_by_path_tail_name(self, cursor: Cursor, path: str, tail: str, name: str, limit: int = 1) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute("SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE path LIKE ? AND path LIKE ? AND name LIKE ? ORDER BY path, lineno LIMIT ?", (f'{path}%', f'%{tail}', f'%{name}', limit))]

    def search_by_path_tail_name_unlimited(self, cursor: Cursor, path: str, tail: str, name: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute("SELECT uuid, path, lineno, depth, type, name, text FROM Fragment WHERE path LIKE ? AND path LIKE ? AND name LIKE ? ORDER BY path, lineno", (f'{path}%', f'%{tail}', f'%{name}'))]

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
            for row in cursor.execute('SELECT COUNT(1), SUM(embedded) FROM Fragment'):
                return (row[0] or 0), (row[1] or 0)
            return 0, 0

    async def delete(self):
        inventory = Inventory()
        inventory.delete_project(self.project_id)

        await self.drop_database()

        if os.path.isdir(self.data_dir):
            shutil.rmtree(self.data_dir)

    @classmethod
    async def download(cls, url: str, *, timeout: float = 30.0) -> str:
        with timer(f'Downloaded {url!r}'):
            async with aiohttp.ClientSession() as session:
                data = json.dumps(dict(url=url))
                async with session.post(f'{DOWNLOADER_URL}/download', data=data, headers={'Accept': 'text/json'}, timeout=timeout) as response:
                    if response.status != 200:
                        print(f'Failed to download archive {url!r}')
                        raise ProjectError(f'Failed to download archive: {url}')
                    content: bytes = await response.content.read()
                    project_id = content.decode('utf-8').strip()
                    assert RX.GUID.match(project_id)
                    print(f'Project ID is {project_id}')
                    return project_id

    async def search(self, *, path: str = '', tail: str = '', name: str = '', text: str = '', limit: int = 1) -> List[Hit]:
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

        # Vector database search
        parser_cls = (
                parsers.detect(tail) or
                parsers.detect(path) or
                parsers.TextParser
        )
        instruction = parser_cls.query_instruction
        fragment_uuids = uuid_of_fragments(fragments)
        results = await self.search_vector_database(fragment_uuids, instruction, text, limit)

        # Stable sort order is determined by the scores (or by UUID if it is a tie)
        results.sort(key=lambda result: (-result.score, result.uuid))

        # Source of fragments
        if fragments:
            # Text search is
            fragment_map = {fragment.uuid: fragment for fragment in fragments}
        else:
            # Pull the fragments referenced from the vector database results
            with self.cursor() as cursor:
                uuids = [result.uuid for result in results]
                fragment_map = {fragment.uuid: fragment for fragment in self.list_fragments_by_uuid(cursor, uuids)}

        # Combine into hits, preserve vector results sort order
        hits = [Hit.from_fragment(result.score, fragment_map[result.uuid]) for result in results[:limit]]
        return hits

    async def search_vector_database(self, uuids: List[str], instruction: str, query: str, limit: int):
        embedding = await EMBEDDER_CLIENT.embed_query(instruction, query, timeout=20.0)
        assert embedding.shape == (1, 768)
        results = await self.collection.search(embedding[0].tolist(), limit=limit, uuids=uuids)
        return results

    async def summarize(self, *, path: str = '', tail: str = '', name: str = '') -> str:
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

        limit = 2000 if not path and not name else 1000
        if sum(tiktoken_len(line) for line in summary) > limit:
            summary = [line for line in summary if not line.lstrip().startswith('Usages:')]
        if sum(tiktoken_len(line) for line in summary) > limit:
            summary = [line for line in summary if not line.lstrip().startswith('Variables:')]
        if sum(tiktoken_len(line) for line in summary) > limit:
            summary = [line for line in summary if not line.lstrip().startswith('Methods:')]

        total = sum(tiktoken_len(line) for line in summary)
        if total > limit:
            summary = summary[:len(summary) * limit // total]

        return '\n'.join(summary)

    def summarize_fragments(self, fragments: List[Fragment]) -> Iterator[str]:
        fragments.sort(key=lambda fragment: (fragment.path.count('/'), fragment.path, fragment.lineno))
        for fragment in fragments:
            if fragment.type == 'summary':
                yield fragment.text
