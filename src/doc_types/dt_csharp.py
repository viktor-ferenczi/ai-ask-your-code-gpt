__all__ = ['CSharpDocType']

import uuid
from typing import Iterator

from common.constants import C
from doc_types.dt_text import TextDocType
from model.fragment import Fragment
from parsers.python_splitter import PythonSplitter
from parsers.tokenization import tiktoken_len


class CSharpDocType(TextDocType):
    store_instruction: str = 'Represent the C# code for retrieval'
    query_instruction: str = 'Represent the C# question for retrieving relevant code'

    # FIXME: This is not proper C# parsing!
    parser_kws = dict(
        chunk_size=C.MAX_TOKENS_PER_FRAGMENT,
        length_function=tiktoken_len,
        separators=[
            "\nnamespace ",
            "\npublic class ",
            "\ninternal class ",
            "\npublic static class ",
            "\ninternal static class ",
            "\npublic interface ",
            "\ninternal interface ",
            "\npublic static interface ",
            "\ninternal static interface ",
            "protected ",
            "private ",
            "internal ",
            "public ",
            "\n\n", "\n", " ", ""
        ]
    )

    # def split(self, path: str, text: str) -> Iterator[Fragment]:
    #     for index, chunk in enumerate(self.splitter.split_code(text)):
    #         yield Fragment(str(uuid.uuid4()), path, chunk.lineno, chunk.text, chunk.name)
