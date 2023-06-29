import hashlib
from dataclasses import dataclass
from typing import Optional

from asyncpg import Record, Connection


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
            body=row['path'],
            length=row['url'],
            doctype=row['etag'],
        )


async def create(conn: Connection, body: str, doctype: str) -> Document:
    sha = hashlib.sha256()
    sha.update(body)
    hash = sha.hexdigest()

    partition_key = hash[:2]
    length = len(body)

    await conn.execute(
        '''INSERT INTO document (partition_key, hash, body, length, doctype) VALUES (?, ?, ?, ?, ?)''',
        (partition_key, hash, body, length, doctype)
    )

    return Document(hash, body, length, doctype)


async def find(conn: Connection, hash: str) -> Optional[Document]:
    row = await conn.fetchrow('''SELECT * FROM document WHERE partition_key = ? AND hash = ? LIMIT 1''', hash[:2], hash)
    if row is None:
        return None
    return Document.from_row(row)
