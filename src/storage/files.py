from dataclasses import dataclass
from typing import Optional

from asyncpg import Record, Connection

from common.constants import C


@dataclass
class File:
    id: int
    project_id: int
    path_in_project: str
    mime_type: str
    size: int
    document_hash: str
    archive_hash: str

    @classmethod
    def from_row(cls, row: Record) -> "File":
        return cls(
            id=row['id'],
            project_id=row['project_id'],
            path_in_project=row['path_in_project'],
            mime_type=row['mime_type'],
            size=row['size'],
            document_hash=row['document_hash'],
            archive_hash=row['archive_hash'],
        )


async def truncate(conn: Connection):
    if not C.DEVELOPMENT:
        raise RuntimeError('Refusing to truncate table if not in development')
    await conn.execute('TRUNCATE file')


async def create(conn: Connection, project_id: int, path_in_project: str, mime_type: str, size: int, document_hash: Optional[str], archive_hash: Optional[str]) -> File:
    id = await conn.fetchval(
        '''INSERT INTO file (project_id, path_in_project, mime_type, size, document_hash, archive_hash) VALUES ($1, $2, $3, $4, $5, $6) RETURNING id''',
        project_id, path_in_project, mime_type, size, document_hash, archive_hash
    )
    return File(id, project_id, path_in_project, mime_type, size, document_hash, archive_hash)


async def find(conn: Connection, id: int) -> Optional[File]:
    row = await conn.fetchrow('''SELECT * FROM file WHERE id = $1''', id)
    if row is None:
        return None
    return File.from_row(row)
