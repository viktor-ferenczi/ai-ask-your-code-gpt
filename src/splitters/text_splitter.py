import re
from dataclasses import dataclass
from typing import Callable, Iterator, Collection, Tuple, List


@dataclass
class Sentence:
    lineno: int
    length: int
    depth: int
    text: str


class TextSplitter:
    max_depth = 32
    max_token_size = 8
    default_separators: Tuple[Tuple[str, str]] = (
        ('>', r"^\s*$"),
        ('>', r"^.*$"),
        ('>', r"\s+"),
    )

    def __init__(self, *, chunk_size: int, length_function: Callable[[str], int], separators: Collection[Tuple[str, str]] = ()) -> None:
        self.chunk_size: int = chunk_size
        self.length_function: Callable[[str], int] = length_function

        self.separators: List[Tuple[str, re.Pattern[str]]] = [
            (affinity, re.compile(pattern, re.MULTILINE))
            for affinity, pattern in (separators or self.default_separators)
        ]

    def split_text(self, text: str) -> Iterator[Sentence]:
        lineno = 1
        for length, depth, text in self.__split_recursive(text, 0):
            yield Sentence(lineno, length, depth, text)
            lineno += text.count('\n')

    def __split_recursive(self, text: str, depth: int) -> Iterator[Tuple[int, int, str]]:
        if not text:
            return

        if len(text) <= self.chunk_size or depth > self.max_depth:
            length = self.length_function(text)
            yield length, depth, text
            return

        if len(text) < self.max_token_size * self.chunk_size:
            length = self.length_function(text)
            if length <= self.chunk_size:
                yield length, depth, text
                return

        if depth >= len(self.separators):
            half = len(text) // 2
            if half:
                yield from self.__split_recursive(text[:half], depth + 1)
            yield from self.__split_recursive(text[half:], depth + 1)
            return

        affinity, rx = self.separators[depth]
        parts: List[str] = rx.split(text)
        if len(parts) < 2:
            yield from self.__split_recursive(text, depth + 1)
            return

        seps = rx.findall(text)
        assert len(seps) + 1 == len(parts)

        if affinity == '>':
            for part, sep in zip(parts[:-1], seps):
                yield from self.__split_recursive(part + sep, depth + 1)
            yield from self.__split_recursive(parts[-1], depth + 1)

        elif affinity == '<':
            yield from self.__split_recursive(parts[0], depth + 1)
            for sep, part in zip(seps, parts[1:]):
                yield from self.__split_recursive(sep + part, depth + 1)

        else:
            raise ValueError(f'Invalid separator affinity: {affinity}')
