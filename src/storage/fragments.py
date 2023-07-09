from dataclasses import dataclass
from typing import Optional, List, Tuple, Iterable

from asyncpg import Record, Connection

from common.constants import C
from common.tools import tiktoken_len


@dataclass
class Fragment:
    document_cs: str = ''
    id: int = -1
    lineno: int = 1
    tokens: int = 0
    depth: int = 0
    parent_id: Optional[int] = None
    category: str = 'text'
    summary: bool = False
    name: str = ''
    body: str = ''

    @classmethod
    def from_row(cls, row: Record) -> "Fragment":
        return cls(
            document_cs=row['document_cs'],
            id=row['id'],
            lineno=row['lineno'],
            tokens=row['tokens'],
            depth=row['depth'],
            parent_id=row['parent_id'],
            category=row['category'],
            summary=row['summary'],
            name=row['name'],
            body=row['body'],
        )


async def truncate(conn: Connection):
    if not C.DEVELOPMENT:
        raise RuntimeError('Refusing to truncate table if not in development')
    await conn.execute('TRUNCATE fragment')


async def create(conn: Connection, document_cs: str, lineno: int, depth: int, parent_id: Optional[int], category: str, summary: bool, name: str, body: str) -> Fragment:
    partition_key = document_cs[:2]
    tokens = tiktoken_len(body)

    id = await conn.fetchval(
        '''INSERT INTO fragment (partition_key, document_cs, lineno, tokens, depth, parent_id, category, summary, name, body) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10) RETURNING id''',
        partition_key, document_cs, lineno, tokens, depth, parent_id, category, summary, name, body
    )

    return Fragment(document_cs, id, lineno, tokens, depth, parent_id, category, summary, name, body)


async def query(conn: Connection, document_cs: str, id: int) -> List[Fragment]:
    return [
        Fragment.from_row(row)
        for row in await conn.fetch(
            '''SELECT * FROM fragment WHERE partition_key = $1 AND document_cs = $2 AND id = $3''',
            document_cs[:2], document_cs, id
        )
    ]


async def insert(conn: Connection, fragment: Fragment):
    fragment.id = await conn.fetchval(
        '''
        INSERT INTO fragment (partition_key, document_cs, lineno, tokens, depth, parent_id, category, summary, name, body) 
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
        RETURNING id
        ''',
        fragment.document_cs[:2],
        fragment.document_cs,
        fragment.lineno,
        fragment.tokens,
        fragment.depth,
        fragment.parent_id,
        fragment.category,
        fragment.summary,
        fragment.name[:160],
        fragment.body
    )


# See: https://stackoverflow.com/questions/43739123/best-way-to-insert-multiple-rows-with-asyncpg
async def insert_many(conn: Connection, fragments: Iterable[Fragment]):
    await conn.executemany(
        '''
        INSERT INTO fragment (partition_key, document_cs, lineno, tokens, depth, parent_id, category, summary, name, body) 
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
        ''',
        [
            (
                fragment.document_cs[:2],
                fragment.document_cs,
                fragment.lineno,
                fragment.tokens,
                fragment.depth,
                fragment.parent_id,
                fragment.category,
                fragment.summary,
                fragment.name[:160],
                fragment.body
            )
            for fragment in fragments
        ]
    )


async def get_all_fragments_in_project(conn: Connection, project_id: int) -> List[Fragment]:
    return [
        Fragment.from_row(row) for row in await conn.fetch('''
            SELECT c.* 
            FROM file AS f
            INNER JOIN fragment AS c ON c.partition_key = left(f.document_cs, 2) AND c.document_cs = f.document_cs
            WHERE f.project_id = $1 
            ORDER BY f.depth, f.path, c.lineno, c.id, c.category, c.summary
        ''', project_id)
    ]


async def search_in_project_by_path_tail_name(conn: Connection, project_id: int, path: str, tail: str, name: str, limit: int = 1) -> List[Tuple[str, Fragment]]:
    if name:
        order_by = 'LENGTH(c.name), f.depth, f.path, c.lineno, c.depth, c.category, c.summary, c.id'
    else:
        order_by = 'f.depth, f.path, c.lineno, c.depth, c.category, c.summary, c.id'

    return [
        (row['path'], Fragment.from_row(row))
        for row in await conn.fetch(f'''
            SELECT f.path, c.* 
            FROM file AS f
            INNER JOIN fragment AS c ON c.partition_key = left(f.document_cs, 2) AND c.document_cs = f.document_cs
            WHERE f.project_id = $1 
              AND f.path ILIKE $2 
              AND f.path ILIKE $3
              AND c.name ILIKE $4
            ORDER BY {order_by}
            LIMIT $5
        ''', project_id, f'{path}%', f'%{tail}', f'%{name}', limit)
    ]


async def search_in_project_by_path_tail_name_unlimited(conn: Connection, project_id: int, path: str, tail: str, name: str) -> List[Tuple[str, Fragment]]:
    if name:
        order_by = 'LENGTH(c.name), f.depth, f.path, c.lineno, c.depth, c.category, c.summary, c.id'
    else:
        order_by = 'f.depth, f.path, c.lineno, c.depth, c.category, c.summary, c.id'

    return [
        (row['path'], Fragment.from_row(row))
        for row in await conn.fetch(f'''
            SELECT f.path, c.* 
            FROM file AS f
            INNER JOIN fragment AS c ON c.partition_key = left(f.document_cs, 2) AND c.document_cs = f.document_cs
            WHERE f.project_id = $1 
              AND f.path ILIKE $2
              AND f.path ILIKE $3
              AND c.name ILIKE $4
            ORDER BY {order_by}
        ''', project_id, f'{path}%', f'%{tail}', f'%{name}')
    ]


async def list_project_fragments_by_id(conn: Connection, project_id: int, ids: List[int]) -> List[Tuple[str, Fragment]]:
    if not ids:
        return []

    placeholders = ','.join(f'${2 + i}' for i in range(len(ids)))
    fragments = [
        (row['path'], Fragment.from_row(row))
        for row in await conn.fetch(f'''
            SELECT f.path, c.* 
            FROM file AS f
            INNER JOIN fragment AS c ON c.partition_key = left(f.document_cs, 2) AND c.document_cs = f.document_cs
            WHERE f.project_id = $1
              AND f.id IN ({placeholders})
        ''', project_id, *ids)
    ]
    return fragments


async def list_all_fragments(conn: Connection) -> List[Fragment]:
    fragments = [
        Fragment.from_row(row)
        for row in await conn.fetch(f'''SELECT * FROM fragment ORDER BY id''')
    ]
    return fragments


def delete_by_document_cs(conn: Connection, checksum):
    conn.execute('''
        DELETE FROM fragment 
        WHERE partition_key = $1 
          AND document_cs = $2
    ''', checksum[:2], checksum)


async def count(conn: Connection) -> int:
    return await conn.fetchval('SELECT COUNT(*) FROM fragment')
