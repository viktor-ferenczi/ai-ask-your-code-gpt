import json
import os
import shutil
import sqlite3
from contextlib import contextmanager
from math import sqrt
from sqlite3 import Cursor
from typing import List, ContextManager, Optional, Set, Tuple

import aiohttp
from qdrant_client import QdrantClient

import doc_types
from common.constants import C
from common.timer import timer
from embed.embedder_client import EmbedderClient, QUERY_EMBEDDERS
from model.fragment import Fragment
from model.hit import Hit
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

    def get_fragments_by_path(self, cursor: Cursor, path: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT lineno, text, name, uuid, path FROM Fragment WHERE path = ?', (path,))]

    def get_fragments_by_path_tail(self, cursor: Cursor, tail: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT lineno, text, name, uuid, path FROM Fragment WHERE path LIKE ?', (f'%{tail}',))]

    def get_fragments_by_name(self, cursor: Cursor, name: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT lineno, text, name, uuid, path FROM Fragment WHERE name = ?', (name,))]

    def get_fragments_by_name_tail(self, cursor: Cursor, tail: str) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT lineno, text, name, uuid, path FROM Fragment WHERE name LIKE ?', (f'%{tail}',))]

    def list_fragments_by_uuid(self, cursor: Cursor, uuids: List[str]) -> List[Fragment]:
        if not uuids:
            return []
        placeholders = ','.join('?' for _ in uuids)
        fragments = [Fragment(*row) for row in cursor.execute(f'SELECT lineno, text, name, uuid, path FROM Fragment WHERE uuid IN ({placeholders})', tuple(uuids))]
        return fragments

    def count_fragments(self) -> int:
        with self.cursor() as cursor:
            for row in cursor.execute('SELECT COUNT(1) FROM Fragment'):
                return row[0]

    def count_embedded_fragments(self) -> Tuple[int, int]:
        with self.cursor() as cursor:
            for row in cursor.execute('SELECT COUNT(1), SUM(embedded) FROM Fragment'):
                return tuple(row)

    async def delete(self):
        inventory = Inventory()
        inventory.delete_project(self.project_id)

        await self.drop_database()

        if os.path.isdir(self.data_dir):
            shutil.rmtree(self.data_dir)

    async def download(self, url: str, *, timeout: float = 30.0):
        with timer(f'Downloaded {url!r} for project {self.project_id!r}'):
            async with aiohttp.ClientSession() as session:
                data = json.dumps(dict(url=url))
                async with session.post(f'{DOWNLOADER_URL}/download/{self.project_id}', data=data, headers={'Accept': 'text/json'}, timeout=timeout) as response:
                    if response.status != 200:
                        print(f'Failed to download archive {url!r} for project {self.project_id!r}')
                        raise ProjectError(f'Failed to download archive: {url}')

    async def search(self, query: str, limit: int) -> Tuple[List[Hit], List[str]]:
        remarks = []

        await self.verify_query(query, limit)
        parts = await self.split_query(query)
        fragments, vector_query = await self.query_fragments(parts)

        embedding_completeness = self.ensure_reasonably_embedded()

        if vector_query:
            # Vector database search
            vector_results = await self.search_vector_database(fragments, limit, vector_query)

            # Stable sort order is determined by the scores (or by UUID if it is a tie)
            vector_results.sort(key=lambda result: (-result.score, result.uuid))

            # Combine into hits, preserve vector results sort order
            if fragments:
                fragment_map = {fragment.uuid: fragment for fragment in fragments}
                hits = [Hit(score=result.score, **fragment_map[result.uuid].__dict__) for result in vector_results]
            else:
                uuids = [result.uuid for result in vector_results]
                with self.cursor() as cursor:
                    fragment_map = {fragment.uuid: fragment for fragment in self.list_fragments_by_uuid(cursor, uuids)}
                hits = [Hit(score=result.score, **fragment_map[result.uuid].__dict__) for result in vector_results]
        else:
            # Relevant based on depth in tree, so the LLM will look at the broader structure first
            hits = [Hit(score=sqrt(1.0 / (1.0 + fragment.path.count('/'))), **fragment.__dict__) for fragment in fragments]
            hits.sort(key=lambda hit: (-hit.score, hit.path, hit.lineno))

            # Limiting only after the sort order is fixed
            hits = hits[:limit]

        # Remark on potential partial content
        if vector_query and embedding_completeness < 100:
            remarks.append(f'Searched {embedding_completeness}% of the content, because Indexing is still in progress.')

        return hits, remarks

    async def verify_query(self, query: str, limit: int):
        if len(query) > C.MAX_QUERY_LENGTH:
            raise ProjectError(f'The query must be at most {C.MAX_QUERY_LENGTH} characters')

        if limit < 1 or limit > C.MAX_QUERY_LIMIT:
            raise ProjectError(f'The limit must be between 1 and {C.MAX_QUERY_LIMIT}')

    async def split_query(self, query):
        query = query.strip()
        if query in ('.', '/', '?'):
            query = ''

        parts: List[str] = [part for part in query.split() if part.strip()]
        default_query = not parts

        if default_query:
            query = 'README.md readme.txt TOC.md .md .txt'  # FIXME: Add these once supported: .doc .docx .pdf
            parts = query.split()

        return parts

    def ensure_reasonably_embedded(self) -> int:
        inventory = Inventory()
        if inventory.has_project_embedded(self.project_id):
            return 100

        fragment_count, embedded_count = self.count_embedded_fragments()
        if not fragment_count:
            raise ProjectError(f'Your project is being indexed. Please try again later.')

        progress = 100
        if embedded_count < fragment_count:
            progress = int(round(100.0 * embedded_count / fragment_count))

        if progress < C.MINIMUM_PROGRESS_TO_ALLOW_SEARCH:
            raise ProjectError(f'Your project is being indexed. Current progress is {progress}%. Please try again later.')

        return progress

    async def query_fragments(self, parts):
        vector_query = []
        fragments: Set[Fragment] = set()

        with self.cursor() as cursor:
            for part in parts:

                if len(part) < 3:
                    vector_query.append(part)
                    continue

                if not part.endswith('.'):

                    if '.' in part:
                        if part.startswith('.'):
                            fragments.update(self.get_fragments_by_path_tail(cursor, part))
                            fragments.update(self.get_fragments_by_name_tail(cursor, part))
                        else:
                            fragments.update(self.get_fragments_by_path(cursor, part))
                            fragments.update(self.get_fragments_by_name(cursor, part))
                            fragments.update(self.get_fragments_by_path_tail(cursor, f'/{part}'))
                            fragments.update(self.get_fragments_by_name_tail(cursor, f'.{part}'))
                        continue

                    if '::' in part:
                        if part.startswith('::'):
                            fragments.update(self.get_fragments_by_name(cursor, part))
                            fragments.update(self.get_fragments_by_name_tail(cursor, part))
                        else:
                            fragments.update(self.get_fragments_by_name(cursor, part))
                            fragments.update(self.get_fragments_by_name_tail(cursor, f'::{part}'))
                        continue

                vector_query.append(part)

        return list(fragments), vector_query

    async def search_vector_database(self, fragments: List[Fragment], limit, vector_query):
        instruction = await self.determine_query_instruction(fragments)

        print('>>> ' + repr((instruction, ' '.join(vector_query))))

        embedding = await EMBEDDER_CLIENT.embed_query(instruction, ' '.join(vector_query), timeout=20.0)
        assert embedding.shape == (1, 768)

        uuid_filter = [fragment.uuid for fragment in fragments]

        vector_search_results = await self.collection.search(embedding[0].tolist(), limit=limit, uuid_filter=uuid_filter)
        return vector_search_results

    async def determine_query_instruction(self, fragments):
        for fragment in fragments:
            doc_type_cls = doc_types.detect_by_extension(fragment.path)
            if doc_type_cls is not None:
                return doc_type_cls.query_instruction

        return doc_types.TextDocType.query_instruction
