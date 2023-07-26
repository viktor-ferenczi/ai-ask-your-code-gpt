from contextlib import asynccontextmanager
from typing import AsyncContextManager

import asyncpg
from asyncpg import UndefinedTableError, Connection

from common.constants import C
from storage import schema, properties


class Tasks:
    pass


class Database:

    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool

    @classmethod
    @asynccontextmanager
    async def create_pool(cls, dsn: str):
        async with asyncpg.create_pool(dsn, command_timeout=C.DATABASE_COMMAND_TIMEOUT) as pool:
            yield Database(pool)

    # Contexts


    @classmethod
    @asynccontextmanager
    async def from_dsn(cls, dsn: str) -> AsyncContextManager["Database"]:
        async with asyncpg.create_pool(dsn, command_timeout=C.DATABASE_COMMAND_TIMEOUT) as pool:
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
        if C.IS_PRODUCTION:
            raise RuntimeError('Refusing to drop the database in production')

        async with self.connection() as conn:
            async with conn.transaction():
                await conn.execute(schema.DROP)

        print(f'Dropped database')

    async def create(self):
        async with self.connection() as conn:
            async with conn.transaction():
                await conn.execute(schema.CREATE)

        print(f'Created database version {schema.VERSION}')

    async def migrate(self):
        while 1:
            async with self.connection() as conn:
                try:
                    version = await properties.read(conn, 'Version')
                except UndefinedTableError:
                    await self.create()
                    break

            if version == schema.VERSION:
                break

            if version > schema.VERSION:
                raise ValueError(f'Database version {version} is newer than the schema VERSION {schema.VERSION} in the code, which should not happen')

            migration = schema.MIGRATIONS.get(version)
            if not migration:
                raise ValueError(f'Migration is not defined for database version {version}')

            async with self.transaction() as conn:
                await conn.execute(migration)
                await properties.write(conn, 'Version', version + 1)

            print(f'Migrated database from version {version} to {version + 1}')
