import os
from typing import Generator

from kafka import KafkaConsumer
from kafka.consumer.fetcher import ConsumerRecord

KAFKA_SERVER = os.environ.get('KAFKA_SERVER', 'localhost:9092')
KAFKA_GROUP = os.environ.get('KAFKA_GROUP', 'default-group')


def consume(*topics: str) -> Generator[ConsumerRecord]:
    consumer = KafkaConsumer(
        *topics,
        bootstrap_servers=KAFKA_SERVER,
        group_id=KAFKA_GROUP)

    # Consume messages
    yield from consumer
