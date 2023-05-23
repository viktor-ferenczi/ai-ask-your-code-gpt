__all__ = ['TextDocType']

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
        self.splitter: TextSplitter = self.splitter_cls(**self.splitter_kws)

    def split(self, path: str, text: str) -> Iterator[Fragment]:
        lineno = 1
        for index, paragraph in enumerate(self.splitter.split_text(text)):
            yield Fragment(path, lineno, paragraph, '')
            # FIXME: Not exact due to the splitter eating the separators, but good enough for sorting
            lineno += paragraph.count('\n') + 1
