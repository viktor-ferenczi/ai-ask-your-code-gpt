from base_test_case import BaseSyncTestCase
from common.tools import tiktoken_len
from splitters.markdown_splitter import MarkdownSplitter
from splitters.text_splitter import TextSplitter


class TestSplitters(BaseSyncTestCase):
    test_script = __file__

    def verify_splitter(self, splitter: TextSplitter, filename: str):
        text = self.read_test_file_as_text(filename)
        sentences = list(splitter.split_text(text))

        merged = ''.join(sentence.text for sentence in sentences)
        self.assertEqual(merged, text, 'Merged sentences do not match the original text')

        self.verify(filename, sentences, 'py')

    def test_splitters(self):
        splitter = TextSplitter(chunk_size=150, length_function=tiktoken_len)
        self.verify_splitter(splitter, 'paul_graham_essay.txt')

        splitter = MarkdownSplitter(chunk_size=150, length_function=tiktoken_len)
        self.verify_splitter(splitter, 'LangChain_README.md')
        self.verify_splitter(splitter, 'cpp_programming_README.md')

        self.assertAllSucceeded()
