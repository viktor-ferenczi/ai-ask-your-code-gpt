from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from asyncpg import Record, Connection

from common.constants import C


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


async def truncate(conn: Connection):
    if not C.DEVELOPMENT:
        raise RuntimeError('Refusing to truncate table if not in development')
    await conn.execute('TRUNCATE project')


async def create(conn: Connection, uid: str, name: str) -> Project:
    row = await conn.fetchrow(
        '''INSERT INTO project (uid, name) VALUES ($1, $2) RETURNING id, created''',
        uid, name
    )
    id = row['id']
    created = row['created']
    return Project(id, uid, name, created, created)


async def find(conn: Connection, id: int) -> Optional[Project]:
    row = await conn.fetchrow('''SELECT * FROM project WHERE id = $1''', id)
    if row is None:
        return None
    return Project.from_row(row)


async def find_by_uid_and_name(conn: Connection, uid: str, name: str) -> Optional[Project]:
    row = await conn.fetchrow('''
            SELECT * 
            FROM project 
            WHERE uid = $1 
              AND name = $2 
            LIMIT 1
        ''', uid, name)
    if row is None:
        return None
    return Project.from_row(row)


async def update_accessed(conn: Connection, id: int, accessed: datetime):
    await conn.execute('UPDATE project SET accessed = $2 WHERE id = $1', id, accessed)
