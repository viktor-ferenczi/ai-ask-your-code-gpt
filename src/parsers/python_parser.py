import uuid
from typing import Iterator, Set

from tree_sitter import Parser, Tree, TreeCursor, Node

from common.constants import C
from common.text import decode_escape
from common.tools import tiktoken_len, new_uuid
from common.tree import walk_children
from model.fragment import Fragment
from parsers.base_parser import BaseParser
from splitters.text_splitter import TextSplitter


class PythonParser(BaseParser):
    name = 'Python'
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

        for sentence in self.splitter.split_text(decode_escape(content)):
            yield Fragment(new_uuid(), path, sentence.lineno, 0, 'module', '', sentence.text)

        classes: Set[str] = set()
        functions: Set[str] = set()
        methods: Set[str] = set()
        variables: Set[str] = set()
        usages: Set[str] = set()

        for child, depth in walk_children(cursor):
            node: Node = child.node
            # if not node.child_count:
            #     print(f"|{decode_escape(node.text)} |{node.type}|")
            lineno = 1 + node.start_point[0]
            if node.type == 'import_statement' or node.type == 'import_from_statement':
                for sentence in self.splitter.split_text(decode_escape(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'dependency', '', sentence.text)
            elif node.type == 'class_definition':
                name = decode_escape(node.child_by_field_name('name').text)
                classes.add(name)
                for sentence in self.splitter.split_text(decode_escape(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'class', name, sentence.text)
            elif node.type == 'function_definition':
                name = decode_escape(node.child_by_field_name('name').text)
                if depth:
                    methods.add(name)
                else:
                    functions.add(name)
                for sentence in self.splitter.split_text(decode_escape(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'function', name, sentence.text)
            elif node.type == 'expression_statement':
                if node.child_count > 0 and node.children[0].type == 'assignment':
                    text = decode_escape(node.text)
                    name = (text.split('=', 1)[0] if '=' in text else text).split()[0].strip()
                    variables.add(name)
                    for sentence in self.splitter.split_text(decode_escape(node.text)):
                        yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'variable', name, sentence.text)
            elif node.type == 'identifier':
                name = decode_escape(node.text)
                usages.add(name)

        usages -= functions | classes | methods | variables

        variables -= {v for v in variables if len(v) < 3 and not v[:1].isupper()}
        usages -= {v for v in usages if len(v) < 3 and not v[:1].isupper()}

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
        if usages:
            summary.append(f"  Usages: {' '.join(sorted(usages))}")

        summary = ''.join(f'{line}\n' for line in summary)
        yield Fragment(new_uuid(), path, 1, 0, 'summary', '', summary)
