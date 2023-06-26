from contextlib import asynccontextmanager
from typing import AsyncContextManager

import asyncpg
from asyncpg import UndefinedTableError

from storage import schema
from storage import sql


class Database:
    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool

    @asynccontextmanager
    async def connection(self) -> AsyncContextManager[asyncpg.Connection]:
        async with self.pool.acquire() as conn:
            yield conn

    async def drop(self):
        async with self.connection() as conn:
            async with conn.transaction():
                await conn.execute(schema.DROP)

    async def create(self):
        async with self.connection() as conn:
            async with conn.transaction():
                await conn.execute(schema.CREATE)

    async def migrate(self):
        while 1:
            async with self.connection() as conn:
                try:
                    version = await conn.fetchval(sql.GET_VERSION) or 0
                except UndefinedTableError:
                    version = 0

                if version == schema.VERSION:
                    break

                if version > schema.VERSION:
                    raise ValueError(f'Database version {version} is newer than the schema VERSION {schema.VERSION} in the code, which should not happen')

                migration = schema.MIGRATIONS.get(version)
                if not migration:
                    raise ValueError(f'Migration is not defined for database version {version}')

                await conn.execute(migration)

                new_version = await conn.fetchval(sql.GET_VERSION) or 0
                if new_version <= version:
                    raise ValueError(f'New version {new_version} after migration must be higher than the former version {version}')

                print(f'Migrated database from version {version} to {new_version}')
