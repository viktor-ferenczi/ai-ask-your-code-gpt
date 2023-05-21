import os
import re
import uuid
from dataclasses import dataclass
from typing import List, Optional, Dict

import libcst as cst
import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter, PythonCodeTextSplitter, MarkdownTextSplitter
from libcst.metadata import MetadataWrapper, PositionProvider

SOURCE_DIR = r'C:\Dev\LLM\Source\viktor-ferenczi-dblayer'

CATEGORY_MODULE = 'module'
CATEGORY_FUNCTION = 'function'
CATEGORY_CLASS = 'class'

LANGUAGE_TEXT = 'Text'
LANGUAGE_MD = 'Markdown'
LANGUAGE_PYTHON = 'Python'
LANGUAGE_SHELL = 'Shell'
LANGUAGE_CS = 'C#'
LANGUAGE_C = 'C'
LANGUAGE_CPP = 'C++'
LANGUAGE_JAVA = 'Java'
LANGUAGE_JS = 'JavaScript'
LANGUAGE_CSS = 'CSS'
LANGUAGE_HTML = 'HTML'
LANGUAGE_RUST = 'Rust'
LANGUAGE_ZIG = 'Zig'
LANGUAGE_SQL = 'SQL'

IGNORE = 'ignore'

EXTENSIONS = {
    '.txt': LANGUAGE_TEXT,
    '.md': LANGUAGE_MD,
    '.py': LANGUAGE_PYTHON,
    '.sh': LANGUAGE_SHELL,
    '.cs': LANGUAGE_CS,
    '.c': LANGUAGE_C,
    '.h': LANGUAGE_C,
    '.cpp': LANGUAGE_CPP,
    '.hpp': LANGUAGE_CPP,
    '.java': LANGUAGE_JAVA,
    '.js': LANGUAGE_JS,
    '.css': LANGUAGE_CSS,
    '.html': LANGUAGE_HTML,
    '.rust': LANGUAGE_RUST,
    '.zig': LANGUAGE_ZIG,
    '.sql': LANGUAGE_SQL,
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
    chunk_size=400,
    chunk_overlap=0,
    length_function=tiktoken_len,
    separators=["\n\n", "\n"]
)

markdown_splitter = MarkdownTextSplitter(
    chunk_size=400,
    chunk_overlap=0,
    length_function=tiktoken_len,
)

python_splitter = PythonCodeTextSplitter(
    chunk_size=400,
    chunk_overlap=0,
    length_function=tiktoken_len,
)


@dataclass
class Block:
    block_id: str
    project_id: str
    path: str
    index: int
    language: str
    name: str
    category: str
    fragment: str

    def __str__(self) -> str:
        return f'Block({self.block_id!r}, {self.project_id!r}, {self.path!r}, {self.index}, {self.language!r}, {self.name!r}, {self.category!r})'

    @property
    def meta(self) -> Dict[str, object]:
        return dict(
            path=self.path,
            index=self.index,
            language=self.language,
            name=self.name,
            category=self.category,
        )


@dataclass
class Source:
    project_id: str
    path: str
    language: str
    text: str

    def find_blocks(self):
        self.blocks: List[Block] = []
        self.errors: List[str] = []

        if self.language == LANGUAGE_TEXT:
            self.find_text_blocks(text_splitter)
        if self.language == LANGUAGE_MD:
            self.find_text_blocks(markdown_splitter)
        elif self.language == LANGUAGE_PYTHON:
            self.find_python_blocks()
        else:
            self.find_text_blocks(text_splitter)
            # raise ValueError(f'Invalid source language: {self.language}')

    def find_python_blocks(self):
        initial_block_count: int = len(self.blocks)

        try:
            self.find_python_blocks_with_libcst()
        except SyntaxError as e:
            print(f'FAILED TO PARSE PYTHON CODE: [{e.__class__.__name__}] {e}')
            self.errors.append(f'Failed to parse as Python 3 source code, splitting as text instead')

            del self.blocks[initial_block_count:]

            self.find_python_blocks_as_text()

    def find_python_blocks_with_libcst(self):
        module = MetadataWrapper(cst.parse_module(self.text))
        block_extractor = BlockExtractor(self)
        module.visit(block_extractor)

    rx_python_top_def = re.compile(r'^def\s+(\w+)\s*\(', re.MULTILINE)
    rx_python_classes = re.compile(r'^class\s+(\w+)\s*[:(]', re.MULTILINE)
    rx_python_methods = re.compile(r'^\s+def\s+(\w+)\s*\(', re.MULTILINE)

    def find_python_blocks_as_text(self):
        self.find_text_blocks(python_splitter)

    def find_text_blocks(self, splitter):
        for fragment in splitter.split_text(self.text):
            block = Block(str(uuid.uuid4()), self.project_id, self.path, len(self.blocks), 'text', '', '', fragment)
            self.blocks.append(block)


