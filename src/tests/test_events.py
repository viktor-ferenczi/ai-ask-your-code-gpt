import asyncio
import unittest
from datetime import datetime

import asyncpg

from common.events import Producer, Consumer, Cleanup
from common.tools import wait_until_cancelled


class TestProducerConsumer(unittest.IsolatedAsyncioTestCase):
    # postgres://user:password@host:port/database
    dsn = 'postgres://askyourcode:askyourcode@127.0.0.1:5432/askyourcode_test'

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        async with asyncpg.create_pool(self.dsn, command_timeout=60) as pool:
            cleanup = Cleanup(pool)
            await cleanup.delete_all_events()

    async def test_produce_consume(self):
        async with asyncpg.create_pool(self.dsn, command_timeout=60) as pool:
            producer = Producer(pool)
            consumer = Consumer(pool)

            events = []

            # Register callback
            async def event_handler(param1: str):
                events.append(param1)
                self.assertEqual(param1, 'value1')

            consumer.register_event_handler('event1', event_handler)

            async with consumer.listen():
                # Produce event
                started = datetime.utcnow()
                created = await producer.publish_event('event1', {"param1": "value1"})
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

            events = []

            # Register callback that fails
            async def event_handler(param1: str):
                events.append(param1)
                raise Exception('Test Exception')

            consumer.register_event_handler('event2', event_handler)

            async with consumer.listen():
                # Produce event
                await producer.publish_event('event2', {"param1": "value1"})

                # Run consumer for a short time to process event
                await asyncio.wait_for(wait_until_cancelled(), timeout=0.5)

            self.assertEqual(len(events), 1)


if __name__ == '__main__':
    unittest.main()
