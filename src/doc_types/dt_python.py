__all__ = ['PythonDocType']

import uuid
from typing import Iterator

from doc_types.dt_text import TextDocType
from model.fragment import Fragment
from parsers.python_splitter import PythonSplitter


class PythonDocType(TextDocType):
    code = True

    store_instruction: str = 'Represent the Python code for retrieval'
    query_instruction: str = 'Represent the text query for retrieving relevant parts of the code'

    parser_cls = PythonSplitter

    def load(self, path: str, data: bytes) -> Iterator[Fragment]:
        # FIXME: Support multiple encodings
        text = data.decode('utf-8', errors='replace').replace('\r\n', '\n')

        for index, chunk in enumerate(self.splitter.split_code(text)):
            yield Fragment(uuid=str(uuid.uuid4()), path=path, lineno=chunk.lineno, text=chunk.text, name=chunk.name)
