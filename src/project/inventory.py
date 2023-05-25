import os.path
import sqlite3
import time
from contextlib import contextmanager
from typing import Optional, ContextManager

from common.constants import C
from common.marker import Marker


class Inventory:

    def __init__(self) -> None:
        os.makedirs(C.DATA_DIR, exist_ok=True)
        self.db_path = os.path.join(C.DATA_DIR, 'inventory.sqlite')
        self.notify_project_registered = Marker(os.path.join(C.DATA_DIR, 'project-registered.notify'))
        self.notify_project_deleted = Marker(os.path.join(C.DATA_DIR, 'project-deleted.notify'))

    @contextmanager
    def cursor(self) -> ContextManager[sqlite3.Cursor]:
        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cursor:
                yield cursor

    def create_database(self):
        if os.path.exists(self.db_path):
            return

        self.drop_database()

        with self.cursor() as cursor:
            cursor.execute('''
                    CREATE TABLE Inventory(
                        project_id TEXT PRIMARY KEY,
                        registered INTEGER NOT NULL,
                        last_used INTEGER NOT NULL,
                        extracted INTEGER DEFAULT 0 NOT NULL,
                        embedded INTEGER DEFAULT 0 NOT NULL
                    )
                ''')
            cursor.execute('CREATE INDEX idx_inventory_project_id ON Inventory(project_id)')

    def register_project(self, project_id: str):
        with self.cursor() as cursor:
            now = int(time.time())
            cursor.execute('INSERT OR REPLACE INTO Inventory(project_id, registered, last_used) VALUES (?, ?, ?, ?)', (project_id, now, now))

        self.notify_project_registered.mark()

    def delete_project(self, project_id: str):
        with self.cursor() as cursor:
            cursor.execute('DELETE FROM Inventory WHERE project_id=?', (project_id,))

        self.notify_project_deleted.mark()

    def get_next_project_to_extract(self) -> Optional[str]:
        with self.cursor() as cursor:
            for project_id, registered in cursor.execute('SELECT project_id, registered FROM Inventory WHERE extracted = 0 ORDER BY registered LIMIT 1'):
                wait_time = int(time.time()) - registered
                print(f'Project {project_id} extract queue duration: {wait_time}s')
                return project_id
        return None

    def mark_project_as_extracted(self, project_id: str):
        with self.cursor() as cursor:
            cursor.execute('UPDATE Project SET extracted = 1 WHERE project_id = ?', (project_id,))

    def get_next_project_to_embed(self) -> Optional[str]:
        with self.cursor() as cursor:
            for project_id, registered in cursor.execute('SELECT project_id, registered FROM Inventory WHERE extracted = 1 AND embedded = 0 ORDER BY registered LIMIT 1'):
                wait_time = int(time.time()) - registered
                print(f'Project {project_id} embed queue duration: {wait_time}s')
                return project_id
        return None

    def mark_project_as_embedded(self, project_id: str):
        with self.cursor() as cursor:
            cursor.execute('UPDATE Project SET embedded = 1 WHERE project_id = ?', (project_id,))

    def get_expired_projects(self, cutoff: int, limit: int) -> Optional[str]:
        with self.cursor() as cursor:
            for project_id, registered in cursor.execute('SELECT project_id, registered FROM Inventory WHERE last_used < ? ORDER BY registered LIMIT ?', (cutoff, limit)):
                wait_time = int(time.time()) - registered
                print(f'Project {project_id} loading queue duration: {wait_time}s')
                return project_id
        return None

    def drop_database(self):
        if os.path.isfile(self.db_path):
            os.remove(self.db_path)

        self.notify_project_registered.clear()
        self.notify_project_deleted.clear()
