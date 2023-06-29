import asyncio
from typing import List

from base_storage_test import BaseStorageTest
from storage.pubsub import PubSub


class TestPubSub(BaseStorageTest):
    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()
        self.pubsub = PubSub(self.db)

    async def asyncTearDown(self) -> None:
        del self.pubsub
        await super().asyncTearDown()

    async def test_timeout(self) -> None:
        try:
            await self.pubsub.receive_with_timeout(0.1)
        except asyncio.TimeoutError:
            self.assertTrue(True)
        else:
            self.fail()

    async def test_event(self) -> None:
        numbers: List[int] = []

        async def receive():
            async for event in self.pubsub.iter_events():
                if event.channel == 'Test':
                    numbers.append(event.params['x'])
                    break

        async with self.pubsub.listen('Test'):
            await self.pubsub.send('Test', x=42)
            await asyncio.wait_for(receive(), timeout=0.1)

        self.assertEqual(len(numbers), 1)
        self.assertEqual(numbers[0], 42)
