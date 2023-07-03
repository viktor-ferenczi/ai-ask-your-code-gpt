from typing import Callable

from splitters.text_splitter import TextSplitter


class MarkdownSplitter(TextSplitter):

    def __init__(self, *, chunk_size: int, length_function: Callable[[str], int]) -> None:
        super().__init__(
            chunk_size=chunk_size,
            length_function=length_function,
            separators=(
                           # Headings
                           ('<', r"^##\s"),
                           ('<', r"^###\s"),
                           ('<', r"^####\s"),
                           ('<', r"^#####\s"),
                           ('<', r"^######\s"),

                           # Separator lines
                           ('>', r"^\s*\*{3,}\s*$"),
                           ('>', r"^\s*-{3,}\s*$"),
                           ('>', r"^\s*_{3,}\s*$"),

                           # End of code block
                           ('>', r"^```\s*$"),

                           # Numbered lists
                           ('<', r"^\s*\d+\.\s+"),

                           # Unordered lists
                           ('<', r"^\s*[\*\-]\.\s+"),

                           # Links on separate lines
                           ('<', r"^\s*\[\!"),
                       ) + TextSplitter.default_separators
        )
