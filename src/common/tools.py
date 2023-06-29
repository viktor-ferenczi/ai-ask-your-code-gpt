import asyncio
import time
import uuid
from asyncio import CancelledError
from typing import List, Callable, Iterator, Awaitable, Any

import tiktoken

ENCODING = tiktoken.encoding_for_model('gpt-3.5-turbo')


def find(lst: List[object], predicate: Callable[[object], bool]):
    for i, v in enumerate(lst):
        if predicate(v):
            return i
    return -1


def tiktoken_len(text):
    tokens = ENCODING.encode(
        text,
        disallowed_special=()
    )
    return len(tokens)


def find_iter(text: str, sub: str) -> Iterator[int]:
    i = 0
    e = len(text)
    while i < e:
        f = text.find(sub, i)
        if f < 0:
            break
        yield f
        i = f + len(sub)


def new_uuid() -> str:
    return str(uuid.uuid4())


async def wait_until_cancelled():
    while 1:
        try:
            await asyncio.sleep(3600)
        except CancelledError:
            break


def retry(fn: Callable[[], Any], handle_exceptions=(), max_retries: int = 9, delay: float = 0.01, delay_multiplier: float = 1.4142135, max_delay: float = 1.0) -> Any:
    for attempt in range(max_retries):
        try:
            return fn()
        except handle_exceptions:
            time.sleep(delay)
            delay = min(max_delay, delay * delay_multiplier)

    return fn()


async def async_retry(fn: Callable[[], Awaitable[Any]], handle_exceptions=(), max_retries: int = 9, delay: float = 0.01, delay_multiplier: float = 1.4142135, max_delay: float = 1.0) -> Any:
    for attempt in range(max_retries):
        try:
            return await fn()
        except handle_exceptions as e:
            print(f'WARNING: Retry {1 + attempt}/{max_retries} of {fn.__name__} in {delay:.3f}s due to error: [{e.__class__.__name__}] {e}')
            await asyncio.sleep(delay)
            delay = min(max_delay, delay * delay_multiplier)

    return await fn()
