import uuid
from typing import List, Callable, Iterator

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
