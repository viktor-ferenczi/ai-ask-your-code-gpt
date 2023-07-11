from typing import Iterator, Set

from tree_sitter import Parser, Tree, TreeCursor, Node

from common.constants import C
from common.text import decode_normalize
from common.tools import tiktoken_len, new_uuid
from common.tree import walk_children
from model.fragment import Fragment
from parsers.base_parser import BaseParser
from splitters.text_splitter import TextSplitter


class JavaScriptParser(BaseParser):
    name = 'JavaScript'
    extensions = ('js',)
    mime_types = ('text/javascript',)
    tree_sitter_language_name = 'javascript'
    is_code = True

    def __init__(self) -> None:
        super().__init__()
        self.splitter = TextSplitter(
            chunk_size=C.MAX_TOKENS_PER_FRAGMENT,
            length_function=tiktoken_len,
            separators=(
                ('<', r"^.*?function\s+"),
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

        functions: Set[str] = set()
        variables: Set[str] = set()
        usages: Set[str] = set()

        debug = False
        for child, depth in walk_children(cursor):
            node: Node = child.node
            if debug and not node.child_count:
                print(f"@{depth}|{node.type}|{decode_normalize(node.text)}|")
            lineno = 1 + node.start_point[0]
            if node.type == 'import_statement':
                for sentence in self.splitter.split_text(decode_normalize(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'dependency', '', sentence.text, tiktoken_len(sentence.text))
            elif (node.type == 'function' and
                  node.next_sibling is not None and
                  node.next_sibling.type == 'identifier'):
                name = decode_normalize(node.next_sibling.text)
                functions.add(name)
                for sentence in self.splitter.split_text(decode_normalize(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'function', name, sentence.text, tiktoken_len(sentence.text))
            elif (node.type == 'identifier' and
                  node.next_sibling is not None and
                  node.next_sibling.type == '=' and
                  node.next_sibling.next_sibling is not None and
                  node.next_sibling.next_sibling.type == 'function'):
                name = decode_normalize(node.text)
                functions.add(name)
                for sentence in self.splitter.split_text(decode_normalize(node.text)):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'function', name, sentence.text, tiktoken_len(sentence.text))
            elif (node.type == 'variable_declarator' and
                  node.child_count and
                  node.children[0].type == 'identifier'):
                text = decode_normalize(node.text)
                name = decode_normalize(node.children[0].text)
                variables.add(name)
                for sentence in self.splitter.split_text(text):
                    yield Fragment(new_uuid(), path, lineno + sentence.lineno - 1, depth, 'variable', name, sentence.text, tiktoken_len(sentence.text))
            elif node.type == 'identifier':
                name = decode_normalize(node.text)
                usages.add(name)

        usages -= functions | variables

        variables.discard('$')

        variables -= {v for v in variables if len(v) < 3 and not v[:1].isupper()}
        usages -= {v for v in usages if len(v) < 3 and not v[:1].isupper()}

        summary = []
        if functions:
            summary.append(f"  Functions: {' '.join(sorted(functions))}")
        if variables:
            summary.append(f"  Variables: {' '.join(sorted(variables))}")
        if usages:
            summary.append(f"  Usages: {' '.join(sorted(usages))}")

        summary = ''.join(f'{line}\n' for line in summary)
        yield Fragment(new_uuid(), path, 1, 0, 'summary', '', summary, tiktoken_len(summary))
