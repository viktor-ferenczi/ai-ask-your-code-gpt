import os
from typing import Optional, Type

from magic import Magic
from tree_sitter import Language

from parsers.base_parser import BaseParser
from parsers.markdown_parser import MarkdownParser
from parsers.python_parser import PythonParser
from parsers.text_parser import TextParser

PARSERS = (
    TextParser,
    MarkdownParser,
    PythonParser,
)

PARSERS_BY_EXTENSION = {}
PARSERS_BY_MIME_TYPE = {}


def register_parsers():
    for parser_cls in PARSERS:
        assert issubclass(parser_cls, BaseParser)
        for extension in parser_cls.extensions:
            PARSERS_BY_EXTENSION[extension] = parser_cls
        for mime_type in parser_cls.mime_types:
            PARSERS_BY_MIME_TYPE[mime_type] = parser_cls


register_parsers()
del register_parsers

TREE_SITTER_DIR = os.path.normpath(os.environ.get('TREE_SITTER_DI', os.path.expanduser('~/.tree-sitter')))
TREE_SITTER_BUILD_DIR = os.path.join(TREE_SITTER_DIR, 'build')
TREE_SITTER_REPOS_DIR = os.path.join(TREE_SITTER_DIR, 'repos')
TREE_SITTER_LIBRARY = os.path.join(TREE_SITTER_BUILD_DIR, 'my-languages.so')

Language.build_library(
    TREE_SITTER_LIBRARY,
    [
        os.path.join(TREE_SITTER_REPOS_DIR, f'tree-sitter-{parser_cls.tree_sitter_language_name}')
        for parser_cls in PARSERS
        if parser_cls.tree_sitter_language_name
    ]
)


def set_tree_sitter_languages():
    for parser_cls in PARSERS:
        if parser_cls.tree_sitter_language_name:
            parser_cls.tree_sitter_language = Language(TREE_SITTER_LIBRARY, parser_cls.tree_sitter_language_name)


set_tree_sitter_languages()
del set_tree_sitter_languages

MAGIC = Magic(mime=True)


def detect(path: str, content: Optional[bytes] = None) -> Optional[Type[BaseParser]]:
    parser_cls = None

    if '.' in path:
        extension = path.rsplit('.', 1)[-1].lower()
        parser_cls = PARSERS_BY_EXTENSION.get(extension)

    if parser_cls is None and content is not None:
        mime_type = MAGIC.from_buffer(content)
        parser_cls = PARSERS_BY_MIME_TYPE.get(mime_type)

    return parser_cls
