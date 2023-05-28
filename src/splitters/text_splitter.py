from typing import Callable, List, Iterator, Collection


def iter_split(fragments: List[str], separator: str) -> Iterator[str]:
    for text in fragments:
        start = 0
        while 1:
            next = text.find(separator, start)
            if next < 0:
                yield text[start:]
                break
            yield text[start:next]
            start = next


class TextSplitter:

    def __init__(self, chunk_size: int, length_function: Callable[[str], int] = len, separators: Collection[str] = ('\n\n', '\n', ' ', '')) -> None:
        self.chunk_size = chunk_size
        self.separators = separators
        self.length_function = length_function

    def split_text(self, text: str) -> Iterator[str]:
        s = 0
        a = 0
        b = len(text)
        while a < b:

            # Can the fragment fit?
            if self.length_function(text[a:b]) <= self.chunk_size:
                yield text[a:b]
                a = b
                b = len(text)
                s = 0
                continue

            # Split
            c = self.separators[s]
            if c:
                n = text.find(c, a + 1)
                if n < 0 or n >= b:
                    s += 1
                    continue
                b = n
                continue

            # Just half at the character level to progress faster
            b = (a + b) // 2


class MarkdownTextSplitter(TextSplitter):

    def __init__(self, chunk_size: int, length_function: Callable[[str], int] = len) -> None:
        super().__init__(
            chunk_size,
            length_function,
            (
                # First, try to split along Markdown headings (starting with level 2)
                "\n## ",
                "\n### ",
                "\n#### ",
                "\n##### ",
                "\n###### ",
                # Note the alternative syntax for headings (below) is not handled here
                # Heading level 2
                # ---------------
                # End of code block
                "```\n\n",
                # Horizontal lines
                "\n\n***\n\n",
                "\n\n---\n\n",
                "\n\n___\n\n",
                # Note that this splitter doesn't handle horizontal lines defined
                # by *three or more* of ***, ---, or ___, but this is not handled
                "\n\n",
                "\n",
                " ",
                "",
            )
        )
