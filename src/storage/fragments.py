from dataclasses import dataclass
from typing import Optional, List, Tuple

from asyncpg import Record, Connection

from common.constants import C
from common.tools import tiktoken_len


@dataclass
class Fragment:
    document_cs: str = ''
    id: int = ''
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
            id=row['id'],
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


async def create(conn: Connection, document_cs: str, lineno: int, depth: int, parent_id: Optional[int], category: str, definition: bool, summary: bool, name: str, body: str) -> Fragment:
    partition_key = document_cs[:2]
    tokens = tiktoken_len(body)

    id = await conn.fetchval(
        '''INSERT INTO fragment (partition_key, document_cs, lineno, tokens, depth, parent_id, category, definition, summary, name, body) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11) RETURNING id''',
        partition_key, document_cs, lineno, tokens, depth, parent_id, category, definition, summary, name, body
    )

    return Fragment(document_cs, id, lineno, tokens, depth, parent_id, category, definition, summary, name, body)


async def query(conn: Connection, document_cs: str, id: int) -> List[Fragment]:
    return [
        Fragment.from_row(row)
        for row in await conn.fetch(
            '''SELECT * FROM fragment WHERE partition_key = $1 AND document_cs = $2 AND id= $3''',
            document_cs[:2], document_cs, id
        )
    ]


async def insert(conn: Connection, fragment: Fragment):
    fragment.id = await conn.fetchval(
        '''
        INSERT INTO fragment (partition_key, document_cs, lineno, tokens, depth, parent_id, category, definition, summary, name, body) 
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)
        RETURNING id
        ''',
        fragment.document_cs[:2],
        fragment.document_cs,
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


async def get_all_fragments(conn: Connection, project_id: int) -> List[Fragment]:
    return [
        Fragment.from_row(row) for row in await conn.fetch('''
            SELECT f.* 
            FROM fragment AS f
            INNER JOIN file AS e ON e.document_cs = f.document_cs AND e.project_id = $1
            ORDER BY f.document_cs, f.lineno, f.category, f.definition, f.summary
        ''', project_id)
    ]


async def search_by_path_tail_name(conn: Connection, project_id: int, path: str, tail: str, name: str, limit: int = 1) -> List[Tuple[str, Fragment]]:
    return [
        (row['path'], Fragment.from_row(row))
        for row in await conn.fetch('''
            SELECT e.path, f.* 
            FROM fragment AS f
            INNER JOIN file AS e ON e.document_cs = f.document_cs AND e.project_id = $1
            WHERE e.path ILIKE $2 
              AND e.path ILIKE $3
              AND f.name ILIKE $4
            ORDER BY LENGTH(name), e.path, lineno 
            LIMIT $5
        ''', project_id, f'{path}%', f'%{tail}', f'%{name}', limit)
    ]


async def search_by_path_tail_name_unlimited(conn: Connection, project_id: int, path: str, tail: str, name: str) -> List[Tuple[str, Fragment]]:
    return [
        (row['path'], Fragment.from_row(row))
        for row in await conn.fetch('''
            SELECT e.path, f.* 
            FROM fragment AS f
            INNER JOIN file AS e ON e.document_cs = f.document_cs AND e.project_id = $1
            WHERE e.path ILIKE $2
              AND e.path ILIKE $3
              AND f.name ILIKE $4
            ORDER BY LENGTH(name), e.path, lineno
        ''', project_id, f'{path}%', f'%{tail}', f'%{name}')
    ]


async def list_fragments_by_id(conn: Connection, project_id: int, ids: List[int]) -> List[Tuple[str, Fragment]]:
    if not ids:
        return []

    placeholders = ','.join(f'${1 + i}' for i in range(len(ids)))
    fragments = [
        (row['path'], Fragment.from_row(row))
        for row in await conn.fetch(f'''
            SELECT e.path, f.* 
            FROM fragment AS f
            INNER JOIN file AS e ON e.document_cs = f.document_cs AND e.project_id = $1
            WHERE id IN ({placeholders})
        ''', *ids)
    ]
    return fragments
