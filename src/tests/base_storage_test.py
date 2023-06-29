import unittest

import asyncpg
from asyncpg import Pool

from storage.database import Database


class BaseStorageTest(unittest.IsolatedAsyncioTestCase):
    # postgres://user:password@host:port/database
    dsn = 'postgres://askyourcode:askyourcode@127.0.0.1:5432/askyourcode_test'

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        self.pool: Pool = asyncpg.create_pool(self.dsn, command_timeout=60)
        await self.pool._async__init__()
        self.db = Database(self.pool)

        await self.db.migrate()

    async def asyncTearDown(self) -> None:
        del self.db

        self.pool.terminate()
        del self.pool

        await super().asyncTearDown()
