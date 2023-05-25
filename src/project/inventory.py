import os.path
import sqlite3
from datetime import datetime

from common.constants import C


class Inventory:

    def __init__(self) -> None:
        os.makedirs(C.DATA_DIR, exist_ok=True)
        self.db_path = os.path.join(C.DATA_DIR, 'inventory.sqlite')

    def create_database(self):
        if os.path.exists(self.db_path):
            return

        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cur:
                cur.execute('''
                    CREATE TABLE Inventory(
                        project_id TEXT PRIMARY KEY,
                        registered TEXT NOT NULL,
                        loaded INTEGER DEFAULT 0 NOT NULL
                    )
                ''')
                cur.execute('CREATE INDEX idx_inventory_project_id ON Inventory(project_id)')

    def register_project(self, project_id: str):
        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cur:
                now = datetime.utcnow().replace(microsecond=0).isoformat()
                cur.execute('INSERT OR REPLACE INTO Inventory(project_id, loaded) VALUES (?, ?, 0)', (project_id, now))

    def delete_project(self, project_id: str):
        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cur:
                cur.execute('DELETE FROM Inventory WHERE project_id=?', (project_id,))

    def find_projects_to_be_loaded(self) -> List[str]:
        with sqlite3.connect(self.db_path) as db:
            with db.cursor() as cur:
                return [row['uuid'] for row in cur.execute('SELECT project_id FROM Inventory WHERE loaded=0 ORDER BY registered')]

    def delete_database(self):
        if os.path.isfile(self.db_path):
            os.remove(self.db_path)
