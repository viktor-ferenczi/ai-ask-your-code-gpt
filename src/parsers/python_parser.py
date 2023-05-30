import uuid
from typing import Iterator

from tree_sitter import Parser, Tree, TreeCursor, Node

from common.constants import C
from common.tools import tiktoken_len
from model.fragment import Fragment
from parsers.base_parser import BaseParser
from splitters.text_splitter import TextSplitter


def new_uuid() -> str:
    return str(uuid.uuid4())


def decode(content: bytes) -> str:
    return content.decode('utf-8', errors='surrogateescape')


def walk_children(cursor: TreeCursor) -> Iterator[TreeCursor]:
    node: Node = cursor.node
    child_count = node.child_count
    if not child_count:
        return

    cursor.goto_first_child()
    for i in range(child_count):
        if i:
            cursor.goto_next_sibling()
        yield cursor
        walk_children(cursor)

    cursor.goto_parent()


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
                ('<', r"^\s+with\s+"),
                ('<', r"^\s+for\s+"),
                ('<', r"^\s+if\s+"),
                ('<', r"^\s+elif\s+"),
                ('<', r"^\s+else\s+"),
                ('<', r"^\s+try\s+"),
            )
        )

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        parser = Parser()
        parser.set_language(self.tree_sitter_language)
        tree: Tree = parser.parse(content)
        cursor: TreeCursor = tree.walk()

        for sentence in self.splitter.split_text(decode(content)):
            yield Fragment(new_uuid(), path, sentence.lineno, 0, 'module', '', sentence.text)

        for child in walk_children(cursor):
            node: Node = child.node
            lineno = 1 + node.start_point[0]
            if node.type == 'import_statement' or node.type == 'import_from_statement':
                for sentence in self.splitter.split_text(decode(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, 0, 'dependency', '', sentence.text)
            elif node.type == 'class_definition':
                name = decode(node.child_by_field_name('name').text)
                for sentence in self.splitter.split_text(decode(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, 0, 'class', name, sentence.text)
            elif node.type == 'function_definition':
                name = decode(node.child_by_field_name('name').text)
                for sentence in self.splitter.split_text(decode(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, 0, 'function', name, sentence.text)
            elif node.type == 'expression_statement':
                if node.child_count > 0 and node.children[0].type == 'assignment':
                    text = decode(node.text)
                    name = text.split('=', 1)[0].strip()
                    for sentence in self.splitter.split_text(decode(node.text)):
                        yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, 0, 'variable', name, sentence.text)
