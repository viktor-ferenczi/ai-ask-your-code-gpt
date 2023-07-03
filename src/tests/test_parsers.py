import os
from pprint import pformat

from base_test_case import BaseTestCase
from parsers.registrations import BaseParser, detect, detect_mime


class TestParsers(BaseTestCase):
    test_script = __file__

    def test_parsers(self):
        for path, relpath in self.walk_test_files():
            filename = os.path.basename(path)

            content = self.read_test_file_as_bytes(relpath)

            mime_type = detect_mime(content)
            parser_cls = detect(filename, mime_type)
            self.assertIsNotNone(parser_cls)

            parser: BaseParser = parser_cls()
            fragments = list(parser.parse(relpath, content))

            # Replace UUIDs with sequence numbers, so they are stable
            for index, fragment in enumerate(fragments):
                fragment.uuid = f'TEST-{index:02d}'

            # In case of documentation joining the fragments must reproduce the original document
            if not parser.is_code:
                joined_texts = ''.join(fragment.text for fragment in fragments if fragment.type == 'documentation').replace('\r\n', '\n').replace('\r', '')
                original_text = content.decode('utf-8').replace('\r\n', '\n').replace('\r', '')
                self.assertEqual(joined_texts, original_text)

            actual = f'from model.fragment import Fragment\n\n# Parser: {parser_cls.__name__}\n\n' + ''.join(
                f'f{i} = {pformat(fragment, width=120)}\n\n'
                for i, fragment in enumerate(fragments)
            )

            self.verify(filename, actual)
            self.assertAllSucceeded()

        self.assertAllSucceeded()
