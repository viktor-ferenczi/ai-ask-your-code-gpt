import re
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


class HtmlParser(BaseParser):
    name = 'HTML'
    extensions = ('htm', 'html')
    mime_types = ('text/html',)
    # tree_sitter_language_name = 'html'
    is_code = True

    def __init__(self) -> None:
        super().__init__()
        self.splitter = TextSplitter(
            chunk_size=C.MAX_TOKENS_PER_FRAGMENT,
            length_function=tiktoken_len,
            separators=(
                ('<', r"<head>"),
                ('<', r"<body>"),
                ('<', r"<h1>.*?</h1>"),
                ('<', r"<h2>.*?</h2>"),
                ('<', r"<h3>.*?</h3>"),
                ('<', r"<h4>.*?</h4>"),
                ('<', r"<h5>.*?</h5>"),
                ('<', r"<h6>.*?</h6>"),
                ('<', r"<h7>.*?</h7>"),
                ('<', r"<h8>.*?</h8>"),
                ('<', r"<h9>.*?</h9>"),
                ('<', r"<div>"),
                ('<', r"<p>"),
                ('<', r"<hr\s*/?>"),
                ('<', r"<span>"),
            )
        )

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        # parser = Parser()
        # parser.set_language(self.tree_sitter_language)
        # tree: Tree = parser.parse(content)
        # cursor: TreeCursor = tree.walk()

        text_content = decode_replace(content)
        for sentence in self.splitter.split_text(text_content):
            yield Fragment(new_uuid(), path, sentence.lineno, 0, 'module', '', sentence.text)

        headers: List[str] = []
        rx = re.compile(r"<h([1-9])>(.*?)</h\1>")
        for m in rx.finditer(text_content):
            headers.append(f'{"#" * int(m.group(1))} {m.group(2)}')

        # for child, depth in walk_children(cursor):
        #     node: Node = child.node
        #     if not node.child_count:
        #         print(f"@{depth}|{node.type}|{decode_replace(node.text)}|")
        #     lineno = 1 + node.start_point[0]
        #     continue # TODO: Complete it
        #     if node.type == 'import_statement' or node.type == 'import_from_statement':
        #         for sentence in self.splitter.split_text(decode_replace(node.text)):
        #             yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'dependency', '', sentence.text)
        #     elif node.type == 'class_definition':
        #         name = decode_replace(node.child_by_field_name('name').text)
        #         classes.add(name)
        #         for sentence in self.splitter.split_text(decode_replace(node.text)):
        #             yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'class', name, sentence.text)
        #     elif node.type == 'function_definition':
        #         name = decode_replace(node.child_by_field_name('name').text)
        #         if depth:
        #             methods.add(name)
        #         else:
        #             functions.add(name)
        #         for sentence in self.splitter.split_text(decode_replace(node.text)):
        #             yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'function', name, sentence.text)
        #     elif node.type == 'expression_statement':
        #         if node.child_count > 0 and node.child_count and node.children[0].type == 'assignment':
        #             text = decode_replace(node.text)
        #             name = (text.split('=', 1)[0] if '=' in text else text).split()[0].strip()
        #             variables.add(name)
        #             for sentence in self.splitter.split_text(decode_replace(node.text)):
        #                 yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'variable', name, sentence.text)
        #     elif node.type == 'identifier':
        #         name = decode_replace(node.text)
        #         usages.add(name)

        if not headers:
            return

        summary = [f'{self.name}: {path}'] + headers
        summary = ''.join(f'{line}\n' for line in summary)
        yield Fragment(new_uuid(), path, 1, 0, 'summary', '', summary)
