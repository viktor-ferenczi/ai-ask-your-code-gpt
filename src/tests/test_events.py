import asyncio
import unittest
from datetime import datetime
from typing import List

import asyncpg

from common.tools import wait_until_cancelled
from storage.events import Producer, Consumer, Cleanup, EventName


class TestProducerConsumer(unittest.IsolatedAsyncioTestCase):
    # postgres://user:password@host:port/database
    dsn = 'postgres://askyourcode:askyourcode@127.0.0.1:5432/askyourcode_test'

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        async with asyncpg.create_pool(self.dsn, command_timeout=60) as pool:
            cleanup = Cleanup(pool)
            await cleanup.recreate_table()
            await cleanup.delete_all_events()

    async def test_produce_consume(self):
        async with asyncpg.create_pool(self.dsn, command_timeout=60) as pool:
            producer = Producer(pool)
            consumer = Consumer(pool)

            events: List[str] = []

            # Register callback
            async def event_handler(param1: str):
                events.append(param1)
                self.assertEqual(param1, 'value1')

            consumer.register_event_handler(EventName.Test1, event_handler)

            async with consumer.listen():
                # Produce event
                started = datetime.utcnow()
                created = await producer.publish_event(EventName.Test1, {"param1": "value1"})
                finished = datetime.utcnow()
                self.assertTrue(started <= created)
                self.assertTrue(created <= finished)

                # Run consumer for a short time to process event
                await asyncio.wait_for(wait_until_cancelled(), timeout=0.5)

            self.assertEqual(len(events), 1)

    async def test_produce_consume_fail(self):
        async with asyncpg.create_pool(self.dsn, command_timeout=60) as pool:
            producer = Producer(pool)
            consumer = Consumer(pool)

            events: List[str] = []

            # Register callback that fails
            async def event_handler(param1: str):
                events.append(param1)
                raise Exception('Test Exception')

            consumer.register_event_handler(EventName.Test2, event_handler)

            async with consumer.listen():
                # Produce event
                await producer.publish_event(EventName.Test2, {"param1": "value1"})

                # Run consumer for a short time to process event
                await asyncio.wait_for(wait_until_cancelled(), timeout=0.5)

            self.assertEqual(len(events), 1)


if __name__ == '__main__':
    unittest.main()
