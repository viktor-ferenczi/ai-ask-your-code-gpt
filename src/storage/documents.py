import hashlib
from dataclasses import dataclass
from typing import Optional

from asyncpg import Record, Connection

from common.constants import C


@dataclass
class Document:
    checksum: str
    body: bytes
    doctype: str

    @classmethod
    def from_row(cls, row: Record) -> "Document":
        return cls(
            checksum=row['checksum'],
            body=row['body'],
            doctype=row['doctype'],
        )


async def truncate(conn: Connection):
    if not C.DEVELOPMENT:
        raise RuntimeError('Refusing to truncate table if not in development')
    await conn.execute('TRUNCATE document')


async def create(conn: Connection, checksum: str, body: bytes, doctype: str) -> Document:
    partition_key = checksum[:2]

    await conn.execute(
        '''INSERT INTO document (partition_key, checksum, body, doctype) VALUES ($1, $2, $3, $4)''',
        partition_key, checksum, body, doctype
    )

    return Document(checksum, body, doctype)


async def find_by_checksum(conn: Connection, checksum: str) -> Optional[Document]:
    row = await conn.fetchrow('''SELECT * FROM document WHERE partition_key = $1 AND checksum = $2 LIMIT 1''', checksum[:2], checksum)
    if row is None:
        return None
    return Document.from_row(row)
