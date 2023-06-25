from typing import AsyncIterable

from aiokafka import AIOKafkaConsumer, ConsumerRecord

from streaming.config import KAFKA_SERVER


async def consume(*topics: str, group_id: str = '') -> AsyncIterable[ConsumerRecord]:
    if not group_id:
        group_id = '+'.join(sorted(topics))

    consumer = AIOKafkaConsumer(
        *topics,
        bootstrap_servers=KAFKA_SERVER,
        group_id=group_id)

    # Get cluster layout and join group `my-group`
    await consumer.start()

    try:
        # Consume messages
        async for rec in consumer:
            yield rec
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()
