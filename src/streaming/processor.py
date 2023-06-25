from typing import Callable, Dict, Iterable

from kafka.consumer.fetcher import ConsumerRecord

from streaming.consumer import consume
from streaming.message import Message
from streaming.producer import send_many

THandler = Callable[[ConsumerRecord], Iterable[Message]]


def process(handlers: Dict[str, THandler], *, poll_ms: float = float('inf')):
    def iter_responses():
        topics = list(handlers.keys())
        for rec in consume(*topics, poll_ms=poll_ms):
            handler = handlers.get(rec.topic)
            if handler is None:
                continue
            try:
                responses = list(handler(rec))
            except KeyboardInterrupt:
                raise
            except:
                print(f'Unexpected error while processing message: {rec!r}')
            else:
                yield from responses

    send_many(iter_responses())
