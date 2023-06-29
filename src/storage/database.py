from contextlib import asynccontextmanager
from typing import AsyncContextManager

import asyncpg
from asyncpg import UndefinedTableError, Connection

from storage import schema, properties


class Tasks:
    pass


class Database:

    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool
        
    @classmethod
    @asynccontextmanager
    async def create_pool(cls, dsn: str):
        async with asyncpg.create_pool(dsn, command_timeout=60) as pool:
            yield Database(pool)

    # Contexts

    # @classmethod
    # @asynccontextmanager
    # async def from_dsn(cls, dsn: str) -> AsyncContextManager["Database"]:
    #     # FIXME: This should work, but instead freezes at the end of block:
    #     # async with asyncpg.create_pool(dsn, command_timeout=60) as pool:
    #
    #     # Workaround
    #     pool: Pool = asyncpg.create_pool(cls.dsn, command_timeout=60)
    #     await pool._async__init__()
    #     try:
    #         yield Database(pool)
    #     finally:
    #         pool.terminate()

    @classmethod
    @asynccontextmanager
    async def from_dsn(cls, dsn: str) -> AsyncContextManager["Database"]:
        async with asyncpg.create_pool(dsn, command_timeout=60) as pool:
            yield cls(pool)

    @asynccontextmanager
    async def connection(self) -> AsyncContextManager[Connection]:
        async with self.pool.acquire() as conn:
            yield conn

    @asynccontextmanager
    async def transaction(self, *, readonly=False) -> AsyncContextManager[Connection]:
        async with self.pool.acquire() as conn:
            async with conn.transaction(readonly=readonly):
                yield conn

    # Schema creation and migration

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
                    version = await properties.read(conn, 'Version')
                except UndefinedTableError:
                    version = 0

                if version == schema.VERSION:
                    break

                if version > schema.VERSION:
                    raise ValueError(f'Database version {version} is newer than the schema VERSION {schema.VERSION} in the code, which should not happen')

                migration = schema.MIGRATIONS.get(conn, version)
                if not migration:
                    raise ValueError(f'Migration is not defined for database version {version}')

                await conn.execute(migration)

                new_version = await properties.read(conn, 'Version') or 0
                if new_version <= version:
                    raise ValueError(f'New version {new_version} after migration must be higher than the former version {version}')

                print(f'Migrated database from version {version} to {new_version}')
