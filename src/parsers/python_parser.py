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


class PythonParser(BaseParser):
    name = 'Python'
    extensions = ('py', 'bzl', 'scons')
    mime_types = ('text/python', 'text/x-python')
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
        text_content = decode_replace(content).replace('\r\n', '\n').replace('\r', '')
        for sentence in self.splitter.split_text(text_content):
            yield Fragment(new_uuid(), path, sentence.lineno, 0, 'module', '', sentence.text)

        yield from self.iter_python_fragments(path, content)

    def iter_python_fragments(self, path: str, content: bytes) -> Iterator[Fragment]:
        parser = Parser()
        parser.set_language(self.tree_sitter_language)
        tree: Tree = parser.parse(content)
        cursor: TreeCursor = tree.walk()

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

            if node.type == 'import' or node.type == 'from' and node.parent:
                for sentence in self.splitter.split_text(decode_replace(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'dependency', '', sentence.text)
                continue

            if node.type == 'class' and node.next_sibling and node.parent:
                name = decode_replace(node.next_sibling.text)
                classes.add(name)
                for sentence in self.splitter.split_text(decode_replace(node.parent.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'class', name, sentence.text)
                continue

            if node.type == 'def' and node.next_sibling and node.parent:
                name = decode_replace(node.next_sibling.text)
                if depth > 1:
                    methods.add(name)
                else:
                    functions.add(name)
                for sentence in self.splitter.split_text(decode_replace(node.parent.text)):
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

        variables -= classes
        variables -= functions
        variables -= methods
        variables -= {'self', 'set', 'dict', 'list', 'bool', 'int', 'float', 'dir', 'zip', 'isinstance', 'issubclass', 'is', 'super'}
        variables = {v for v in variables if not v.startswith('__') and (len(v) > 3 or v[:1].isupper())}

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
            summary.append(f"  Variables and usages: {' '.join(sorted(variables))}")

        summary = ''.join(f'{line}\n' for line in summary)
        yield Fragment(new_uuid(), path, 1, 0, 'summary', '', summary)
