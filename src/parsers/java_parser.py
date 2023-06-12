from typing import Iterator

from tree_sitter import Parser, Tree, TreeCursor, Node

from common.constants import C
from common.text import decode_replace
from common.tools import tiktoken_len, new_uuid
from common.tree import walk_nodes
from model.fragment import Fragment
from parsers.base_parser import BaseParser
from parsers.model import Name
from splitters.text_splitter import TextSplitter


class JavaParser(BaseParser):
    name = 'Java'
    extensions = ('java',)
    mime_types = ('text/x-java',)
    store_instruction = 'Represent the Java code for retrieval'
    query_instruction = 'Represent the text query for retrieving relevant parts of the code'
    tree_sitter_language_name = 'java'

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

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        parser = Parser()
        parser.set_language(self.tree_sitter_language)
        tree: Tree = parser.parse(content)
        cursor: TreeCursor = tree.walk()

        for sentence in self.splitter.split_text(decode_replace(content)):
            yield Fragment(new_uuid(), path, sentence.lineno, 0, 'module', '', sentence.text)

        name_map = {}
        for name in self.collect_names(walk_nodes(cursor)):
            name.name = decode_replace(name.name)
            names = name_map.get(name.category)
            if names is None:
                names = name_map[name.category] = set()
            names.add(name)

        usages = set()
        for key in name_map:
            names = name_map[key]
            usages.update(name for name in names if not name.definition)
            name_map[key] = [name for name in names if name.definition]
        name_map['usage'] = usages

        summary = [
            f'{self.name}: {path}\n',
        ]
        table = [
            ('interface', 'Interfaces'),
            ('class', 'Classes'),
            ('method', 'Methods'),
            ('variable', 'Variables'),
            ('usage', 'Usages'),
        ]
        for key, label in table:
            names = name_map.get(key)
            if not names:
                continue
            names = [name.name for name in names]
            names = [name for name in names if len(name) >= 3 or name[:1].isupper()]
            if names:
                summary.append(f"  {label}: {' '.join(sorted(names))}\n")

        summary = ''.join(summary)
        yield Fragment(new_uuid(), path, 1, 0, 'summary', '', summary)

    def collect_names(self, nodes: Iterator[Node]):
        for node in nodes:
            if node.type in ['class_declaration', 'interface_declaration']:
                for child in node.children:
                    if child.type == 'identifier':
                        yield Name('class' if node.type == 'class_declaration' else 'interface', child.text, True)
                    if child.type == 'method_declaration':
                        for method_child in child.children:
                            if method_child.type == 'identifier':
                                yield Name('method', method_child.text, True)

            elif node.type == 'method_declaration':
                for child in node.children:
                    if child.type == 'identifier':
                        yield Name('method', child.text, True)

            elif node.type in ['variable_declaration', 'constant_declaration']:
                for child in node.children:
                    if child.type == 'identifier':
                        yield Name('variable', child.text, True)

            elif node.type == 'identifier':
                parent = node.parent
                if parent is not None and parent.type in ['assignment_expression', 'update_expression']:
                    yield Name('variable', node.text, False)

                elif parent is not None and parent.type == 'method_invocation':
                    for sibling in parent.children:
                        if sibling is not node and sibling.type == 'identifier':
                            yield Name('method', sibling.text, False)
