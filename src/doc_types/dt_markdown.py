__all__ = ['MarkdownDocType']

from langchain.text_splitter import MarkdownTextSplitter

from doc_types.dt_text import TextDocType


class MarkdownDocType(TextDocType):
    store_instruction: str = 'Represent the Markdown document for retrieval'
    query_instruction: str = 'Represent the Markdown document question for retrieving relevant sections'

    splitter_cls = MarkdownTextSplitter
