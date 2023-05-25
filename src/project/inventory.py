import os.path
import sqlite3
import time
from typing import Optional

from common.constants import C
from common.marker import Marker


class Inventory:

    def __init__(self) -> None:
        os.makedirs(C.DATA_DIR, exist_ok=True)
        self.db_path = os.path.join(C.DATA_DIR, 'inventory.sqlite')
        self.notify_project_registered = Marker(os.path.join(C.DATA_DIR, 'project-registered.notify'))
        self.notify_project_deleted = Marker(os.path.join(C.DATA_DIR, 'project-deleted.notify'))

    def create_database(self):
        if os.path.exists(self.db_path):
            return

        self.delete_database()

        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cur:
                cur.execute('''
                    CREATE TABLE Inventory(
                        project_id TEXT PRIMARY KEY,
                        registered INTEGER NOT NULL,
                        loaded INTEGER DEFAULT 0 NOT NULL
                    )
                ''')
                cur.execute('CREATE INDEX idx_inventory_project_id ON Inventory(project_id)')

    def register_project(self, project_id: str):
        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cur:
                cur.execute('INSERT OR REPLACE INTO Inventory(project_id, loaded) VALUES (?, ?, 0)', (project_id, int(time.time())))

        self.notify_project_registered.mark()

    def delete_project(self, project_id: str):
        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cur:
                cur.execute('DELETE FROM Inventory WHERE project_id=?', (project_id,))

        self.notify_project_deleted.mark()

    def get_next_project_to_load(self) -> Optional[str]:
        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cur:
                for project_id, registered in cur.execute('SELECT project_id, registered FROM Inventory WHERE loaded=0 ORDER BY registered LIMIT 1'):
                    wait_time = int(time.time()) - registered
                    print(f'Project {project_id} loading queue duration: {wait_time}s')
                    return project_id
        return None

    def delete_database(self):
        if os.path.isfile(self.db_path):
            os.remove(self.db_path)

        self.notify_project_registered.clear()
        self.notify_project_deleted.clear()
