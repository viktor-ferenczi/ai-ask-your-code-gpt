import asyncio
import unittest

import asyncpg
from asyncpg import Pool

from common.constants import C
from storage.database import Database
from storage.pubsub import PubSub
from storage.scheduler import Scheduler


class BaseTestCase(unittest.IsolatedAsyncioTestCase):
    first = True

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        if C.IS_PRODUCTION:
            raise RuntimeError('Do not run the test suite in production!')

        self.maxDiff = 32768

        self.pool: Pool = asyncpg.create_pool(C.DSN, command_timeout=60)
        await self.pool._async__init__()
        self.db = Database(self.pool)

        cls = self.__class__
        if cls.first:
            await self.db.drop()
            cls.first = False

        await self.db.migrate()

        self.scheduler = Scheduler(self.db)
        self.pubsub = PubSub(self.db)

        await self.scheduler.delete_all_tasks()

    async def asyncTearDown(self) -> None:
        del self.db

        self.pool.terminate()
        del self.pool

        # Without this the test suite continues to spin in PyCharm
        await asyncio.sleep(0.01)

        await super().asyncTearDown()
