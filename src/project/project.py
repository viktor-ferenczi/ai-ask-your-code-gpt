import json
import os
import shutil
import sqlite3
from contextlib import contextmanager
from sqlite3 import Cursor
from typing import List, ContextManager, Optional, Set, Dict

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


class Project:

    def __init__(self, project_id: str) -> None:
        self.project_id: str = project_id

        self.data_dir: str = os.path.join(C.DATA_DIR, 'projects', self.project_id[:2], self.project_id[2:4], self.project_id)
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
        try:
            os.remove(self.db_path)
        except:
            pass

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

    def get_fragments_by_path(self, cursor: Cursor, paths: List[str], limit: int) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT lineno, text, name, uuid, path FROM Fragment WHERE path IN (?) ORDER BY path, lineno LIMIT ?', (paths, limit))]

    def get_fragments_by_path_tail(self, cursor: Cursor, path: str, limit: int) -> List[Fragment]:
        return [Fragment(*row) for row in cursor.execute('SELECT lineno, text, name, uuid, path FROM Fragment WHERE path LIKE ? ORDER BY path, lineno LIMIT ?', (f'%{path}', limit))]

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
                        raise IOError(f'Failed to download archive {url!r}')

    async def search(self, query: str, limit: int) -> List[Hit]:
        if len(query) > C.MAX_QUERY_LENGTH:
            raise ValueError(f'The query must be at most {C.MAX_QUERY_LENGTH} characters')

        if limit > C.MAX_QUERY_LIMIT:
            raise ValueError(f'The limit must be at most {C.MAX_QUERY_LIMIT}')

        query = query.strip()
        if not query or query in ('.', '/', '?'):
            query = 'README.md readme.txt TOC.md _TOC.md __TOC.md .md .txt'  # FIXME: Add these once supported: .doc .docx .pdf

        parts: List[str] = [part for part in query.split() if part.strip()]

        if not parts:
            # Empty query used by ChatGPT to check for the project's existence
            parts: List[str] = 'readme documentation text anything'.split()

        vector_query = []
        fragments: Set[Fragment] = set()
        with self.cursor() as cursor:
            for part in parts:

                if '.' not in part:
                    vector_query.append(part)
                    continue

                part_fragments = self.get_fragments_by_path_tail(cursor, part, limit)
                if part_fragments:
                    fragments.update(part_fragments)
                else:
                    vector_query.append(part)

        fragments: List[Fragment] = list(fragments)

        instruction = doc_types.TextDocType.query_instruction
        for fragment in fragments:
            doc_type_cls = doc_types.detect_by_extension(fragment.path)
            if doc_type_cls is not None:
                instruction = doc_type_cls.query_instruction
                break

        if not vector_query:
            fragments.sort(key=lambda f: (f.path, f.lineno))
            hits = [Hit(score=1.0, **fragment.__dict__) for fragment in fragments]
            return hits

        vector_query = ' '.join(vector_query)
        embedding = await EMBEDDER_CLIENT.embed_query(instruction, vector_query, timeout=20.0)

        uuid_filter = [fragment.uuid for fragment in fragments]
        results = await self.collection.search(embedding, limit=limit, uuid_filter=uuid_filter)

        result_map = {result.uuid: result.score for result in results}

        if uuid_filter:
            fragments: List[Fragment] = [fragment for fragment in fragments if fragment.uuid in result_map]

            hits: List[Hit] = [
                Hit(score=result_map[fragment.uuid], **fragment.__dict__)
                for fragment in fragments
            ]
        else:
            uuids = [result.uuid for result in results]
            with self.cursor() as cursor:
                fragments: Dict[str, Fragment] = {f.uuid: f for f in self.list_fragments_by_uuid(cursor, uuids)}

            hits: List[Hit] = [
                Hit(score=result.score, **fragments[result.uuid].__dict__)
                for result in results if result.uuid in fragments
            ]

        hits.sort(key=lambda hit: (-hit.score, hit.path, hit.lineno))
        return hits
