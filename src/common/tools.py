from typing import List, Callable

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
