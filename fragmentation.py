import os
import re
import uuid
from dataclasses import dataclass
from typing import List, Optional

import libcst as cst
import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter
from libcst.metadata import MetadataWrapper, PositionProvider

SOURCE_DIR = r'C:\Dev\LLM\Source\viktor-ferenczi-dblayer'

CATEGORY_MODULE = 'module'
CATEGORY_FUNCTION = 'function'
CATEGORY_CLASS = 'class'

LANGUAGE_TEXT = 'text'
LANGUAGE_PYTHON = 'python'
LANGUAGE_UNKNOWN = 'unknown'
IGNORE = 'ignore'

EXTENSIONS = {
    '.md': LANGUAGE_TEXT,
    '.txt': LANGUAGE_TEXT,
    '.py': LANGUAGE_PYTHON,
    '.sh': LANGUAGE_UNKNOWN,
    '.cs': LANGUAGE_UNKNOWN,
    '.c': LANGUAGE_UNKNOWN,
    '.h': LANGUAGE_UNKNOWN,
    '.cpp': LANGUAGE_UNKNOWN,
    '.hpp': LANGUAGE_UNKNOWN,
    '.java': LANGUAGE_UNKNOWN,
    '.js': LANGUAGE_UNKNOWN,
    '.css': LANGUAGE_UNKNOWN,
    '.html': LANGUAGE_UNKNOWN,
    '.rust': LANGUAGE_UNKNOWN,
    '.zig': LANGUAGE_UNKNOWN,
    '.sql': LANGUAGE_UNKNOWN,
    '.pyc': IGNORE,
    '.pyo': IGNORE,
    '.log': IGNORE,
    '.bak': IGNORE,
    '~': IGNORE,
    '.svnignore': IGNORE,
    '.gitignore': IGNORE,
    '.hgignore': IGNORE,
    '.com': IGNORE,
    '.exe': IGNORE,
    '.dll': IGNORE,
    '.lib': IGNORE,
    '.so': IGNORE,
    '.a': IGNORE,
    '.o': IGNORE,
}


@dataclass
class Chunk:
    id: str
    index: int
    fragment: str
    embed: List[float]
    inserted: bool

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id


@dataclass
class Doc:
    source: str
    title: str
    text: str
    chunks: List[Chunk]

    def __hash__(self):
        return hash(self.text)

    def __eq__(self, other):
        return self.text == other.text


tokenizer = tiktoken.encoding_for_model('gpt-3.5-turbo')


# create the length function
def tiktoken_len(text):
    tokens = tokenizer.encode(
        text,
        disallowed_special=()
    )
    return len(tokens)


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0,
    length_function=tiktoken_len,
    separators=["\n\n", "\n"]
)


@dataclass
class Block:
    project_id: str
    path: str
    lineno: int
    language: str
    name: str
    category: str
    fragment: str

    def __str__(self) -> str:
        return f'Block({self.project_id!r}, {self.path!r}, {self.lineno}, {self.language!r}, {self.name!r}, {self.category!r})'

    @property
    def meta(self) -> str:
        return f'''\
path: {self.path}
lineno: {self.lineno}
language: {self.language}
name: {self.name}
category: {self.category}
'''


class Source:
    def __init__(self, project_id: str, path: str, language: str, text: str) -> None:
        super().__init__()
        self.project_id: str = project_id
        self.path: str = path
        self.language: str = language
        self.text: str = f'\n{text.rstrip()}\n'

        self.blocks: List[Block] = []
        self.errors: List[str] = []
        self.find_blocks()

    def __str__(self) -> str:
        return f'Source({self.path!r}, {self.language!r})'

    __repr__ = __str__

    def find_blocks(self):
        if self.language == LANGUAGE_TEXT:
            self.find_text_blocks()
        elif self.language == LANGUAGE_PYTHON:
            self.find_python_blocks()
        elif self.language == LANGUAGE_UNKNOWN:
            self.errors.append('Could not detect the programming language (unsupported or unknown)')
            self.find_text_blocks()
        else:
            raise ValueError(f'Invalid source language: {self.language}')

    def find_python_blocks(self):
        try:
            self.find_python_blocks_with_libcst()
        except SyntaxError as e:
            print(f'FAILED TO PARSE PYTHON CODE: [{e.__class__.__name__}] {e}')
            self.errors.append(f'Failed to parse as Python 3 source code, a regexp based parser was used instead')
            self.find_python_blocks_with_regexps()

    def find_python_blocks_with_libcst(self):
        module = MetadataWrapper(cst.parse_module(self.text))
        block_extractor = BlockExtractor(self)
        module.visit(block_extractor)

    rx_python_top_def = re.compile(r'^def\s+(\w+)\s*\(', re.MULTILINE)
    rx_python_classes = re.compile(r'^class\s+(\w+)\s*[:(]', re.MULTILINE)
    rx_python_methods = re.compile(r'^\s+def\s+(\w+)\s*\(', re.MULTILINE)

    def find_python_blocks_with_regexps(self):
        # TODO
        self.find_text_blocks()

        # for top in self.rx_python_top.finditer(self.text.replace('\t', '    ')):
        #     pass
        #
        # functions = self.text.split('\ndef')
        # for fn in functions:
        #     classes = f'\ndef{fn}\n'.split('\nclass')
        #     for cls in classes:
        #         methods = f'\nclass{fn}\n'.split('\n    def')

    def find_text_blocks(self):
        lineno = 1
        for paragraph in self.text.split('\n\n'):
            for fragment in text_splitter.split_text(paragraph):
                block = Block(self.project_id, self.path, lineno, 'text', '', '', fragment)
                self.blocks.append(block)
                lineno += fragment.count('\n') + 1


