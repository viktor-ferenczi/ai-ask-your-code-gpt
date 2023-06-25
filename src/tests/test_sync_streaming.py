import unittest
from pprint import pformat
from typing import Iterable, List

from kafka.consumer.fetcher import ConsumerRecord

from common.tools import new_uuid
from streaming.admin import create_topic, delete_topic
from streaming.consumer import consume
from streaming.message import Message
from streaming.processor import process
from streaming.producer import send_one, send_many

TOPIC1 = f'Test-{new_uuid()}'
TOPIC2 = f'Test-{new_uuid()}'

TOPICS = [TOPIC1, TOPIC2]


class TestSyncStreaming(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        for topic in TOPICS:
            create_topic(topic)

    def tearDown(self) -> None:
        super().tearDown()
        for topic in TOPICS:
            delete_topic(topic)

    def test_streaming(self):
        for _ in range(1):

            send_one(Message(TOPIC1, b'1'))
            send_many([Message(TOPIC1, b'2'), Message(TOPIC1, b'3')])

            msgs = self.consume_messages(3)
            self.verify_messages(msgs, TOPIC1)

    def test_processor(self):
        for _ in range(5):

            send_many([Message(TOPIC1, f'{i}'.encode()) for i in range(3)])

            def handler(rec: ConsumerRecord) -> Iterable[Message]:
                n = int(rec.value.decode())
                yield Message(TOPIC2, f'{n + 1}'.encode())

            process({TOPIC1: handler}, poll_ms=500)

            msgs = self.consume_messages(3)
            self.verify_messages(msgs, TOPIC2)

    def consume_messages(self, count: int):
        msgs = list(consume(TOPIC1, poll_ms=500))
        self.assertEqual(len(msgs), count, f'len(msgs)={len(msgs)}')
        return msgs

    def verify_messages(self, msgs: List[ConsumerRecord], topic: str):
        msgs.sort(key=lambda m: int(m.value.decode()))
        for i, msg in enumerate(msgs):
            self.assertEqual(msg.topic, topic)
            self.assertEqual(msg.value, f'{i + 1}'.encode(), pformat(msgs))
