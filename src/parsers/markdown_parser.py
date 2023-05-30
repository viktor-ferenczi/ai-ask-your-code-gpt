import re
import uuid
from typing import Iterator

from common.constants import C
from common.markdown_splitter import MarkdownSplitter
from model.fragment import Fragment
from parsers.base_parser import BaseParser

RX_MARKDOWN_HEADING = re.compile(r'^(#{1,6})\s+(.*)$')


# FIXME: Use a proper Markdown parser instead!
class MarkdownParser(BaseParser):
    extension = ('md',)
    mime_types = ('text/markdown',)

    def __init__(self) -> None:
        super().__init__()
        self.splitter = MarkdownSplitter(C.MAX_TOKENS_PER_FRAGMENT)

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        text = content.decode('utf-8', errors='surrogateescape')
        lineno = 1
        depth = 0
        for part in self.splitter.split_text(text):
            lines = part.split('\n')

            name = ''
            for line in lines:
                m = RX_MARKDOWN_HEADING.match(line.lstrip())
                if m is not None:
                    d = len(m.group(1))
                    if d < depth or not name:
                        name = m.group(2).rstrip()
                    depth = d

            yield Fragment(
                uuid=str(uuid.uuid4()),
                path=path,
                lineno=lineno,
                depth=depth,
                type='text',
                name=name,
                text=part,
            )

            lineno += len(lines)
