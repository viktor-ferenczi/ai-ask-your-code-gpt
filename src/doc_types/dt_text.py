__all__ = ['TextDocType']

import uuid
from typing import Iterator

from common.text_splitter import TextSplitter

from common.constants import C
from model.fragment import Fragment
from common.tools import tiktoken_len


class TextDocType:
    code = False


    parser_cls = TextSplitter
    parser_kws = dict(
        chunk_size=C.MAX_TOKENS_PER_FRAGMENT,
        length_function=tiktoken_len
    )

    def __init__(self) -> None:
        super().__init__()
        self.splitter = self.parser_cls(**self.parser_kws)

    def load(self, path: str, data: bytes) -> Iterator[Fragment]:
        # FIXME: Support multiple encodings
        text = data.decode('utf-8', errors='replace').replace('\r\n', '\n')

        lineno = 1
        for index, paragraph in enumerate(self.splitter.split_text(text)):
            yield Fragment(uuid=str(uuid.uuid4()), path=path, lineno=lineno, text=paragraph, name='')
            lineno += paragraph.count('\n')

    @classmethod
    def summarize(cls, text: str) -> Iterator[str]:
        max_width = C.MAX_SUMMARY_WIDTH
        for section in text.split('\n\n'):
            section = section.strip()
            if section and '\n' not in section and section[:1].isdigit():
                if len(section) <= max_width:
                    yield section
                else:
                    yield f'{section[:max_width]}...'
