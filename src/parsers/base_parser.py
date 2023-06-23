from typing import Iterator, Tuple

import tree_sitter

from model.fragment import Fragment


class BaseParser:
    name: str = ''
    extensions: Tuple[str] = ()
    mime_types: Tuple[str] = ()
    tree_sitter_language_name: str = ''
    tree_sitter_subdir: Tuple[str] = ()
    tree_sitter_language: tree_sitter.Language  # Set automatically
    is_code = False

    def __init__(self) -> None:
        assert self.name
        assert self.extensions
        assert self.mime_types

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:
        raise NotImplementedError()
