import unittest

import asyncpg
from asyncpg import Pool

from common.constants import C
from storage.database import Database


class BaseStorageTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        self.pool: Pool = asyncpg.create_pool(C.TEST_DSN, command_timeout=60)
        await self.pool._async__init__()
        self.db = Database(self.pool)

        await self.db.migrate()

    async def asyncTearDown(self) -> None:
        del self.db

        self.pool.terminate()
        del self.pool

        await super().asyncTearDown()
