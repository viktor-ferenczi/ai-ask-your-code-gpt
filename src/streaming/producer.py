from typing import Iterable

from kafka import KafkaProducer

from streaming.config import KAFKA_SERVER
from streaming.message import Message


def send_one(msg: Message):
    producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER])
    producer.send(msg.topic, msg.value)


def send_many(iter_messages: Iterable[Message]):
    producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER])
    for msg in iter_messages:
        producer.send(msg.topic, msg.value)
