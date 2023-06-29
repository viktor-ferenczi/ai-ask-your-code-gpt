import unittest

import asyncpg
from asyncpg import Pool

from common.constants import C
from storage.database import Database


class BaseTestCase(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        if C.IS_PRODUCTION:
            raise RuntimeError('Do not run the test suite in production!')

        self.pool: Pool = asyncpg.create_pool(C.DSN, command_timeout=60)
        await self.pool._async__init__()
        self.db = Database(self.pool)

        await self.db.migrate()

    async def asyncTearDown(self) -> None:
        del self.db

        self.pool.terminate()
        del self.pool

        await super().asyncTearDown()
