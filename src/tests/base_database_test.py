import asyncio
import os
import shutil
import unittest
from typing import Any

import asyncpg
from asyncpg import Pool

from common.constants import C
from storage.database import Database
from storage.pubsub import PubSub
from storage.scheduler import Scheduler


class BaseDatabaseTest(unittest.IsolatedAsyncioTestCase):
    first = True

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        if C.IS_PRODUCTION:
            raise RuntimeError('Do not run the test suite in production!')

        self.maxDiff = 32768

        print(f'Cleared archive directory: {C.ARCHIVE_DIR}')
        if os.path.isdir(C.ARCHIVE_DIR):
            for _ in range(10):
                try:
                    shutil.rmtree(C.ARCHIVE_DIR)
                except (IOError, OSError):
                    await asyncio.sleep(0.5)
                else:
                    break

        self.pool: Pool = asyncpg.create_pool(C.DSN, command_timeout=60, min_size=1, max_size=10)
        await self.pool._async__init__()
        self.db = Database(self.pool)

        if BaseDatabaseTest.first:
            await self.db.drop()
            BaseDatabaseTest.first = False

        await self.db.migrate()

        self.scheduler = Scheduler(self.db)
        self.pubsub = PubSub(self.db)

        await self.scheduler.delete_all_tasks()

        await asyncio.sleep(0.01)

    async def asyncTearDown(self) -> None:
        del self.db

        self.pool.terminate()
        del self.pool

        # Without this the test suite continues to spin in PyCharm
        await asyncio.sleep(0.01)

        await super().asyncTearDown()

    def assertEqual(self, first: Any, second: Any, msg: Any = ...) -> None:
        super().assertEqual(second, first, msg)

    def assertNotEqual(self, first: Any, second: Any, msg: Any = ...) -> None:
        super().assertNotEqual(second, first, msg)
