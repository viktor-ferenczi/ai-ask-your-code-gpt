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

    async def test_event(self) -> None:
        numbers: List[int] = []

        async def receive():
            async for event in self.pubsub.listen('Test'):
                if event.channel == 'Test':
                    numbers.append(event.params['x'])
                    break

        async def send():
            await asyncio.sleep(0.2)
            await self.pubsub.send('Test', x=42)

        await asyncio.wait([receive(), send()])

        self.assertEqual(len(numbers), 1)
        self.assertEqual(numbers[0], 42)
