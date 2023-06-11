from typing import Iterator, Tuple

import tree_sitter

from model.fragment import Fragment


class BaseParser:
    name: str = ''
    extensions: Tuple[str] = ()
    mime_types: Tuple[str] = ()
    store_instruction: str = ''
    query_instruction: str = ''
    tree_sitter_language_name: str = ''
    tree_sitter_language: tree_sitter.Language  # Set automatically

    def __init__(self) -> None:
        assert self.name
        assert self.extensions
        assert self.mime_types
        assert self.store_instruction
        assert self.query_instruction

    @classmethod
    def is_code(cls) -> bool:
        return bool(cls.tree_sitter_language_name)

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        raise NotImplementedError()
