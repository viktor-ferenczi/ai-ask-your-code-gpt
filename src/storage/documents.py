import hashlib
from dataclasses import dataclass
from typing import Optional

from asyncpg import Record, Connection

from common.constants import C


@dataclass
class Document:
    hash: str
    body: str
    length: int
    doctype: str

    @classmethod
    def from_row(cls, row: Record) -> "Document":
        return cls(
            hash=row['hash'],
            body=row['body'],
            length=row['length'],
            doctype=row['doctype'],
        )


async def truncate(conn: Connection):
    if not C.DEVELOPMENT:
        raise RuntimeError('Refusing to truncate table if not in development')
    await conn.execute('TRUNCATE document')


async def create(conn: Connection, body: str, doctype: str) -> Document:
    sha = hashlib.sha256()
    sha.update(body.encode('utf-8'))
    hash = sha.hexdigest()

    partition_key = hash[:2]
    length = len(body)

    await conn.execute(
        '''INSERT INTO document (partition_key, hash, body, length, doctype) VALUES ($1, $2, $3, $4, $5)''',
        partition_key, hash, body, length, doctype
    )

    return Document(hash, body, length, doctype)


async def find(conn: Connection, hash: str) -> Optional[Document]:
    row = await conn.fetchrow('''SELECT * FROM document WHERE partition_key = $1 AND hash = $2 LIMIT 1''', hash[:2], hash)
    if row is None:
        return None
    return Document.from_row(row)
