from typing import Iterator, Tuple

from tree_sitter import Node

from common.constants import C
from common.text import decode_replace
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
        ('macro', 'Macro'),
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
                ('<', r"^\s+class\s+"),
                ('<', r"^\s+while\s+"),
                ('<', r"^\s+for\s+"),
                ('<', r"^\s+if\s+"),
                ('<', r"^\s+elif\s+"),
                ('<', r"^\s+else\s+"),
                ('<', r"^\s+try\s+"),
                ('<', r"^\s+#if\s+"),
                ('<', r"^\s+#ifdef\s+"),
                ('<', r"^\s+#ifndef\s+"),
            )
        )

    def collect_names(self, nodes: Iterator[Tuple[Node, int, int]]):
        for node, lineno, depth in nodes:
            if not node.child_count:
                print(f'@{depth}|{node.type}|{decode_replace(node.text)}')

            if node.type == 'class' and node.parent:
                sibling: Node = node.next_sibling
                while sibling:
                    if sibling.type == '{':
                        yield Name(category='class', name=node.text, definition=node.parent.text, lineno=lineno, depth=depth)
                        break
                    sibling = sibling.next_sibling

            elif node.type == 'identifier':
                category = ''
                sibling: Node = node.next_sibling
                while sibling:
                    if sibling.type == '(':
                        category = 'function'
                        break
                    sibling = sibling.next_sibling

                if category == 'function':
                    if node.prev_sibling and node.prev_sibling.type == '::' and node.prev_sibling.prev_sibling and node.prev_sibling.prev_sibling.type == 'namespace_identifier':
                        yield Name(category='method', name=node.prev_sibling.prev_sibling.text + b'::' + node.text, definition=node.prev_sibling.prev_sibling.text, lineno=lineno, depth=depth)
                    else:
                        for child in node.parent.children:
                            if child.type == 'class':
                                category = 'method'
                                break
                        yield Name(category=category, name=node.text, definition=node.parent.text, lineno=lineno, depth=depth)

                elif node.prev_sibling and node.prev_sibling.type == '#define':
                    yield Name(category='macro', name=node.text, definition=node.prev_sibling.text, lineno=lineno, depth=depth)

                elif node.prev_sibling and node.prev_sibling.type == 'class':
                    yield Name(category='class', name=node.text, definition=node.prev_sibling.text, lineno=lineno, depth=depth)

                elif node.prev_sibling and node.prev_sibling.type == '=':
                    yield Name(category='variable', name=node.text, definition=node.text, lineno=lineno, depth=depth)

                elif node.prev_sibling and node.prev_sibling.type == '::' and node.prev_sibling.prev_sibling and node.prev_sibling.prev_sibling.type == 'namespace_identifier':
                    yield Name(category='method', name=node.prev_sibling.prev_sibling.text + b'::' + node.text, definition=node.prev_sibling.prev_sibling.text, lineno=lineno, depth=depth)

                else:
                    yield Name(category='variable', name=node.text, definition='', lineno=lineno, depth=depth)

            elif node.type == 'field_identifier' and node.parent:
                category = 'field'
                sibling: Node = node.next_sibling
                while sibling:
                    if sibling.type == '(':
                        category = 'method'
                        break
                    sibling = sibling.next_sibling
                yield Name(category=category, name=node.text, definition=node.parent.text, lineno=lineno, depth=depth)

            elif node.type == 'type_identifier':
                yield Name(category='class', name=node.text, definition='', lineno=lineno, depth=depth)
