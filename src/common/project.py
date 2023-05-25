import os
import shutil
import sqlite3
import time
from pathlib import Path
from typing import List

from common.constants import C
from model.fragment import Fragment


class Project:

    def __init__(self, project_id: str) -> None:
        self.project_id: str = project_id

        self.data_dir: str = os.path.join(C.PROJECTS_DIR, self.project_id[:2], self.project_id[2:4], self.project_id)
        os.makedirs(self.data_dir, exist_ok=True)

        self.archive_path: str = os.path.join(self.data_dir, 'archive.zip')
        self.db_path: str = os.path.join(self.data_dir, 'fragment.db')
        self.done_marker_path: str = os.path.join(self.data_dir, 'done')
        self.used_marker_path: str = os.path.join(self.data_dir, 'used')

    def create_database(self):
        if os.path.exists(self.db_path):
            return

        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cur:
                cur.execute('''
                    CREATE TABLE Fragment(
                        uuid TEXT PRIMARY KEY,
                        path TEXT NOT NULL,
                        lineno INTEGER NOT NULL,
                        text TEXT NOT NULL,
                        name TEXT,
                        embedded INTEGER DEFAULT 0
                    )
                ''')

    def index_by_path(self):
        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cur:
                cur.execute('CREATE INDEX idx_fragment_path ON Fragment(path)')

    def insert_fragment(self, fragment: Fragment):
        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cur:
                cur.execute('INSERT INTO Fragment(uuid, path, lineno, text, name) VALUES (?, ?, ?, ?, ?)',
                            (fragment.uuid, fragment.path, fragment.lineno, fragment.text, fragment.name))

    def mark_fragments_embedded(self, uuids: List[str]):
        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cur:
                cur.execute('UPDATE Fragment SET embedded=1 WHERE uuid IN ?', (uuids,))

    def get_uuids_of_fragments_to_embed(self) -> List[str]:
        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cur:
                return [row['uuid'] for row in cur.execute('SELECT uuid FROM Fragment WHERE embedded=0')]

    def get_fragments_by_path(self, paths: List[str]) -> List[str]:
        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cur:
                return [row['uuid'] for row in cur.execute('SELECT uuid FROM Fragment WHERE path IN (?)', (paths,))]

    def get_fragments_by_path_tail(self, path: str) -> List[str]:
        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cur:
                return [row['uuid'] for row in cur.execute('SELECT uuid FROM Fragment WHERE path LIKE (?)', (f'%{path}',))]

    def touch(self):
        Path(self.used_marker_path).touch()

    @property
    def age(self) -> float:
        return max(0.0, time.time() - os.stat(self.used_marker_path).st_mtime)

    @property
    def done(self) -> bool:
        return os.path.isfile(self.done_marker_path)

    def mark_as_done(self):
        with open(self.done_marker_path, 'wb'):
            pass

    def delete(self):
        if os.path.isdir(self.data_dir):
            shutil.rmtree(self.data_dir)
