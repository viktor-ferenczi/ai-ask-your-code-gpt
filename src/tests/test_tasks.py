import asyncio
import unittest
from datetime import datetime
from typing import List

import asyncpg

from common.tools import wait_until_cancelled
from storage.tasks import Scheduler, Processor, Cleanup, TaskFailed, TaskName


class TestProducerConsumer(unittest.IsolatedAsyncioTestCase):
    # postgres://user:password@host:port/database
    dsn = 'postgres://askyourcode:askyourcode@127.0.0.1:5432/askyourcode_test'

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        async with asyncpg.create_pool(self.dsn, command_timeout=60) as pool:
            cleanup = Cleanup(pool)
            await cleanup.recreate_table()
            await cleanup.delete_all_tasks()

    async def test_produce_consume(self):
        async with asyncpg.create_pool(self.dsn, command_timeout=60) as pool:
            scheduler = Scheduler(pool)
            processor = Processor(pool)

            tasks1: List[str] = []

            # Register callback
            async def task_processor(param1: str):
                tasks1.append(param1)
                self.assertEqual(param1, 'value1')

            processor.register_task(TaskName.Test1, task_processor)

            async with processor.listen():
                # Produce task
                started = datetime.utcnow()
                created = await scheduler.schedule(TaskName.Test1, 'P1', param1='value1')
                finished = datetime.utcnow()
                self.assertTrue(started <= created, f'{started!r} <= {created!r}')
                self.assertTrue(created <= finished, f'{created!r} <= {finished!r}')

                # Run consumer for a short time to process task
                await asyncio.wait_for(wait_until_cancelled(), timeout=0.5)

            self.assertEqual(len(tasks1), 1)

            tasks2 = await scheduler.check(TaskName.Test1, 'P1')
            self.assertEqual(len(tasks2), 1)
            self.assertEqual(tasks2[0]['created'], created)

            tasks3 = await scheduler.check(TaskName.Test2, '?')
            self.assertEqual(len(tasks3), 0)

    async def test_produce_consume_fail(self):
        async with asyncpg.create_pool(self.dsn, command_timeout=60) as pool:
            scheduler = Scheduler(pool)
            processor = Processor(pool)

            tasks1: List[str] = []

            # Register callback that fails
            async def task_processor(param1: str):
                tasks1.append(param1)
                raise TaskFailed('Test Failed')

            processor.register_task(TaskName.Test2, task_processor)

            async with processor.listen():
                # Produce task
                await scheduler.schedule(TaskName.Test2, 'P2', param1='value1')

                # Run consumer for a short time to process task
                await asyncio.wait_for(wait_until_cancelled(), timeout=0.5)

            self.assertEqual(len(tasks1), 1)

            tasks2 = await scheduler.check(TaskName.Test2, 'P2')
            self.assertEqual(len(tasks2), 1)
            self.assertEqual(tasks2[0]['message'], 'Test Failed')

    async def test_produce_consume_unexpected_error(self):
        async with asyncpg.create_pool(self.dsn, command_timeout=60) as pool:
            scheduler = Scheduler(pool)
            processor = Processor(pool)

            tasks1: List[str] = []

            # Register callback that fails
            async def task_processor(param1: str):
                tasks1.append(param1)
                raise Exception('Test Exception')

            processor.register_task(TaskName.Test2, task_processor)

            async with processor.listen():
                # Produce task
                await scheduler.schedule(TaskName.Test2, 'P2', param1='value1')

                # Run consumer for a short time to process task
                await asyncio.wait_for(wait_until_cancelled(), timeout=0.5)

            self.assertEqual(len(tasks1), 1)

            tasks2 = await scheduler.check(TaskName.Test2, 'P2')
            self.assertEqual(len(tasks2), 1)
            self.assertEqual(tasks2[0]['message'], 'Unexpected error')
            self.assertTrue("raise Exception('Test Exception')" in tasks2[0]['traceback'])


if __name__ == '__main__':
    unittest.main()
