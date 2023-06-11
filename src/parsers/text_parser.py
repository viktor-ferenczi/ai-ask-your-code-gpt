import uuid
from typing import Iterator

from common.constants import C
from common.tools import tiktoken_len
from model.fragment import Fragment
from parsers.base_parser import BaseParser
from splitters.text_splitter import TextSplitter


class TextParser(BaseParser):
    name = 'Text'
    extensions = ('txt',)
    mime_types = ('text/plain',)
    store_instruction = 'Represent the document for retrieval'
    query_instruction = 'Represent the text query for retrieving relevant paragraphs'

    splitter = TextSplitter(
        chunk_size=C.MAX_TOKENS_PER_FRAGMENT,
        length_function=tiktoken_len
    )

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        text = content.decode('utf-8', errors='replace').replace('\r', '')
        if not text.strip():
            return

        summary = [f'{path}:\n']
        for sentence in self.splitter.split_text(text):

            for line in sentence.text.split('\n'):
                for c in '.:)}]/':
                    if c in line and line.split(c)[0].strip().isdigit():
                        summary.append(f'{line}\n')

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
