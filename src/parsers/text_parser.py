import uuid
from typing import Iterator

from common.constants import C
from common.tools import tiktoken_len
from model.fragment import Fragment
from parsers.base_parser import BaseParser
from splitters.text_splitter import TextSplitter


class TextParser(BaseParser):
    extensions = ('txt',)
    mime_types = ('text/plain',)

    splitter = TextSplitter(
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
