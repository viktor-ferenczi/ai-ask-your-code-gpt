__all__ = ['MarkdownDocType']

from typing import Iterator

from parsers.text_splitter import MarkdownTextSplitter

from common.constants import C
from doc_types.dt_text import TextDocType


class MarkdownDocType(TextDocType):
    store_instruction: str = 'Represent the Markdown document for retrieval'
    query_instruction: str = 'Represent the text query for retrieving relevant sections'

    parser_cls = MarkdownTextSplitter

    @classmethod
    def summarize(cls, text: str) -> Iterator[str]:
        max_width = C.MAX_SUMMARY_WIDTH
        for line in text.split('\n'):
            line = line.strip()
            if line.startswith('#'):
                if len(line) <= max_width:
                    yield line
                else:
                    yield f'{line[:max_width]}...'
