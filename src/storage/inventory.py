import os.path
import time
from contextlib import asynccontextmanager
from typing import Optional, Tuple, List, AsyncContextManager

from asyncpg import Connection

from storage.database import Database


class Inventory:

    def __init__(self, db: Database) -> None:
        self.db = db

    async def find_project(self, url: str, checksum: str = '') -> Optional[str]:
        async with self.db.connection() as conn:
            if checksum:
                for row in conn.execute('SELECT project_id FROM Inventory WHERE url = ? AND checksum = ?', (url, checksum)):
                    return row[0]
            else:
                for row in conn.execute('SELECT project_id FROM Inventory WHERE url = ? AND extracted != 2 ORDER BY registered DESC LIMIT 1', (url,)):
                    return row[0]
            return None

    async def register_project(self, project_id: str, url: str, checksum: str):
        async with self.db.connection() as conn:
            now = int(time.time())
            conn.execute('INSERT INTO Inventory(project_id, url, checksum, registered, last_used) VALUES (?, ?, ?, ?, ?)', (project_id, url, checksum, now, now))

    async def reprocess_project(self, project_id: str):
        async with self.db.connection() as conn:
            conn.execute('UPDATE Inventory SET extracted=0, embedded=0 WHERE project_id=?', (project_id,))

    async def delete_project(self, project_id: str):
        async with self.db.connection() as conn:
            conn.execute('DELETE FROM Inventory WHERE project_id=?', (project_id,))

    async def get_next_project_to_extract(self) -> Optional[str]:
        async with self.db.connection() as conn:
            for project_id, registered in conn.execute('SELECT project_id, registered FROM Inventory WHERE extracted = 0 ORDER BY registered DESC LIMIT 1'):
                wait_time = int(time.time()) - registered
                print(f'Project {project_id} extract queue duration: {wait_time}s')
                return project_id
        return None

    async def mark_project_extracted(self, project_id: str):
        async with self.db.connection() as conn:
            conn.execute('UPDATE Inventory SET extracted = 1 WHERE project_id = ?', (project_id,))

    async def mark_project_cleaned(self, project_id: str):
        async with self.db.connection() as conn:
            conn.execute('UPDATE Inventory SET extracted = 2 WHERE project_id = ?', (project_id,))

    async def touch_project(self, project_id: str):
        now = int(time.time())
        async with self.db.connection() as conn:
            conn.execute('UPDATE Inventory SET last_used = ? WHERE project_id = ?', (project_id, now))

    def has_project_extracted(self, project_id: str) -> bool:
        async with self.db.connection() as conn:
            for row in conn.execute('SELECT extracted FROM Inventory WHERE project_id = ?', (project_id,)):
                return bool(row[0])

    async def get_next_project_to_embed(self) -> Optional[str]:
        async with self.db.connection() as conn:
            for project_id, registered in conn.execute('SELECT project_id, registered FROM Inventory WHERE extracted = 1 AND embedded = 0 ORDER BY registered LIMIT 1'):
                wait_time = int(time.time()) - registered
                print(f'Project {project_id} embed queue duration: {wait_time}s')
                return project_id
        return None

    async def mark_project_embedded(self, project_id: str):
        async with self.db.connection() as conn:
            conn.execute('UPDATE Inventory SET embedded = 1 WHERE project_id = ?', (project_id,))

    async def has_project_embedded(self, project_id: str) -> bool:
        async with self.db.connection() as conn:
            for row in conn.execute('SELECT embedded FROM Inventory WHERE project_id = ?', (project_id,)):
                return bool(row[0])
            return False

    async def get_expired_projects(self, cutoff: int, limit: int) -> List[Tuple[str, str]]:
        async with self.db.connection() as conn:
            projects = [tuple(row) for row in conn.execute('SELECT project_id, url FROM Inventory WHERE extracted < 2 AND last_used < ? ORDER BY registered LIMIT ?', (cutoff, limit))]
        return projects

    async def get_project_url(self, project_id: str) -> str:
        async with self.db.connection() as conn:
            for row in conn.execute('SELECT url FROM Inventory WHERE project_id = ?', (project_id,)):
                return row[0]
            return ''

    async def get_archive_checksum(self, project_id: str) -> str:
        async with self.db.connection() as conn:
            for row in conn.execute('SELECT checksum FROM Inventory WHERE project_id = ?', (project_id,)):
                return row[0]
            return ''
