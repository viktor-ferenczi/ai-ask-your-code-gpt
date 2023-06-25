import os
from typing import Tuple, AsyncIterable

from aiokafka import AIOKafkaProducer

KAFKA_SERVER = os.environ.get('KAFKA_SERVER', 'localhost:9092')


async def send_one(topic: str, payload: bytes):
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_SERVER)

    # Get cluster layout and initial topic/partition leadership information
    await producer.start()

    try:
        # Produce message
        await producer.send_and_wait(topic, payload)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()


async def send_many(iter_messages: AsyncIterable[Tuple[str, bytes]]):
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_SERVER)

    # Get cluster layout and initial topic/partition leadership information
    await producer.start()

    try:
        # Produce messages
        async for topic, payload in iter_messages:
            await producer.send_and_wait(topic, payload)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()
