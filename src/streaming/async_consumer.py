import os
from typing import AsyncGenerator

from aiokafka import AIOKafkaConsumer, ConsumerRecord

KAFKA_SERVER = os.environ.get('KAFKA_SERVER', 'localhost:9092')
KAFKA_GROUP = os.environ.get('KAFKA_GROUP', 'default-group')


async def consume(*topics: str) -> AsyncGenerator[ConsumerRecord]:
    consumer = AIOKafkaConsumer(
        *topics,
        bootstrap_servers=KAFKA_SERVER,
        group_id=KAFKA_GROUP)

    # Get cluster layout and join group `my-group`
    await consumer.start()

    try:
        # Consume messages
        async for msg in consumer:
            yield msg
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()
