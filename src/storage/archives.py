import os
from dataclasses import dataclass
from typing import Optional

from asyncpg import Record, Connection

from common.tools import hash_file


@dataclass
class Archive:
    hash: str
    path: str
    size: int
    url: str
    etag: Optional[str]

    @classmethod
    def from_row(cls, row: Record) -> "Archive":
        return cls(
            hash=row['hash'],
            path=row['path'],
            size=row['size'],
            url=row['url'],
            etag=row['etag'],
        )


async def create(conn: Connection, path: str, url: str, etag: Optional[str] = None) -> Archive:
    hash = hash_file(path)
    size = os.stat(path).st_size
    await conn.execute(
        '''INSERT INTO archive (hash, path, size, url, etag) VALUES (?, ?, ?, ?, ?)''',
        (hash, path, size, url, etag)
    )
    return Archive(hash, path, size, url, etag)


async def find_by_hash(conn: Connection, hash: str) -> Optional[Archive]:
    for row in await conn.fetch('''SELECT * FROM archive WHERE hash = ? LIMIT 1''', hash):
        return Archive.from_row(row)


async def find_by_url(conn: Connection, url: str) -> Optional[Archive]:
    row = await conn.fetchrow('''SELECT * FROM archive WHERE url = ? LIMIT 1''', url)
    if row is None:
        return None
    return Archive.from_row(row)
