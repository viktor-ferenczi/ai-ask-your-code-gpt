import uuid
from typing import Iterator

from common.constants import C
from common.tools import tiktoken_len
from model.fragment import Fragment
from parsers.base_parser import BaseParser
from splitters.text_splitter import TextSplitter


class PythonParser(BaseParser):
    extensions = ('py',)
    mime_types = ('text/python', 'text/x-python')
    store_instruction = 'Represent the Python code for retrieval'
    query_instruction = 'Represent the text query for retrieving relevant parts of the code'
    tree_sitter_language_name = 'python'

    def __init__(self) -> None:
        super().__init__()
        self.splitter = TextSplitter(
            chunk_size=C.MAX_TOKENS_PER_FRAGMENT,
            length_function=tiktoken_len,
            separators=(
                ('<', r"^\s+class\s+"),
                ('<', r"^\s+def\s+"),
            )
        )

    # FIXME: Replace with proper parser
    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        text = content.decode('utf-8', errors='surrogateescape').replace('\r', '')
        for sentence in self.splitter.split_text(text):
            yield Fragment(
                uuid=str(uuid.uuid4()),
                path=path,
                lineno=sentence.lineno,
                depth=sentence.depth,
                type='python',
                name='',
                text=sentence.text,
            )
