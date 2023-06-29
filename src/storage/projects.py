from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from asyncpg import Record, Connection


@dataclass
class Project:
    id: int
    uid: str
    name: str
    created: datetime
    accessed: datetime

    @classmethod
    def from_row(cls, row: Record) -> "Project":
        return cls(
            id=row['id'],
            uid=row['uid'],
            name=row['name'],
            created=row['created'],
            accessed=row['accessed'],
        )


async def create(conn: Connection, uid: str, name: str) -> Project:
    row = await conn.fetchrow(
        '''
        INSERT INTO project (uid, name) VALUES (?, ?) 
        RETURNING id, created
        ''',
        (uid, name)
    )
    id = row['id']
    created = row['created']
    return Project(id, uid, name, created, created)


async def find(conn: Connection, id: int) -> Optional[Project]:
    row = await conn.fetchrow('''SELECT * FROM project WHERE id = ?''', id)
    if row is None:
        return None
    return Project.from_row(row)
