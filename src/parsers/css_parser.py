import uuid
from typing import Iterator, Set, List

from tree_sitter import Parser, Tree, TreeCursor, Node

from common.constants import C
from common.text import decode_replace
from common.tools import tiktoken_len, new_uuid
from common.tree import walk_children
from model.fragment import Fragment
from parsers.base_parser import BaseParser
from splitters.text_splitter import TextSplitter


class CssParser(BaseParser):
    name = 'CSS'
    extensions = ('css',)
    mime_types = ('text/css',)
    store_instruction = 'Represent the CSS document for retrieval'
    query_instruction = 'Represent the text query for retrieving relevant parts of the document'
    tree_sitter_language_name = 'css'

    def __init__(self) -> None:
        super().__init__()
        self.splitter = TextSplitter(
            chunk_size=C.MAX_TOKENS_PER_FRAGMENT,
            length_function=tiktoken_len,
            separators=(
                ('<', r"^.*?{"),
            )
        )

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        parser = Parser()
        parser.set_language(self.tree_sitter_language)
        tree: Tree = parser.parse(content)
        cursor: TreeCursor = tree.walk()

        for sentence in self.splitter.split_text(decode_replace(content)):
            yield Fragment(new_uuid(), path, sentence.lineno, 0, 'module', '', sentence.text)

        classes: List[str] = []
        class_set: Set[str] = set()

        for child, depth in walk_children(cursor):
            node: Node = child.node
            # if not node.child_count:
            #     print(f"@{depth}|{decode_replace(node.text)}|{node.type}|")
            lineno = 1 + node.start_point[0]
            if node.type == 'class_name':
                name = decode_replace(node.text)
                if name not in class_set:
                    classes.append(name)
                    class_set.add(name)
                for sentence in self.splitter.split_text(decode_replace(node.parent.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'class', name, sentence.text)

        if not classes:
            return

        summary = [
            f'{self.name}: {path}',
        ]
        summary.append(f"  Classes: {' '.join(classes)}")
        summary = ''.join(f'{line}\n' for line in summary)
        yield Fragment(new_uuid(), path, 1, 0, 'summary', '', summary)
