from dataclasses import dataclass
from typing import List

from asyncpg import Record, Connection

from common.constants import C


@dataclass
class Usage:
    project_id: int
    definition_file_id: int
    definition_start: int
    usage_file_id: int
    usage_start: int

    @classmethod
    def from_row(cls, row: Record) -> "Usage":
        return cls(
            project_id=row['project_id'],
            definition_file_id=row['definition_file_id'],
            definition_start=row['definition_start'],
            usage_file_id=row['usage_file_id'],
            usage_start=row['usage_start'],
        )


async def truncate(conn: Connection):
    if not C.DEVELOPMENT:
        raise RuntimeError('Refusing to truncate table if not in development')
    await conn.execute('TRUNCATE usage')


async def create(conn: Connection, project_id: int, definition_file_id: int, definition_start: int, usage_file_id: int, usage_start: int) -> Usage:
    partition_key = f'{project_id % 100:02d}'
    await conn.execute(
        '''INSERT INTO usage (partition_key, project_id, definition_file_id, definition_start, usage_file_id, usage_start) VALUES ($1, $2, $3, $4, $5, $6)''',
        partition_key, project_id, definition_file_id, definition_start, usage_file_id, usage_start
    )
    return Usage(project_id, definition_file_id, definition_start, usage_file_id, usage_start)


async def find_usages(conn: Connection, project_id: int, definition_file_id: int, definition_start: int) -> List[Usage]:
    return [
        Usage.from_row(row)
        for row in await conn.fetch(
            '''SELECT * FROM usage WHERE project_id = $1 AND definition_file_id = $2 AND definition_start = $3''',
            project_id, definition_file_id, definition_start
        )
    ]


async def find_definitions(conn: Connection, project_id: int, usage_file_id: int, usage_start: int) -> List[Usage]:
    return [
        Usage.from_row(row)
        for row in await conn.fetch(
            '''SELECT * FROM usage WHERE project_id = $1 AND usage_file_id = $2 AND usage_start = $3''',
            project_id, usage_file_id, usage_start
        )
    ]
