import json
from typing import Iterator

from common.constants import C
from common.text import decode_normalize
from common.tools import tiktoken_len, new_uuid
from model.fragment import Fragment
from splitters.text_splitter import TextSplitter
from .python_parser import PythonParser


class PythonNotebookParser(PythonParser):
    name = 'PythonNotebook'
    extensions = ('ipynb',)
    mime_types = ('text/x-ipynb',)
    tree_sitter_language_name = 'python'
    is_code = True

    def __init__(self) -> None:
        super().__init__()
        self.splitter = TextSplitter(
            chunk_size=C.MAX_TOKENS_PER_FRAGMENT,
            length_function=tiktoken_len,
            separators=(
                ('<', r"^\s+class\s+"),
                ('<', r"^\s+def\s+"),
                ('<', r"^\s+with\s+"),
                ('<', r"^\s+while\s+"),
                ('<', r"^\s+for\s+"),
                ('<', r"^\s+if\s+"),
                ('<', r"^\s+elif\s+"),
                ('<', r"^\s+else\s+"),
                ('<', r"^\s+try\s+"),
            )
        )

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        if '/.ipynb_checkpoints' in path:
            return

        text_content = decode_normalize(content)

        for sentence in self.splitter.split_text(text_content):
            yield Fragment(new_uuid(), path, sentence.lineno, 0, 'notebook', '', sentence.text)

        try:
            data = json.loads(text_content)
        except json.JSONDecodeError:
            print(f'Failed to decode as JSON, indexing it as text only: {path}')
            return

        source = '\n\n'.join(''.join(cell.get('source', [])) for cell in data.get('cells', []) if cell.get('cell_type') == 'code')
        markdown = '\n\n'.join(''.join(cell.get('source', [])) for cell in data.get('cells', []) if cell.get('cell_type') == 'markdown')
        del data

        for sentence in self.splitter.split_text(source):
            yield Fragment(new_uuid(), path, sentence.lineno, 0, 'python', '', sentence.text)

        for sentence in self.splitter.split_text(markdown):
            yield Fragment(new_uuid(), path, sentence.lineno, 0, 'documentation', '', sentence.text)
        del markdown

        yield from self.iter_python_fragments(path, source.encode('utf-8'))
