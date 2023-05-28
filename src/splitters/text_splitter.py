from typing import Callable, Iterator, Collection


def find_iter(text: str, sub: str) -> Iterator[int]:
    i = 0
    e = len(text)
    while i < e:
        f = text.find(sub, i)
        if f < 0:
            break
        yield f
        i = f + len(sub)


class TextSplitter:
    default_separators = (
        '>\n\n',
        '>\n',
        '> '
    )

    def __init__(self, chunk_size: int, length_function: Callable[[str], int] = len, separators: Collection[str] = ()) -> None:
        self.chunk_size = chunk_size
        self.separators = separators or self.default_separators
        self.length_function = length_function

    def split_text(self, text: str) -> Iterator[str]:
        chunk = []
        total = 0
        for part, length in self.__split_recursive(text, 0):
            if total + length > self.chunk_size:
                yield ''.join(chunk)
                chunk.clear()
                total = 0
            chunk.append(part)
            total += length

        if chunk:
            yield ''.join(chunk)

    def __split_recursive(self, text: str, depth: int) -> Iterator[str]:
        length = self.length_function(text)
        if length <= self.chunk_size:
            yield text, length
            return

        if depth >= len(self.separators):
            if len(text) < 2:
                yield text
            else:
                half = len(text) // 2
                yield from self.__split_recursive(text[:half], depth)
                yield from self.__split_recursive(text[half:], depth)
            return

        sep = self.separators[depth]
        aff = sep[0]
        sep = sep[1:]

        parts = text.split(sep)
        if aff == '>':
            for part in parts[:-1]:
                yield from self.__split_recursive(part + sep, depth + 1)
            yield from self.__split_recursive(parts[-1], depth + 1)
        elif aff == '<':
            yield from self.__split_recursive(parts[0], depth + 1)
            for part in parts[1:]:
                yield from self.__split_recursive(sep + part, depth + 1)
        else:
            raise ValueError(f'Invalid separator affinity: {sep!r}')


class MarkdownTextSplitter(TextSplitter):

    def __init__(self, chunk_size: int, length_function: Callable[[str], int] = len) -> None:
        super().__init__(
            chunk_size,
            length_function,
            (
                # First, try to split along Markdown headings (starting with level 2)
                "<\n## ",
                "<\n### ",
                "<\n#### ",
                "<\n##### ",
                "<\n###### ",
                # Note the alternative syntax for headings (below) is not handled here
                # Heading level 2
                # ---------------
                # End of code block
                ">```\n\n",
                # Horizontal lines
                ">\n\n***\n\n",
                ">\n\n---\n\n",
                ">\n\n___\n\n",
                # Note that this splitter doesn't handle horizontal lines defined
                # by *three or more* of ***, ---, or ___, but this is not handled
                ">\n\n",
                ">\n",
                "> ",
            )
        )
