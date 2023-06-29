from typing import Iterator, Tuple

from tree_sitter import Node

from common.constants import C
from common.tools import tiktoken_len
from parsers.model import Code
from parsers.tree_sitter_parser import TreeSitterParser
from splitters.text_splitter import TextSplitter


class JavaParser(TreeSitterParser):
    name = 'Java'
    extensions = ('java',)
    mime_types = ('text/x-java',)
    tree_sitter_language_name = 'java'

    categories = {
        'interface': 'Interfaces',
        'class': 'Classes',
        'method': 'Methods',
        'variable': 'Variables',
        'usage': 'Usages'
    }

    def __init__(self) -> None:
        super().__init__()
        self.splitter = TextSplitter(
            chunk_size=C.MAX_TOKENS_PER_FRAGMENT,
            length_function=tiktoken_len,
            separators=(
                ('<', r"^\s+interface\s+"),
                ('<', r"^\s+class\s+"),
                ('<', r"^\s+while\s+"),
                ('<', r"^\s+for\s+"),
                ('<', r"^\s+if\s+"),
                ('<', r"^\s+elif\s+"),
                ('<', r"^\s+else\s+"),
                ('<', r"^\s+try\s+"),
            )
        )

    def collect_names(self, nodes: Iterator[Tuple[Node, int, int]]):
        for node, lineno, depth in nodes:
            if node.type in ['class_declaration', 'interface_declaration']:
                for child in node.children:
                    if child.type == 'identifier':
                        yield Code(category='class' if node.type == 'class_declaration' else 'interface', name=child.text, definition=node.text, lineno=lineno, depth=depth)
                    if child.type == 'method_declaration':
                        for method_child in child.children:
                            if method_child.type == 'identifier':
                                yield Code(category='method', name=method_child.text, definition=node.text, lineno=lineno, depth=depth)

            elif node.type == 'method_declaration':
                for child in node.children:
                    if child.type == 'identifier':
                        yield Code(category='method', name=child.text, definition=node.text, lineno=lineno, depth=depth)

            elif node.type in ['variable_declaration', 'constant_declaration']:
                for child in node.children:
                    if child.type == 'identifier':
                        yield Code(category='variable', name=child.text, definition=node.text, lineno=lineno, depth=depth)

            elif node.type == 'identifier':
                parent = node.parent
                if parent is not None and parent.type in ['assignment_expression', 'update_expression']:
                    yield Code(category='variable', name=node.text, definition='', lineno=lineno, depth=depth)

                elif parent is not None and parent.type == 'method_invocation':
                    for sibling in parent.children:
                        if sibling is not node and sibling.type == 'identifier':
                            yield Code(category='method', name=sibling.text, definition='', lineno=lineno, depth=depth)
