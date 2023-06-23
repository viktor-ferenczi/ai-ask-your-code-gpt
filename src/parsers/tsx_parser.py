from parsers.typescript_parser import TypeScriptParser


class TsxParser(TypeScriptParser):
    name = 'TSX'
    extensions = ('tsx',)
    mime_types = ('application/tsx', 'application/x-tsx')
    tree_sitter_subdir = ('tsx',)
