from typing import Iterable

from kafka import KafkaConsumer
from kafka.consumer.fetcher import ConsumerRecord

from streaming.config import KAFKA_SERVER


def consume(*topics: str,
            group_id: str = '',
            poll_ms: float = float('inf')) -> Iterable[ConsumerRecord]:
    if not group_id:
        group_id = '+'.join(sorted(topics))

    consumer = KafkaConsumer(
        *topics,
        bootstrap_servers=KAFKA_SERVER,
        group_id=group_id,
        auto_offset_reset='earliest'
    )

    # Consume messages
    while 1:
        topic_records = consumer.poll(poll_ms, max_records=1)
        if not topic_records:
            break
        for records in topic_records.values():
            yield from records
