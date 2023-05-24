from typing import Optional, Type

from .dt_csharp import CSharpDocType
from .dt_markdown import MarkdownDocType
from .dt_python import PythonDocType
from .dt_text import TextDocType

DOC_TYPES = {
    'txt': TextDocType,
    'md': MarkdownDocType,
    'py': PythonDocType,
    # 'sh': ShellDocType,
    'cs': CSharpDocType,
    # 'c': ,
    # 'h': ,
    # 'cpp': ,
    # 'hpp': ,
    # 'java': ,
    # 'js': ,
    # 'css': ,
    # 'html': ,
    # 'rust': ,
    # 'zig': ,
    # 'sql': ,
}


def detect_by_extension(path_or_filename: str) -> Optional[Type[TextDocType]]:
    extension = path_or_filename.rsplit('.')[-1].lower()
    return DOC_TYPES.get(extension)
