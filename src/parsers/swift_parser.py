from typing import Iterator, Tuple

from tree_sitter import Node

from common.constants import C
from common.tools import tiktoken_len
from parsers.model import Code
from parsers.tree_sitter_parser import TreeSitterParser
from splitters.text_splitter import TextSplitter


class SwiftParser(TreeSitterParser):
    name = 'Swift'
    extensions = ('swift',)
    mime_types = ('text/x-swift',)
    tree_sitter_language_name = 'swift'
    debug = True

    categories = {
        'protocol': 'Protocols',
        'class': 'Classes',
        'function': 'Functions',
        'property': 'Properties',
        'variable': 'Variables',
    }

    def __init__(self) -> None:
        super().__init__()
        self.splitter = TextSplitter(
            chunk_size=C.MAX_TOKENS_PER_FRAGMENT,
            length_function=tiktoken_len,
            separators=(
                ('<', r"^\s+protocol\s+"),
                ('<', r"^\s+class\s+"),
                ('<', r"^\s+func\s+"),
                ('<', r"^\s+while\s+"),
                ('<', r"^\s+for\s+"),
                ('<', r"^\s+if\s+"),
                ('<', r"^\s+else if\s+"),
                ('<', r"^\s+else\s+"),
            )
        )

    def collect_names(self, nodes: Iterator[Tuple[Node, int, int]]):
        for node, lineno, depth in nodes:
            if node.type in ['class_declaration', 'protocol_declaration']:
                for child in node.children:
                    if child.type == 'type_identifier':
                        yield Code(category='class' if node.type == 'class_declaration' else 'protocol', name=child.text, definition=node.text, lineno=lineno, depth=depth)
                    if child.type == 'protocol_function_declaration':
                        for function_child in child.children:
                            if function_child.type == 'simple_identifier':
                                yield Code(category='function', name=function_child.text, definition=node.text, lineno=lineno, depth=depth)

            elif node.type == 'function_declaration':
                for child in node.children:
                    if child.type == 'simple_identifier':
                        yield Code(category='function', name=child.text, definition=node.text, lineno=lineno, depth=depth)

            elif node.type == 'property_declaration':
                for child in node.children:
                    if child.type == 'pattern':
                        for grandchild in child.children:
                            if grandchild.type == 'simple_identifier':
                                yield Code(category='property', name=grandchild.text, definition=node.text, lineno=lineno, depth=depth)

            elif node.type == 'simple_identifier':
                parent = node.parent
                if parent is not None and parent.type == 'assignment':
                    yield Code(category='variable', name=node.text, definition='', lineno=lineno, depth=depth)
