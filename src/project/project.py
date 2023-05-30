import json
import os
import shutil
import sqlite3
from contextlib import contextmanager
from sqlite3 import Cursor
from typing import List, ContextManager, Optional, Tuple, Iterator

import aiohttp
from qdrant_client import QdrantClient

import doc_types
from common.constants import C, RX
from common.timer import timer
from embed.embedder_client import EmbedderClient, QUERY_EMBEDDERS
from model.fragment import Fragment
from model.hit import Hit
from model.tools import uuid_of_fragments
from project.collection import Collection
from project.inventory import Inventory
from common.tools import tiktoken_len

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
                    text TEXT NOT NULL,
                    name TEXT,
                    embedded INTEGER DEFAULT 0 NOT NULL
                )
            ''')

        await self.collection.create()

    async def drop_database(self):
        os.remove(self.db_path)
        await self.collection.delete()

    def index_by_path(self, cursor: Cursor):
        cursor.execute('CREATE INDEX idx_fragment_path ON Fragment(path)')

    def index_by_lineno(self, cursor: Cursor):
        cursor.execute('CREATE INDEX idx_fragment_lineno ON Fragment(lineno)')

    def index_by_name(self, cursor: Cursor):
        cursor.execute('CREATE INDEX idx_fragment_name ON Fragment(name)')

    def insert_fragment(self, cursor: Cursor, fragment: Fragment):
        cursor.execute('INSERT INTO Fragment(uuid, path, lineno, text, name) VALUES (?, ?, ?, ?, ?)',
                       (fragment.uuid, fragment.path, fragment.lineno, fragment.text, fragment.name))

    def mark_fragments_embedded(self, cursor: Cursor, uuids: List[str]):
        if not uuids:
            return
        placeholders = ','.join('?' for _ in uuids)
        cursor.execute(f'UPDATE Fragment SET embedded=1 WHERE uuid IN ({placeholders})', tuple(uuids))

    def get_fragments_to_embed(self, cursor: Cursor, limit: int) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT lineno, text, name, uuid, path FROM Fragment WHERE embedded=0 ORDER BY path, lineno LIMIT ?', (limit,))]

    def get_fragments_by_paths(self, cursor: Cursor, paths: List[str], limit: int) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT lineno, text, name, uuid, path FROM Fragment WHERE path IN (?) ORDER BY path, lineno LIMIT ?', (paths, limit))]

    def get_fragments_by_path_tail(self, cursor: Cursor, tail: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT lineno, text, name, uuid, path FROM Fragment WHERE path LIKE ?', (f'%{tail}',))]

    def get_fragments_by_name_tail(self, cursor: Cursor, tail: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT lineno, text, name, uuid, path FROM Fragment WHERE name LIKE ?', (f'%{tail}',))]

    def get_fragments_by_path_name(self, cursor: Cursor, path: str, name: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT lineno, text, name, uuid, path FROM Fragment WHERE path LIKE ? AND name LIKE ?', (f'%{path}', f'{name}%'))]

    def get_fragments_by_path(self, cursor: Cursor, path: str, name: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT lineno, text, name, uuid, path FROM Fragment WHERE path LIKE ?', (f'%{path}',))]

    def get_fragments_by_name(self, cursor: Cursor, path: str, name: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT lineno, text, name, uuid, path FROM Fragment WHERE path LIKE ?', (f'{name}%',))]

    def get_fragments_by_path_ext(self, cursor: Cursor, path: str, ext: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT lineno, text, name, uuid, path FROM Fragment WHERE path LIKE ? AND path LIKE ?', (f'{path}%', f'%{ext}'))]

    def get_fragments_by_name_ext(self, cursor: Cursor, name: str, ext: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT lineno, text, name, uuid, path FROM Fragment WHERE name LIKE ? AND path LIKE ?', (f'%{name}', f'%{ext}'))]

    def search_by_ext_path(self, cursor: Cursor, ext: str, path: str, limit: int = 1) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute("SELECT lineno, text, name, uuid, path FROM Fragment WHERE path LIKE ? AND path LIKE ? ORDER BY LENGTH(path) - LENGTH(REPLACE(path, '/', '')), path, lineno LIMIT ?", (f'%{ext}', f'{path}%', limit))]

    def search_by_ext_name(self, cursor: Cursor, ext: str, name: str, limit: int = 1) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute("SELECT lineno, text, name, uuid, path FROM Fragment WHERE name LIKE ? AND path LIKE ? ORDER BY LENGTH(path) - LENGTH(REPLACE(path, '/', '')), path, lineno LIMIT ?", (f'%{ext}', f'%{name}', limit))]

    def search_by_ext(self, cursor: Cursor, ext: str, limit: int = 1) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute("SELECT lineno, text, name, uuid, path FROM Fragment WHERE name LIKE ? ORDER BY LENGTH(path) - LENGTH(REPLACE(path, '/', '')), path, lineno LIMIT ?", (f'%{ext}', limit))]

    def search_by_path_tail_name(self, cursor: Cursor, path: str, tail: str, name: str, limit: int = 1) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute("SELECT lineno, text, name, uuid, path FROM Fragment WHERE path LIKE ? AND path LIKE ? AND name LIKE ? ORDER BY path, lineno LIMIT ?", (f'{path}%', f'%{tail}', f'%{name}', limit))]

    def search_by_path_tail_name_unlimited(self, cursor: Cursor, path: str, tail: str, name: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute("SELECT lineno, text, name, uuid, path FROM Fragment WHERE path LIKE ? AND path LIKE ? AND name LIKE ? ORDER BY path, lineno", (f'{path}%', f'%{tail}', f'%{name}'))]

    def list_fragments_by_uuid(self, cursor: Cursor, uuids: List[str]) -> List[Fragment]:
        if not uuids:
            return []
        placeholders = ','.join('?' for _ in uuids)
        fragments = [Fragment(*row) for row in cursor.execute(f'SELECT lineno, text, name, uuid, path FROM Fragment WHERE uuid IN ({placeholders})', tuple(uuids))]
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

        if not text:
            # Ordering and limit was already applied in SQL
            count = len(fragments)
            return [Hit.from_fragment(1.0 - i / count, fragment)
                    for i, fragment in enumerate(fragments)]

        # Vector database search
        doc_type_cls = (
                doc_types.detect_by_extension(tail) or
                doc_types.detect_by_extension(path) or
                doc_types.TextDocType
        )
        instruction = doc_type_cls.query_instruction
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

        if not fragments:
            return ''

        summary = ''.join(f'{line}\n' for line in self.summarize_fragments(fragments))
        return summary

    def summarize_fragments(self, fragments: List[Fragment]) -> Iterator[str]:
        yield from self.summarize_docs([fragment for fragment in fragments if not fragment.name])
        yield from self.summarize_code([fragment for fragment in fragments if fragment.name])

    def summarize_code(self, fragments) -> Iterator[str]:
        if not fragments:
            return

        fragments.sort(key=lambda fragment: (fragment.name, fragment.path.count('/'), fragment.path, fragment.lineno))

        names = sorted(set(fragment.name for fragment in fragments))

        # Shorten
        while names:
            total = sum(tiktoken_len(name) for name in names)
            if total <= 1000:
                break

            max_dots = max(name.count('.') for name in names)
            if max_dots:
                names = [name for name in names if name.count('.') < max_dots]
            else:
                if len(set(name.lower() != name for name in names)) == 2:
                    names = [name for name in names if name.lower() == name]
                else:
                    names = names[:len(names) * 1000 // total]

        yield from names

    def summarize_docs(self, fragments) -> Iterator[str]:
        if not fragments:
            return

        fragments.sort(key=lambda fragment: (fragment.path.count('/'), fragment.path, fragment.lineno))

        summary = []
        for fragment in fragments:
            doc_type_cls = doc_types.detect_by_extension(fragment.path) or doc_types.TextDocType
            summary.extend(doc_type_cls.summarize(fragment.text))

        # Shorten
        while summary:
            total = sum(tiktoken_len(line) for line in summary)
            if total <= 1000:
                break

            max_level = max(line.count('#') for line in summary)
            if max_level:
                summary = [line for line in summary if line.count('#') < max_level]
            else:
                summary = summary[:len(summary) * 1000 // total]

        yield from summary
