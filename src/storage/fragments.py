from dataclasses import dataclass
from typing import Optional, List

from asyncpg import Record, Connection

from common.constants import C
from common.tools import tiktoken_len


@dataclass
class Fragment:
    document_cs: str = ''
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
            document_cs=row['document_cs'],
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


async def truncate(conn: Connection):
    if not C.DEVELOPMENT:
        raise RuntimeError('Refusing to truncate table if not in development')
    await conn.execute('TRUNCATE fragment')


async def create(conn: Connection, document_cs: str, start: int, lineno: int, depth: int, parent_id: Optional[int], category: str, definition: bool, summary: bool, name: str, body: str) -> Fragment:
    partition_key = document_cs[:2]
    length = len(body)
    tokens = tiktoken_len(body)

    await conn.execute(
        '''INSERT INTO fragment (partition_key, document_cs, start, length, lineno, tokens, depth, parent_id, category, definition, summary, name, body) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13)''',
        partition_key, document_cs, start, length, lineno, tokens, depth, parent_id, category, definition, summary, name, body
    )

    return Fragment(document_cs, start, length, lineno, tokens, depth, parent_id, category, definition, summary, name, body)


async def query(conn: Connection, document_cs: str, start: int) -> List[Fragment]:
    return [
        Fragment.from_row(row)
        for row in await conn.fetch(
            '''SELECT * FROM fragment WHERE partition_key = $1 AND document_cs = $2 AND start = $3''',
            document_cs[:2], document_cs, start
        )
    ]


async def insert(conn: Connection, fragment: Fragment):
    await conn.execute(
        '''
        INSERT INTO fragment (partition_key, document_cs, start, length, lineno, tokens, depth, parent_id, category, definition, summary, name, body) 
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13)
        ''',
        fragment.document_cs[:2],
        fragment.document_cs,
        fragment.start,
        fragment.length,
        fragment.lineno,
        fragment.tokens,
        fragment.depth,
        fragment.parent_id,
        fragment.category,
        fragment.definition,
        fragment.summary,
        fragment.name,
        fragment.body
    )
