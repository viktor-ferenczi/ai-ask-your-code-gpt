from typing import Iterator, Tuple

import tree_sitter

from model.fragment import Fragment


class BaseParser:
    extensions: Tuple[str] = ()
    mime_types: Tuple[str] = ()
    tree_sitter_language_name: str = ''
    tree_sitter_language: tree_sitter.Language

    @classmethod
    def is_code(cls) -> bool:
        return bool(cls.tree_sitter_language_name)

    def __init__(self) -> None:
        assert self.extensions
        assert self.mime_types

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        raise NotImplementedError()
