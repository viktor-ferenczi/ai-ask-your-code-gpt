from dataclasses import dataclass
from typing import List

from asyncpg import Record, Connection

from common.constants import C


@dataclass
class Usage:
    project_id: int
    definition_file_id: int
    definition_fragment_id: int
    usage_file_id: int
    usage_fragment_id: int

    @classmethod
    def from_row(cls, row: Record) -> "Usage":
        return cls(
            project_id=row['project_id'],
            definition_file_id=row['definition_file_id'],
            definition_fragment_id=row['definition_fragment_id'],
            usage_file_id=row['usage_file_id'],
            usage_fragment_id=row['usage_fragment_id'],
        )


async def truncate(conn: Connection):
    if not C.DEVELOPMENT:
        raise RuntimeError('Refusing to truncate table if not in development')
    await conn.execute('TRUNCATE usage')


async def create(conn: Connection, project_id: int, definition_file_id: int, definition_fragment_id: int, usage_file_id: int, usage_fragment_id: int) -> Usage:
    partition_key = f'{project_id % 100:02d}'
    await conn.execute(
        '''INSERT INTO usage (partition_key, project_id, definition_file_id, definition_fragment_id, usage_file_id, usage_fragment_id) VALUES ($1, $2, $3, $4, $5, $6)''',
        partition_key, project_id, definition_file_id, definition_fragment_id, usage_file_id, usage_fragment_id
    )
    return Usage(project_id, definition_file_id, definition_fragment_id, usage_file_id, usage_fragment_id)


async def find_usages(conn: Connection, project_id: int, definition_file_id: int, definition_fragment_id: int) -> List[Usage]:
    return [
        Usage.from_row(row)
        for row in await conn.fetch(
            '''SELECT * FROM usage WHERE project_id = $1 AND definition_file_id = $2 AND definition_fragment_id = $3''',
            project_id, definition_file_id, definition_fragment_id
        )
    ]


async def find_definitions(conn: Connection, project_id: int, usage_file_id: int, usage_fragment_id: int) -> List[Usage]:
    return [
        Usage.from_row(row)
        for row in await conn.fetch(
            '''SELECT * FROM usage WHERE project_id = $1 AND usage_file_id = $2 AND usage_fragment_id = $3''',
            project_id, usage_file_id, usage_fragment_id
        )
    ]
