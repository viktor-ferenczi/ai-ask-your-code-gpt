__all__ = ['PythonDocType']

import uuid
from typing import Iterator

from doc_types.dt_text import TextDocType
from model.fragment import Fragment
from .splitters.python_splitter import PythonSplitter


class PythonDocType(TextDocType):
    extension: str = '.py'

    store_instruction: str = 'Represent the Python code for retrieval'
    query_instruction: str = 'Represent the Python question for retrieving relevant code'

    splitter_cls = PythonSplitter

    def load(self, path: str, text: str) -> Iterator[Fragment]:
        for index, chunk in enumerate(self.splitter.split_code(text)):
            yield Fragment(uuid=str(uuid.uuid4()), path=path, lineno=chunk.lineno, text=chunk.text, name=chunk.name)
