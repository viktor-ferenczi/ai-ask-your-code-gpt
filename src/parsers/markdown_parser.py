import uuid
from typing import Iterator

from common.constants import C
from splitters.markdown_splitter import MarkdownSplitter
from common.tools import tiktoken_len
from model.fragment import Fragment
from parsers import BaseParser


# FIXME: Replace with proper parser
class MarkdownParser(BaseParser):
    extensions = ('md',)
    mime_types = ('text/markdown',)

    splitter = MarkdownSplitter(
        chunk_size=C.MAX_TOKENS_PER_FRAGMENT,
        length_function=tiktoken_len
    )

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        text = content.decode('utf-8', errors='surrogateescape').replace('\r', '')
        for sentence in self.splitter.split_text(text):
            yield Fragment(
                uuid=str(uuid.uuid4()),
                path=path,
                lineno=sentence.lineno,
                depth=sentence.depth,
                type='documentation',
                name='',
                text=sentence.text,
            )
