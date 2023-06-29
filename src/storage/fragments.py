from dataclasses import dataclass
from typing import Optional, AsyncIterator

from asyncpg import Record, Connection

from common.tools import tiktoken_len


@dataclass
class Fragment:
    document_hash: str = ''
    start: int = 0
    length: int = 0
    lineno: int = 1
    tokens: int = 0
    depth: int = 0
    parent_id: Optional[int] = None
    category: str = 'text'
    definition: bool = True
    summary: bool = False
    name: str = ''
    body: str = ''

    @classmethod
    def from_row(cls, row: Record) -> "Fragment":
        return cls(
            document_hash=row['document_hash'],
            start=row['start'],
            length=row['length'],
            lineno=row['lineno'],
            tokens=row['tokens'],
            depth=row['depth'],
            parent_id=row['parent_id'],
            category=row['category'],
            definition=row['definition'],
            summary=row['summary'],
            name=row['name'],
            body=row['body'],
        )


async def create(conn: Connection, document_hash: str, start: int, lineno: int, depth: int, parent_id: Optional[int], category: str, definition: bool, summary: bool, name: str, body: str) -> Fragment:
    partition_key = document_hash[:2]
    length = len(body)
    tokens = tiktoken_len(body)

    await conn.execute(
        '''INSERT INTO fragment (partition_key, document_hash, start, length, lineno, tokens, depth, parent_id, category, definition, summary, name, body) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (partition_key, document_hash, start, length, lineno, tokens, depth, parent_id, category, definition, summary, name, body)
    )

    return Fragment(document_hash, start, length, lineno, tokens, depth, parent_id, category, definition, summary, name, body)


async def query(conn: Connection, document_hash: str, start: int) -> AsyncIterator[Fragment]:
    for row in await conn.fetch('''SELECT * FROM fragment WHERE partition_key = ? AND document_hash = ? AND start = ?''', document_hash[:2], hash, start):
        yield Fragment.from_row(row)