class BlockExtractor(cst.CSTTransformer):
    METADATA_DEPENDENCIES = (PositionProvider,)
    block_limit = 1000

    def __init__(self, source: Source) -> None:
        super().__init__()
        self.source: Source = source
        self.namespaces: List[str] = []
        self.module: Optional[cst.Module] = None
        self.size: int = 0

    def store_block(self, lineno: int, category: str, fragment: str):
        if not fragment.strip():
            return

        if self.namespaces:
            full_name = '.'.join(self.namespaces)
        else:
            full_name = ''

        for split_fragment in text_splitter.split_text(fragment):
            block = Block(self.source.project_id, self.source.path, lineno, self.source.language, full_name, category, split_fragment)
            self.source.blocks.append(block)
            lineno += split_fragment.count('\n')

    def visit_Module(self, node: cst.Module):
        self.module = node

    def leave_Module(self, original_node: cst.Module, updated_node: cst.Module):
        self.store_block(1, CATEGORY_MODULE, self.module.code_for_node(updated_node))
        self.module = None
        return updated_node

    def visit_FunctionDef(self, node: cst.FunctionDef):
        self.namespaces.append(node.name.value)

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef):
        position = self.get_metadata(PositionProvider, original_node)
        self.store_block(position.start.line, CATEGORY_FUNCTION, self.module.code_for_node(updated_node))
        self.namespaces.pop()
        return updated_node.with_changes(body=cst.Ellipsis())

    def visit_ClassDef(self, node: cst.ClassDef):
        self.namespaces.append(node.name.value)
        return super().visit_ClassDef(node)

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef):
        position = self.get_metadata(PositionProvider, original_node)
        self.store_block(position.start.line, CATEGORY_CLASS, self.module.code_for_node(updated_node))
        self.namespaces.pop()
        return updated_node.with_changes(body=cst.Ellipsis())


class Project:

    def __init__(self, base_dir: str, project_id: Optional[str] = None) -> None:
        super().__init__()
        self.base_dir: str = base_dir
        self.project_id: str = project_id or str(uuid.uuid4())
        self.sources: List[Source] = []

    def __str__(self) -> str:
        return f'Project({self.base_dir!r})'

    __repr__ = __str__

    def load(self):
        base_dir_len = len(self.base_dir) + 1
        for dirpath, dirnames, filenames in os.walk(self.base_dir):
            for filename in filenames:
                language = self.detect_language(filename)
                if language == IGNORE:
                    continue

                path = os.path.join(dirpath, filename)
                with open(path, 'rt', encoding='utf-8') as f:
                    text = f.read()

                relative_path = path[base_dir_len:].replace('\\', '/')
                source = Source(self.project_id, relative_path, language, text.replace('\r', ''))
                self.sources.append(source)

    @staticmethod
    def detect_language(filename):
        lc_filename = filename.lower()
        for extension, language in EXTENSIONS.items():
            if lc_filename.endswith(extension):
                return language
        return LANGUAGE_UNKNOWN


def main():
    project = Project(SOURCE_DIR)
    project.load()

    DEBUG = False

    if DEBUG:
        print(project)
    for source in project.sources:
        if DEBUG:
            print(source)
            for error in source.errors:
                print(f'ERROR: {error}')
            print()
        for block in source.blocks:
            if DEBUG:
                print(f'### {block}')
            print(block.meta)
            print(block.fragment)
        print()


if __name__ == '__main__':
    main()
