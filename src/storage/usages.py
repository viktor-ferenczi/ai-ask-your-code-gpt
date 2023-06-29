from dataclasses import dataclass
from typing import AsyncIterator

from asyncpg import Record, Connection


@dataclass
class Usage:
    project_id: int
    definition_file_id: int
    usage_file_id: int
    definition_start: int
    usage_start: int

    @classmethod
    def from_row(cls, row: Record) -> "Usage":
        return cls(
            project_id=row['project_id'],
            definition_file_id=row['definition_file_id'],
            usage_file_id=row['usage_file_id'],
            definition_start=row['definition_start'],
            usage_start=row['usage_start'],
        )


async def create(conn: Connection, project_id: int, definition_file_id: int, usage_file_id: int, definition_start: int, usage_start: int) -> Usage:
    partition_key = f'{project_id % 100:02d}'
    await conn.fetchval(
        '''INSERT INTO usage (partition_key, project_id, definition_file_id, usage_file_id, definition_start, usage_start) VALUES (?, ?, ?, ?, ?, ?)''',
        (partition_key, project_id, definition_file_id, usage_file_id, definition_start, usage_start)
    )
    return Usage(project_id, definition_file_id, usage_file_id, definition_start, usage_start)


async def find_usages(conn: Connection, project_id: int, definition_file_id: int, definition_start: int) -> AsyncIterator[Usage]:
    for row in await conn.fetch('''SELECT * FROM usage WHERE project_id = ? AND definition_file_id = ? AND definition_start = ?''', project_id, definition_file_id, definition_start):
        yield Usage.from_row(row)


async def find_definitions(conn: Connection, project_id: int, usage_file_id: int, usage_start: int) -> AsyncIterator[Usage]:
    for row in await conn.fetch('''SELECT * FROM usage WHERE project_id = ? AND usage_file_id = ? AND usage_start = ?''', project_id, usage_file_id, usage_start):
        yield Usage.from_row(row)
