__all__ = ['TextDocType']

import uuid
from typing import Iterator

from langchain.text_splitter import TextSplitter, RecursiveCharacterTextSplitter

from model.fragment import Fragment
from .splitters.tokenization import tiktoken_len


class TextDocType:
    extension: str = '.txt'

    store_instruction: str = 'Represent the document for retrieval'
    query_instruction: str = 'Represent the question for retrieving relevant paragraphs'

    splitter_cls = RecursiveCharacterTextSplitter
    splitter_kws = dict(
        chunk_size=400,
        chunk_overlap=0,
        length_function=tiktoken_len
    )

    def __init__(self) -> None:
        super().__init__()
        self.splitter = self.splitter_cls(**self.splitter_kws)

    def load(self, path: str, data: bytes) -> Iterator[Fragment]:
        # FIXME: Support multiple encodings
        text = data.decode('utf-8', errors='replace').replace('\r\n', '\n')

        lineno = 1
        for index, paragraph in enumerate(self.splitter.split_text(text)):
            yield Fragment(uuid=str(uuid.uuid4()), path=path, lineno=lineno, text=paragraph, name='')
            # FIXME: Not exact due to the splitter eating the separators, but good enough for sorting
            lineno += paragraph.count('\n') + 1
