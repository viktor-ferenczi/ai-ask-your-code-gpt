import os.path
from typing import Tuple, Iterator, Dict, Optional, Set, List

from tree_sitter import Parser, Tree, TreeCursor, Node

from common.constants import C
from common.text import decode_normalize, normalize
from common.tools import new_uuid, tiktoken_len
from common.tree import walk_nodes
from model.fragment import Fragment
from parsers.model import Code
from parsers.registrations import BaseParser
from splitters.text_splitter import TextSplitter


class TreeSitterParser(BaseParser):
    categories: Dict[str, str] = {}
    is_code = True
    debug = False

    def __init__(self) -> None:
        super().__init__()
        assert self.categories
        self.splitter: Optional[TextSplitter] = None
        self.unhandled: Dict[str, Tuple[int, str]] = {}

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        assert self.splitter

        parser = Parser()
        parser.set_language(self.tree_sitter_language)
        tree: Tree = parser.parse(content)
        cursor: TreeCursor = tree.walk()

        name_map: Dict[str, Set[Code]] = {name: set() for name in self.categories}

        debug_file = None
        if self.debug:
            debug_path = os.path.join(C.DATA_DIR, 'debug', path.lstrip('/') + '.log')
            print(f'Tree-Sitter parser debug log: {debug_path}')
            debug_dir = os.path.dirname(debug_path)
            os.makedirs(debug_dir, exist_ok=True)
            debug_file = open(debug_path, 'wt', encoding='utf-8')

        try:
            self.unhandled.clear()

            iter_nodes = walk_nodes(cursor, debug=self.debug, debug_file=debug_file)

            for code in self.collect_names(iter_nodes):
                assert isinstance(code, Code), repr(code)

                if isinstance(code.name, bytes):
                    code.name = decode_normalize(code.name)
                code.name = normalize(code.name).strip()

                if isinstance(code.definition, bytes):
                    code.definition = decode_normalize(code.definition)
                code.definition = normalize(code.definition).strip()

                name_map[code.category].add(code)

            if self.debug and self.unhandled:
                print('', file=debug_file)
                for code in sorted(self.unhandled):
                    lineno, text = self.unhandled[code]
                    print(f'UNHANDLED #{lineno:05d} [{code}] {text}', file=debug_file)
        finally:
            if debug_file:
                debug_file.close()

        usages: Set[Code] = name_map.pop('usage', set())
        for key in name_map:
            codes = name_map[key]
            non_definitions = {name for name in codes if not name.definition}
            usages.update(non_definitions)
            name_map[key] -= non_definitions

        summary = []

        for key, codes in name_map.items():
            assert key in self.categories, key
            if not codes:
                continue

            codes: List[Code] = [code for code in codes if len(code.name) >= 3 or code.name[:1].isupper()]
            if not codes:
                continue

            for code in codes:
                if code.definition:
                    lineno = code.lineno
                    for segment in self.splitter.split_text(code.definition):
                        yield Fragment(
                            uuid=new_uuid(),
                            path=path,
                            lineno=lineno,
                            depth=code.depth,
                            type=code.category,
                            name=code.name,
                            text=segment.text,
                            tokens=tiktoken_len(segment.text),
                        )
                        lineno += segment.text.count('\n')

            label = self.categories[key]
            summary.append(f"  {label}: {' '.join(sorted({name.name for name in codes}))}\n")

        if usages:
            summary.append(f"  Usages: {' '.join(sorted({name.name for name in usages}))}\n")

        summary = ''.join(summary)
        yield Fragment(new_uuid(), path, 1, 0, 'summary', '', summary, tiktoken_len(summary))

    def collect_names(self, nodes: Iterator[Tuple[Node, int, int]]) -> Iterator[Code]:
        raise NotImplementedError()
