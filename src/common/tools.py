from typing import List, Callable


def find(lst: List[object], predicate: Callable[[object], bool]):
    for i, v in enumerate(lst):
        if predicate(v):
            return i
    return -1
