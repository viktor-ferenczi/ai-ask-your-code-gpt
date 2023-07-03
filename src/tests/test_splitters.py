from pprint import pformat

from base_test_case import BaseTestCase
from common.tools import tiktoken_len
from splitters.markdown_splitter import MarkdownSplitter
from splitters.text_splitter import TextSplitter


class TestSplitters(BaseTestCase):
    test_script = __file__

    def verify_splitter(self, splitter: TextSplitter, filename: str):
        text = self.read_test_file_as_text(filename)
        sentences = list(splitter.split_text(text))

        merged = ''.join(sentence.text for sentence in sentences)
        self.assertEqual(merged, text, 'Merged sentences do not match the original text')

        actual = pformat(sentences)
        self.verify(filename, actual)

        self.assertAllSucceeded()

    def test_text_splitter(self):
        splitter = TextSplitter(chunk_size=150, length_function=tiktoken_len)
        self.verify_splitter(splitter, 'paul_graham_essay.txt')

    def test_markdown_splitter(self):
        splitter = MarkdownSplitter(chunk_size=150, length_function=tiktoken_len)
        self.verify_splitter(splitter, 'LangChain_README.md')
        self.verify_splitter(splitter, 'cpp_programming_README.md')
