from typing import Iterator, Tuple

from tree_sitter import Node

from common.constants import C
from common.tools import tiktoken_len
from parsers.model import Name
from parsers.tree_sitter_parser import TreeSitterParser
from splitters.text_splitter import TextSplitter


class CppParser(TreeSitterParser):
    name = 'C++'
    extensions = ('c', 'cc', 'cpp', 'c++', 'h', 'hh', 'hpp', 'h++')
    mime_types = ('text/x-c',)
    tree_sitter_language_name = 'cpp'
    debug = True

    categories = {
        'class': 'Classes',
        'struct': 'Structs',
        'enum': 'Enums',
        'union': 'Unions',
        'typedef': 'Typedefs',
        'macro': 'Macros',
        'function': 'Functions',
        'method': 'Methods',
        'field': 'Fields',
        'variable': 'Variables',
        'using': 'Using',
        'namespace': 'Namespaces',
        'usage': 'Usages',
    }

    def __init__(self) -> None:
        super().__init__()
        self.splitter = TextSplitter(
            chunk_size=C.MAX_TOKENS_PER_FRAGMENT,
            length_function=tiktoken_len,
            separators=(
                ('<', r"^\s+namespace\s+"),
                ('<', r"^\s+using\s+"),
                ('<', r"^\s+interface\s+"),
                ('<', r"^\s+enum class\s+"),
                ('<', r"^\s+enum\s+"),
                ('<', r"^\s+union\s+"),
                ('<', r"^\s+typedef\s+"),
                ('<', r"^\s+struct\s+"),
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

    def collect_names(self, nodes: Iterator[Tuple[Node, int, int]]) -> Iterator[Name]:
        def simple(category: str, identifier_type: str, definition: str):
            for child in node.children:
                if child.type == identifier_type:
                    yield Name(category=category, name=child.text, definition=node.text, lineno=lineno, depth=depth)
                    return

        def two_level(category: str, declarator_type: str, identifier_type: str, definition: str):
            for child in node.children:
                if child.type == declarator_type:
                    for grandchild in child.children:
                        if grandchild.type == identifier_type:
                            yield Name(category=category, name=grandchild.text, definition=node.text, lineno=lineno, depth=depth)
                            return

        for node, lineno, depth in nodes:
            if node.type in (
                    'identifier',
                    'type_identifier',
                    'field_identifier',
                    'qualified_identifier',
                    'namespace_identifier'):
                yield from simple('usage', 'identifier', '')
            elif node.type == 'declaration':
                yield from simple('variable', 'identifier', node.text)
                yield from simple('method', 'qualified_identifier', node.text)
            elif node.type == 'function_declarator':
                yield from simple('function', 'identifier', node.text)
            elif node.type == 'function_definition':
                yield from two_level('function', 'function_declarator', 'identifier', node.text)
            elif node.type == 'field_declaration':
                yield from simple('field', 'field_identifier', node.text)
            elif node.type == 'type_definition':
                yield from simple('typedef', 'type_identifier', node.text)
            elif node.type == 'struct_specifier':
                yield from simple('struct', 'type_identifier', node.text)
            elif node.type == 'class_specifier':
                yield from simple('class', 'type_identifier', node.text)
            elif node.type == 'union_specifier':
                yield from simple('union', 'type_identifier', node.text)
            elif node.type == 'enum_specifier':
                yield from simple('enum', 'type_identifier', node.text)
            elif node.type in ('preproc_def', 'preproc_function_def'):
                yield from simple('macro', 'identifier', node.text)
            elif node.type == 'using_declaration':
                yield from simple('using', 'identifier', node.text)
            elif node.type == 'namespace_definition':
                for child in node.children:
                    if child.type == 'namespace_identifier':
                        yield Name(category='namespace', name=child.text, definition=f'namespace {child.text} {{...}}', lineno=lineno, depth=depth)
            elif node.type not in self.unhandled:
                self.unhandled[node.type] = (lineno, node.text)