class BlockExtractor(cst.CSTTransformer):
    METADATA_DEPENDENCIES = (PositionProvider,)
    block_limit = 1000

    def __init__(self, source: Source) -> None:
        super().__init__()
        self.source: Source = source
        self.namespaces: List[str] = []
        self.module: Optional[cst.Module] = None
        self.size: int = 0

    def store_block(self, category: str, fragment: str):
        if not fragment.strip():
            return

        if self.namespaces:
            full_name = '.'.join(self.namespaces)
        else:
            full_name = ''

        for split_fragment in text_splitter.split_text(fragment):
            block = Block(str(uuid.uuid4()), self.source.project_id, self.source.path, len(self.source.blocks), self.source.language, full_name, category, split_fragment)
            self.source.blocks.append(block)

    def visit_Module(self, node: cst.Module):
        self.module = node

    def leave_Module(self, original_node: cst.Module, updated_node: cst.Module):
        self.store_block(CATEGORY_MODULE, self.module.code_for_node(updated_node))
        self.module = None
        return updated_node

    def visit_FunctionDef(self, node: cst.FunctionDef):
        self.namespaces.append(node.name.value)

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef):
        position = self.get_metadata(PositionProvider, original_node)
        self.store_block(CATEGORY_FUNCTION, self.module.code_for_node(updated_node))
        self.namespaces.pop()
        return updated_node.with_changes(body=cst.Ellipsis())

    def visit_ClassDef(self, node: cst.ClassDef):
        self.namespaces.append(node.name.value)
        return super().visit_ClassDef(node)

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef):
        position = self.get_metadata(PositionProvider, original_node)
        self.store_block(CATEGORY_CLASS, self.module.code_for_node(updated_node))
        self.namespaces.pop()
        return updated_node.with_changes(body=cst.Ellipsis())


@dataclass
class Project:

    def __init__(self, project_id: Optional[str] = None) -> None:
        super().__init__()
        self.project_id: str = project_id or str(uuid.uuid4())
        self.sources: List[Source] = []

    def __str__(self) -> str:
        return f'Project({self.project_id!r})'

    __repr__ = __str__

    def load_from_disk(self, source_dir: str):
        base_dir_len = len(source_dir) + 1
        for dirpath, dirnames, filenames in os.walk(source_dir):
            for filename in filenames:
                language = self.detect_language(filename)
                if not language:
                    continue

                path = os.path.join(dirpath, filename)
                with open(path, 'rt', encoding='utf-8') as f:
                    text = f.read()

                relative_path = path[base_dir_len:].replace('\\', '/')
                source = Source(self.project_id, relative_path, language, text.replace('\r', ''))
                source.find_blocks()
                self.sources.append(source)

    def load_from_memory(self, files):
        for path, text in files:

            language = self.detect_language(path)
            if not language:
                continue

            source = Source(self.project_id, path, language, text.replace('\r', ''))
            source.find_blocks()
            self.sources.append(source)

    @staticmethod
    def detect_language(filename):
        lc_filename = filename.lower()
        for extension, language in EXTENSIONS.items():
            if lc_filename.endswith(extension):
                return language
        return None


def main():
    project = Project()
    project.load_from_disk()

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
