from dataclasses import dataclass
from typing import Optional

from asyncpg import Record, Connection

from common.constants import C


@dataclass
class Archive:
    checksum: str
    path: str
    size: int
    url: str
    etag: str
    common_base_dir: str

    @classmethod
    def from_row(cls, row: Record) -> "Archive":
        return cls(
            checksum=row['checksum'],
            path=row['path'],
            size=row['size'],
            url=row['url'],
            etag=row['etag'],
            common_base_dir=row['common_base_dir'],
        )


async def truncate(conn: Connection):
    if not C.DEVELOPMENT:
        raise RuntimeError('Refusing to truncate table if not in development')
    await conn.execute('TRUNCATE archive')


async def create(conn: Connection, checksum: str, path: str, size: int, url: str, etag: str, common_base_dir: str) -> Archive:
    await conn.execute(
        '''INSERT INTO archive (checksum, path, size, url, etag, common_base_dir) VALUES ($1, $2, $3, $4, $5, $6)''',
        checksum, path, size, url, etag, common_base_dir
    )
    return Archive(checksum, path, size, url, etag, common_base_dir)


async def find_by_checksum(conn: Connection, checksum: str) -> Optional[Archive]:
    for row in await conn.fetch('''SELECT * FROM archive WHERE checksum = $1 LIMIT 1''', checksum):
        return Archive.from_row(row)


async def find_by_url(conn: Connection, url: str) -> Optional[Archive]:
    row = await conn.fetchrow('''SELECT * FROM archive WHERE url = $1 LIMIT 1''', url)
    if row is None:
        return None
    return Archive.from_row(row)
