from typing import Iterator, Tuple

from tree_sitter import Node

from common.constants import C
from common.tools import tiktoken_len
from parsers.model import Name
from parsers.tree_sitter_parser import TreeSitterParser
from splitters.text_splitter import TextSplitter


class CppParser(TreeSitterParser):
    name = 'C++'
    extensions = ('c', 'cpp', 'c++', 'h', 'hpp', 'h++')
    mime_types = ('text/c', 'text/x-cpp', 'text/x-cplusplus')
    store_instruction = 'Represent the C++ code for retrieval'
    query_instruction = 'Represent the text query for retrieving relevant parts of the code'
    tree_sitter_language_name = 'cpp'

    categories = [
        ('namespace', 'Namespaces'),
        ('interface', 'Interfaces'),
        ('class', 'Classes'),
        ('method', 'Methods'),
        ('variable', 'Variables'),
        ('usage', 'Usages'),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.splitter = TextSplitter(
            chunk_size=C.MAX_TOKENS_PER_FRAGMENT,
            length_function=tiktoken_len,
            separators=(
                ('<', r"^\s+namespace\s+"),
                ('<', r"^\s+interface\s+"),
                ('<', r"^\s+class\s+"),
                ('<', r"^\s+using\s+"),
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
            if node.type in ['namespace', 'class', 'function', 'method', 'variable']:
                if node.type in ['namespace', 'class']:
                    for child in node.children:
                        if child.type == 'identifier':
                            yield Name(category=node.type, name=child.text, definition=node.text, lineno=lineno, depth=depth)
                elif node.type in ['function', 'method']:
                    for child in node.children:
                        if child.type == 'identifier':
                            yield Name(category=node.type, name=child.text, definition=node.text, lineno=lineno, depth=depth)
                        if child.type == 'call_expression':
                            for grandchild in child.children:
                                if grandchild.type == 'identifier':
                                    yield Name(category=node.type, name=grandchild.text, definition='', lineno=lineno, depth=depth)
                elif node.type == 'variable':
                    for child in node.children:
                        if child.type == 'identifier':
                            if child.prev_sibling and child.prev_sibling.type == 'type':
                                yield Name(category=node.type, name=child.text, definition=node.text, lineno=lineno, depth=depth)
                            else:
                                yield Name(category=node.type, name=child.text, definition='', lineno=lineno, depth=depth)
