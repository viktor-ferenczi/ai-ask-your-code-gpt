from typing import Iterator

from langchain.text_splitter import PythonCodeTextSplitter
from parsers.text_splitter import TextSplitter

from model.chunk import Chunk
from .python_parser import PythonParser


class PythonSplitter:

    def __init__(self, **kws) -> None:
        self.fallback_splitter = PythonCodeTextSplitter(**kws)
        self.body_splitter = TextSplitter(**kws)

    def split_code(self, code: str) -> Iterator[Chunk]:
        # noinspection PyBroadException
        try:
            # Try proper parsing first
            parser = PythonParser(self.body_splitter)
            yield from parser.parse(code)
        except KeyboardInterrupt:
            raise
        except Exception:
            # In case of invalid syntax fall back to a regexp based splitter
            lineno = 1
            for text in self.fallback_splitter.split_text(code):
                yield Chunk(lineno, text, '')
                lineno += text.count('\n')
