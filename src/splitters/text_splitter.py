import re
from dataclasses import dataclass
from typing import Callable, Iterator, Collection, Tuple, List, Optional


@dataclass
class Sentence:
    lineno: int
    length: int
    depth: int
    text: str
    start: int


class TextSplitter:
    max_depth = 32
    max_token_size = 8
    default_separators: Tuple[Tuple[str, str]] = (
        ('>', r"^\s*$"),  # Paragraphs
        ('>', r"[\.\!\?\:\;]\s+"),  # Sentences
        ('>', r"\n"),  # Lines
        ('>', r"\s+"),  # Words
    )

    def __init__(self, *, chunk_size: int, length_function: Callable[[str], int], separators: Collection[Tuple[str, str]] = ()) -> None:
        self.chunk_size: int = chunk_size
        self.length_function: Callable[[str], int] = length_function

        self.separators: List[Tuple[str, re.Pattern[str]]] = [
            (affinity, re.compile(pattern, re.MULTILINE))
            for affinity, pattern in (separators or self.default_separators)
        ]

    def split_text(self, text: str) -> Iterator[Sentence]:
        lineno: int = 1
        start: int = 0
        sentence: Optional[Sentence] = None
        for length, depth, text in self.__split_recursive(text, 0, 0):

            # Merging subsequent sentences at the same length
            if sentence is None:
                sentence = Sentence(lineno, length, depth, text, start)
            elif sentence.depth <= depth and sentence.length + length <= self.chunk_size:
                sentence.length += length
                sentence.text += text
            else:
                yield sentence
                sentence = Sentence(lineno, length, depth, text, start)

            lineno += text.count('\n')
            start += len(text)

        if sentence is not None:
            yield sentence

    def __split_recursive(self, text: str, sep_index: int, depth: int) -> Iterator[Tuple[int, int, str]]:
        if not text:
            return

        if len(text) <= self.chunk_size or sep_index > self.max_depth:
            length = self.length_function(text)
            yield length, depth, text
            return

        if len(text) < self.max_token_size * self.chunk_size:
            length = self.length_function(text)
            if length <= self.chunk_size:
                yield length, depth, text
                return

        if sep_index >= len(self.separators):
            half = len(text) // 2
            if half:
                yield from self.__split_recursive(text[:half], sep_index + 1, depth)
            yield from self.__split_recursive(text[half:], sep_index + 1, depth)
            return

        affinity, rx = self.separators[sep_index]
        parts: List[str] = rx.split(text)
        if len(parts) < 2:
            yield from self.__split_recursive(text, sep_index + 1, depth)
            return

        seps = rx.findall(text)
        assert len(seps) + 1 == len(parts)

        if affinity == '>':
            yield from self.__split_recursive(parts[0] + seps[0], sep_index + 1, depth)
            if len(parts) > 2:
                for part, sep in zip(parts[1:-1], seps[1:]):
                    yield from self.__split_recursive(part + sep, sep_index + 1, sep_index + 1)
            if parts[-1]:
                yield from self.__split_recursive(parts[-1], sep_index + 1, sep_index + 1)

        elif affinity == '<':
            if parts[0]:
                yield from self.__split_recursive(parts[0], sep_index + 1, sep_index + 1)
            for sep, part in zip(seps, parts[1:]):
                yield from self.__split_recursive(sep + part, sep_index + 1, sep_index + 1)

        else:
            raise ValueError(f'Invalid separator affinity: {affinity}')
