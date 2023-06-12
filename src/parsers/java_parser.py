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
            names = name_map.get(name.category)
            if names is None:
                names = name_map[name.category] = set()
            names.add(name)

        usages = set()
        for names in name_map.values():
            usages.update(name for name in names if not name.definition)
            names[:] = [name for name in names if name.definition]
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
            if names:
                names = [name.name for name in names]
                summary.append(f"  {label}: {' '.join(sorted(names))}\n")

        summary = ''.join(summary)
        yield Fragment(new_uuid(), path, 1, 0, 'summary', '', summary)

    def collect_names(self, nodes: Iterator[Node]):
        for node in nodes:
            if node.type in ('class_declaration', 'interface_declaration'):
                yield Name(category=node.type.split('_')[0],
                           name=node.child_by_field_name('identifier').text,
                           definition=True)
            elif node.type == 'method_declaration':
                yield Name(category='method',
                           name=node.child_by_field_name('identifier').text,
                           definition=True)
            elif node.type in ('local_variable_declaration', 'field_declaration'):
                for declarator in node.child_by_field_name('declarators').children:
                    yield Name(category='variable',
                               name=declarator.child_by_field_name('identifier').text,
                               definition=True)
            elif node.type == 'identifier':
                parent = node.parent
                if parent.type in ('class_declaration', 'interface_declaration'):
                    yield Name(category=parent.type.split('_')[0],
                               name=node.text,
                               definition=False)
                elif parent.type == 'method_declaration':
                    yield Name(category='method',
                               name=node.text,
                               definition=False)
                elif parent.type in ('local_variable_declaration', 'field_declaration'):
                    yield Name(category='variable',
                               name=node.text,
                               definition=False)
