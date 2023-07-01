import hashlib
from dataclasses import dataclass
from typing import Optional

from asyncpg import Record, Connection

from common.constants import C


@dataclass
class Document:
    checksum: str
    doc_type: str
    mime_type: str
    size: int
    body: bytes

    @classmethod
    def from_row(cls, row: Record) -> "Document":
        return cls(
            checksum=row['checksum'],
            doc_type=row['doc_type'],
            mime_type=row['mime_type'],
            size=row['size'],
            body=row['body'],
        )


async def truncate(conn: Connection):
    if not C.DEVELOPMENT:
        raise RuntimeError('Refusing to truncate table if not in development')
    await conn.execute('TRUNCATE document')


async def create(conn: Connection, checksum: str, doc_type: str, mime_type: str, body: bytes) -> Document:
    assert len(doc_type) <= 40
    assert len(mime_type) <= 96

    partition_key = checksum[:2]
    size = len(body)

    await conn.execute(
        '''INSERT INTO document (partition_key, checksum, doc_type, mime_type, size, body) VALUES ($1, $2, $3, $4, $5, $6)''',
        partition_key, checksum, doc_type[:40], mime_type[:96], size, body
    )

    return Document(checksum, doc_type, mime_type, size, body)


async def find_by_checksum(conn: Connection, checksum: str) -> Optional[Document]:
    row = await conn.fetchrow('''SELECT * FROM document WHERE partition_key = $1 AND checksum = $2 LIMIT 1''', checksum[:2], checksum)
    if row is None:
        return None
    return Document.from_row(row)
