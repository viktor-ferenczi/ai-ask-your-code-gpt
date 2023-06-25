from typing import AsyncIterable

from aiokafka import AIOKafkaProducer

from streaming.config import KAFKA_SERVER
from streaming.message import Message


async def send_one(msg: Message):
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_SERVER)

    # Get cluster layout and initial topic/partition leadership information
    await producer.start()

    try:
        # Produce message
        await producer.send_and_wait(msg.topic, msg.value)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()


async def send_many(iter_messages: AsyncIterable[Message]):
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_SERVER)

    # Get cluster layout and initial topic/partition leadership information
    await producer.start()

    try:
        # Produce messages
        async for msg in iter_messages:
            await producer.send_and_wait(msg.topic, msg.value)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()
