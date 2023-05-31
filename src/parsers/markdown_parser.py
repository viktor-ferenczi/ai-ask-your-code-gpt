import uuid
from typing import Iterator

from common.constants import C
from common.tools import tiktoken_len
from model.fragment import Fragment
from parsers import BaseParser
from splitters.markdown_splitter import MarkdownSplitter


# FIXME: Replace with proper parser
class MarkdownParser(BaseParser):
    extensions = ('md',)
    mime_types = ('text/markdown',)
    store_instruction = 'Represent the Markdown document for retrieval'
    query_instruction = 'Represent the text query for retrieving relevant sections'

    splitter = MarkdownSplitter(
        chunk_size=C.MAX_TOKENS_PER_FRAGMENT,
        length_function=tiktoken_len
    )

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        text = content.decode('utf-8', errors='surrogateescape').replace('\r', '')
        summary = []
        for sentence in self.splitter.split_text(text):
            if sentence.text.startswith('#'):
                summary.append(sentence.text.split('\n', 1)[0] + '\n')
            yield Fragment(
                uuid=str(uuid.uuid4()),
                path=path,
                lineno=sentence.lineno,
                depth=sentence.depth,
                type='documentation',
                name='',
                text=sentence.text,
            )

        yield Fragment(
            uuid=str(uuid.uuid4()),
            path=path,
            lineno=1,
            depth=0,
            type='summary',
            name='',
            text=''.join(summary),
        )
