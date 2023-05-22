from typing import List, Optional

import libcst as cst
from langchain.text_splitter import TextSplitter
from libcst.metadata import MetadataWrapper, PositionProvider

from model.chunk import Chunk


class PythonParser(cst.CSTTransformer):
    METADATA_DEPENDENCIES = (PositionProvider,)

    def __init__(self, splitter: TextSplitter) -> None:
        super().__init__()
        self.splitter: TextSplitter = splitter
        self.module: Optional[cst.Module] = None
        self.chunks: List[Chunk] = []
        self.fqn: List[str] = []

    def parse(self, code: str) -> List[Chunk]:
        module = MetadataWrapper(cst.parse_module(code))
        module.visit(self)
        self.chunks.sort(key=lambda chunk: chunk.lineno)
        return self.chunks

    def store(self, lineno: int, name: str, code: str):
        if not code.strip():
            return

        self.chunks.extend(self.split_code(lineno, code, name))

    def split_code(self, lineno: int, code: str, name: str):
        for text in self.splitter.split_text(code):
            yield Chunk(lineno, text, name)
            # FIXME: Not exact due to the splitter eating the separators, but good enough for sorting
            lineno += text.count('\n') + 1

    def visit_Module(self, node: cst.Module):
        self.module = node

    def leave_Module(self, original_node: cst.Module, updated_node: cst.Module):
        self.store(1, 'module', self.module.code_for_node(updated_node))
        self.module = None
        return updated_node

    def visit_FunctionDef(self, node: cst.FunctionDef):
        self.fqn.append(node.name.value)

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef):
        position = self.get_metadata(PositionProvider, original_node)
        self.store(position.start.line, '.'.join(self.fqn), self.module.code_for_node(updated_node))
        self.fqn.pop()
        return updated_node.with_changes(body=cst.Ellipsis())

    def visit_ClassDef(self, node: cst.ClassDef):
        self.fqn.append(node.name.value)

    def leave_ClassDef(self, original_node: cst.ClassDef, updated_node: cst.ClassDef):
        position = self.get_metadata(PositionProvider, original_node)
        self.store(position.start.line, '.'.join(self.fqn), self.module.code_for_node(updated_node))
        self.fqn.pop()
        return updated_node.with_changes(body=cst.Ellipsis())
