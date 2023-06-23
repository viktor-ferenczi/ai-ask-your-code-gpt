import io
from typing import Iterator

import clang
import clang.cindex

from common.constants import C
from common.text import decode_replace
from common.tools import tiktoken_len, new_uuid
from model.fragment import Fragment
from parsers import BaseParser
from splitters.text_splitter import TextSplitter


def depth(node):
    d = 0
    while node:
        d += 1
        node = node.semantic_parent
    return d


class CppParser(BaseParser):
    name = 'C++'
    extensions = ('c', 'cc', 'cpp', 'c++', 'h', 'hh', 'hpp', 'h++')
    mime_types = ('text/c', 'text/x-cpp', 'text/x-cplusplus')
    is_code = True

    categories = [
        ('macro', 'Macro'),
        ('namespace', 'Namespaces'),
        ('interface', 'Interfaces'),
        ('class', 'Classes'),
        ('method', 'Methods'),
        ('variable', 'Variables'),
        ('usage', 'Usages'),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.splitter = TextSplitter(
            chunk_size=C.MAX_TOKENS_PER_FRAGMENT,
            length_function=tiktoken_len,
            separators=(
                ('<', r"^\s+class\s+"),
                ('<', r"^\s+struct\s+"),
                ('<', r"^\s+while\s+"),
                ('<', r"^\s+for\s+"),
                ('<', r"^\s+if\s+"),
                ('<', r"^\s+elif\s+"),
                ('<', r"^\s+else\s+"),
                ('<', r"^\s+try\s+"),
                ('<', r"^\s+#if\s+"),
                ('<', r"^\s+#ifdef\s+"),
                ('<', r"^\s+#ifndef\s+"),
                ('<', r"^\s+#else\s+"),
            )
        )

    categories = {
        'class_decl': 'Classes',
        'cxx_method': 'Methods',
        'enum_decl': 'Enums',
        'function_decl': 'Functions',
        'function_template': 'Templates',
        'namespace': 'Namespaces',
        'struct_decl': 'Structs',
        'using_declaration': 'Using declarations',
        'using_directive': 'Using directives',
        'var_decl': 'Variable declarations',
    }

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:

        lines = decode_replace(content).replace('\r\n', '\n').replace('\r', '').split('\n')

        def get_extent_as_string(node) -> str:
            start = node.extent.start
            end = node.extent.end
            return ''.join(f'{line}\n' for line in lines[start.line - 1:end.line])

        def traverse(node, filename):
            for child in node.get_children():
                if child.location.file.name != filename:
                    continue
                lineno = child.location.line
                type_name = str(child.kind).split(".")[1].lower()
                name = child.spelling
                uuid = new_uuid()
                depth_in_code = depth(child)
                text = get_extent_as_string(child) if child.is_definition() else ''
                fragment = Fragment(uuid, filename, lineno, depth_in_code, type_name, name, text)
                yield fragment
                traverse(child, filename)

        def parse_cpp_file(filename, content):
            index = clang.cindex.Index.create()
            bio = io.BytesIO(content)
            tu = index.parse(path, unsaved_files=[(path, bio)])
            yield from traverse(tu.cursor, filename)

        # test the parser with a file
        name_map = {}
        for fragment in parse_cpp_file(path, content):
            yield fragment

            if fragment.type not in self.categories:
                continue

            if not fragment.name:
                continue

            names = name_map.get(fragment.type)
            if names is None:
                name_map[fragment.type] = names = set()

            names.add(fragment.name)

        summary = [f'C: {path}\n']
        for key in sorted(self.categories):
            names = name_map.get(key)
            if not names:
                continue
            summary.append(f'  {self.categories[key]}: {", ".join(sorted(names))}\n')

        summary = ''.join(summary)
        yield Fragment(new_uuid(), path, 1, 0, 'summary', '', summary)
