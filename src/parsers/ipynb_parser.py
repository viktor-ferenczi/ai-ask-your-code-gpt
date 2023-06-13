import json
import uuid
from typing import Iterator, Set

from tree_sitter import Parser, Tree, TreeCursor, Node

from common.constants import C
from common.text import decode_replace
from common.tools import tiktoken_len, new_uuid
from common.tree import walk_children
from model.fragment import Fragment
from parsers.base_parser import BaseParser
from splitters.text_splitter import TextSplitter


class PythonNotebookParser(BaseParser):
    name = 'PythonNotebook'
    extensions = ('ipynb',)
    mime_types = ('text/x-ipynb', )
    store_instruction = 'Represent the Python code for retrieval'
    query_instruction = 'Represent the text query for retrieving relevant parts of the code'
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
        content = decode_replace(content).replace('\r\n', '\n').replace('\r', '').strip()
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            print(f'Failed to decode as JSON, ignoring: {path}')
            return

        source = '\n\n'.join(''.join(cell.get('source', [])) for cell in data.get('cells', []) if cell.get('cell_type') == 'code')
        markdown = '\n\n'.join(''.join(cell.get('source', [])) for cell in data.get('cells', []) if cell.get('cell_type') == 'markdown')
        del data

        parser = Parser()
        parser.set_language(self.tree_sitter_language)
        tree: Tree = parser.parse(source.encode('utf-8'))
        cursor: TreeCursor = tree.walk()

        for sentence in self.splitter.split_text(content):
            yield Fragment(new_uuid(), path, sentence.lineno, 0, 'notebook', '', sentence.text)

        for sentence in self.splitter.split_text(source):
            yield Fragment(new_uuid(), path, sentence.lineno, 0, 'python', '', sentence.text)

        for sentence in self.splitter.split_text(markdown):
            yield Fragment(new_uuid(), path, sentence.lineno, 0, 'documentation', '', sentence.text)

        # FIXME: From here redundant code

        classes: Set[str] = set()
        functions: Set[str] = set()
        methods: Set[str] = set()
        variables: Set[str] = set()

        debug = False # b'class PromptTemplate' in content
        for child, depth in walk_children(cursor):
            node: Node = child.node
            if debug and not node.child_count:
                print(f"@{depth}|{node.type}|{decode_replace(node.text)}|")

            lineno = 1 + node.start_point[0]

            if node.type == 'import' or node.type == 'from':
                for sentence in self.splitter.split_text(decode_replace(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'dependency', '', sentence.text)
                continue

            if node.type == 'class' and node.next_sibling:
                name = decode_replace(node.next_sibling.text)
                classes.add(name)
                for sentence in self.splitter.split_text(decode_replace(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'class', name, sentence.text)
                continue

            if node.type == 'def' and node.next_sibling:
                name = decode_replace(node.next_sibling.text)
                if depth:
                    methods.add(name)
                else:
                    functions.add(name)
                for sentence in self.splitter.split_text(decode_replace(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'function', name, sentence.text)
                continue

            if node.type == 'identifier':
                name = decode_replace(node.text)
                variables.add(name)
                continue

            if node.type == 'string_content' or node.type == 'comment':
                if node.text and len(node.text) >= 20:
                    for sentence in self.splitter.split_text(decode_replace(node.text)):
                        yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'documentation', '', sentence.text)
                    continue

        variables = {v for v in variables if len(v) >= 3 or v[:1].isupper()}

        if not functions and not classes and not methods and not variables:
            return

        summary = [
            f'{self.name}: {path}',
        ]
        if functions:
            summary.append(f"  Functions: {' '.join(sorted(functions))}")
        if classes:
            summary.append(f"  Classes: {' '.join(sorted(classes))}")
        if methods:
            summary.append(f"  Methods: {' '.join(sorted(methods))}")
        if variables:
            summary.append(f"  Variables: {' '.join(sorted(variables))}")

        summary = ''.join(f'{line}\n' for line in summary)
        yield Fragment(new_uuid(), path, 1, 0, 'summary', '', summary)
