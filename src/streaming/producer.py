import os
from typing import Iterable, Tuple

from kafka import KafkaProducer

KAFKA_SERVER = os.environ.get('KAFKA_SERVER', 'localhost:9092')


def send_one(topic: str, payload: bytes):
    producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER])
    producer.send(topic, payload)


def send_many(iter_messages: Iterable[Tuple[str, bytes]]):
    producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER])
    for topic, payload in iter_messages:
        producer.send(topic, payload)
