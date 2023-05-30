import uuid
from typing import Iterator, Set

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


def walk_children(cursor: TreeCursor, depth=0) -> Iterator[TreeCursor]:
    node: Node = cursor.node
    child_count = node.child_count
    if not child_count:
        return

    cursor.goto_first_child()
    for i in range(child_count):
        if i:
            cursor.goto_next_sibling()
        yield cursor, depth
        yield from walk_children(cursor, depth + 1)

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

        classes: Set[str] = set()
        functions: Set[str] = set()
        methods: Set[str] = set()
        variables: Set[str] = set()
        usages: Set[str] = set()

        for child, depth in walk_children(cursor):
            node: Node = child.node
            # print(f"|{decode(node.text)} |{node.type}|")
            lineno = 1 + node.start_point[0]
            if node.type == 'import_statement' or node.type == 'import_from_statement':
                for sentence in self.splitter.split_text(decode(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'dependency', '', sentence.text)
            elif node.type == 'class_definition':
                name = decode(node.child_by_field_name('name').text)
                classes.add(name)
                for sentence in self.splitter.split_text(decode(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'class', name, sentence.text)
            elif node.type == 'function_definition':
                name = decode(node.child_by_field_name('name').text)
                if depth:
                    methods.add(name)
                else:
                    functions.add(name)
                for sentence in self.splitter.split_text(decode(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'function', name, sentence.text)
            elif node.type == 'expression_statement':
                if node.child_count > 0 and node.children[0].type == 'assignment':
                    text = decode(node.text)
                    name = (text.split('=', 1)[0] if '=' in text else text).split()[0].strip()
                    variables.add(name)
                    for sentence in self.splitter.split_text(decode(node.text)):
                        yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'variable', name, sentence.text)
            elif node.type == 'identifier':
                name = decode(node.text)
                usages.add(name)

        usages -= functions | classes | methods | variables

        summary = [
            f'Summary:',
            f'  Path: {path}',
            f'  Language: Python',
        ]
        if functions:
            summary.append(f"  Functions: {' '.join(functions)}")
        if classes:
            summary.append(f"  Classes: {' '.join(classes)}")
        if methods:
            summary.append(f"  Methods: {' '.join(methods)}")
        if variables:
            summary.append(f"  Variables: {' '.join(variables)}")
        if usages:
            summary.append(f"  Usages: {' '.join(usages)}")

        summary = '\n'.join(summary)
        print(summary)
        yield Fragment(new_uuid(), path, 1, 0, 'summary', '', summary)
