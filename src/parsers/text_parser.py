import uuid
from typing import Iterator

from common.constants import C
from common.text_splitter import TextSplitter
from model.fragment import Fragment
from parsers.base_parser import BaseParser


class TextParser(BaseParser):
    extensions = ('txt',)
    mime_types = ('text/plain',)

    def __init__(self) -> None:
        super().__init__()
        self.splitter = TextSplitter(C.MAX_TOKENS_PER_FRAGMENT)

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        text = content.decode('utf-8', errors='surrogateescape')
        lineno = 1
        for part in self.splitter.split_text(text):
            yield Fragment(
                uuid=str(uuid.uuid4()),
                path=path,
                lineno=lineno,
                depth=0,
                type='text',
                name='',
                text=part,
            )
            lineno += part.count('\n')
