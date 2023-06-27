import io
from typing import Iterator, Set, Dict

import clang
import clang.cindex

from common.constants import C
from common.text import decode_replace
from common.tools import tiktoken_len, new_uuid
from model.fragment import Fragment
from parsers.registrations import BaseParser
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
        ('namespace', 'Namespaces'),
        ('namespace_alias', 'Namespace aliases'),
        ('enum_decl', 'Enums'),
        ('union_decl', 'Unions'),
        ('typedef_decl', 'Typedefs'),
        ('type_alias_decl', 'Type aliases'),
        ('struct_decl', 'Structs'),
        ('class_decl', 'Classes'),
        ('class_template', 'Template classes'),
        ('constructor', 'Constructors'),
        ('destructor', 'Destructors'),
        ('cxx_method', 'Methods'),
        ('function_decl', 'Functions'),
        ('function_template', 'Template functions'),
        ('var_decl', 'Variables'),
        ('using_declaration', 'Using declarations'),
        ('using_directive', 'Using directives'),
        ('static_assert', 'Static asserts'),
    ]

    ignore_types = (
        'unexposed_decl',
    )

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

    def parse(self, path: str, content: bytes) -> Iterator[Fragment]:

        lines = decode_replace(content).replace('\r\n', '\n').replace('\r', '').split('\n')

        name_map: Dict[str, Set] = {name: set() for name, label in self.categories}
        unhandled_types: Dict[str, Fragment] = {}

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

                if type_name in self.ignore_types:
                    continue

                name = child.spelling
                if name and type_name == 'function_decl' and name == name.upper():
                    # Macro usage, ignore for now
                    continue

                uuid = new_uuid()
                depth_in_code = depth(child)
                text = get_extent_as_string(child)  # if child.is_definition() else ''

                if name == 'var_decl' and (text.startswith('class') or text.startswith('struct')):
                    # Class or struct pre-declaration, ignore
                    continue

                if type_name == 'namespace':
                    text = f'namespace {name} {...}'

                if type_name == 'enum_decl' and name == 'class':
                    # Fix the name of enum classes
                    words = [x for x in text.replace('\t', ' ').split() if x]
                    if len(words) >= 3:
                        name = words[2]

                if text:
                    fragment = Fragment(uuid, filename, lineno, depth_in_code, type_name, name, text)
                    if type_name in name_map:
                        yield fragment
                    else:
                        unhandled_types[type_name] = fragment

                traverse(child, filename)

        def parse_cpp_file(filename, content):
            index = clang.cindex.Index.create()
            bio = io.BytesIO(content)
            tu = index.parse(path, unsaved_files=[(path, bio)])
            yield from traverse(tu.cursor, filename)

        for fragment in parse_cpp_file(path, content):
            yield fragment
            if fragment.name:
                names = name_map[fragment.type]
                names.add(fragment.name)

        if unhandled_types:
            print(f'Unhandled fragment types in {path!r}:')
            for type_name in sorted(unhandled_types):
                print(f'- {type_name}: {unhandled_types[type_name]}')
            print()

        summary = [f'C: {path}\n']
        for key, label in sorted(self.categories):
            names = name_map[key]
            if names:
                summary.append(f'  {label}: {", ".join(sorted(names))}\n')

        summary = ''.join(summary)
        yield Fragment(new_uuid(), path, 1, 0, 'summary', '', summary)
