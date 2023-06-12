from typing import List, Tuple, Iterator

from tree_sitter import Parser, Tree, TreeCursor

from common.text import decode_replace
from common.tools import new_uuid
from common.tree import walk_nodes
from model.fragment import Fragment
from parsers import BaseParser


class TreeSitterParser(BaseParser):
    categories: List[Tuple[str, str]] = []

    def __init__(self) -> None:
        super().__init__()
        assert self.categories

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        parser = Parser()
        parser.set_language(self.tree_sitter_language)
        tree: Tree = parser.parse(content)
        cursor: TreeCursor = tree.walk()

        for sentence in self.splitter.split_text(decode_replace(content)):
            yield Fragment(new_uuid(), path, sentence.lineno, 0, 'module', '', sentence.text)

        name_map = {}
        for name in self.collect_names(walk_nodes(cursor)):
            if isinstance(name.name, bytes):
                name.name = decode_replace(name.name)

            if isinstance(name.definition, bytes):
                name.definition = decode_replace(name.definition)

            names = name_map.get(name.category)
            if names is None:
                names = name_map[name.category] = set()

            names.add(name)

        usages = set()
        for key in name_map:
            names = name_map[key]
            usages.update(name for name in names if not name.definition)
            name_map[key] = sorted((name for name in names if name.definition), key=lambda n: n.name)
        name_map['usage'] = sorted(usages, key=lambda n: n.name)

        summary = [
            f'{self.name}: {path}\n',
        ]

        for key, label in self.categories:
            names = name_map.get(key)
            if not names:
                continue

            names = [name for name in names if len(name.name) >= 3 or name.name[:1].isupper()]
            if not names:
                continue

            for name in names:
                if name.definition:
                    yield Fragment(
                        uuid=new_uuid(),
                        path=path,
                        lineno=name.lineno,
                        depth=name.depth,
                        type=name.category,
                        name=name.name,
                        text=name.definition,
                    )

            summary.append(f"  {label}: {' '.join(name.name for name in names)}\n")

        summary = ''.join(summary)
        yield Fragment(new_uuid(), path, 1, 0, 'summary', '', summary)
