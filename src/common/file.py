from io import FileIO
from typing import Iterator


def iter_line_offsets(f: FileIO) -> Iterator[int]:
    offset: int = 0
    for _ in f:
        yield offset
        offset = f.tell()
