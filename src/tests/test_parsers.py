import difflib
import os
import unittest
from pprint import pformat

import parsers
from parsers import BaseParser

MODULE_DIR = os.path.dirname(__file__)
TEST_PROJECT_DIR = os.path.join(MODULE_DIR, 'TestProject')
TEST_OUTPUT_DIR = os.path.join(MODULE_DIR, 'TestOutput')


class TestParsers(unittest.TestCase):

    def test_parsers(self):
        self.maxDiff = 10000
        failed = []
        strip_len = len(TEST_PROJECT_DIR) + 1
        for root, dirs, files in os.walk(TEST_PROJECT_DIR):
            for filename in files:
                path = os.path.join(root, filename)
                output_subdir = os.path.dirname(path)
                os.makedirs(output_subdir, exist_ok=True)

                with open(path, 'rb') as f:
                    content: bytes = f.read()

                relpath = path[strip_len:]
                parser_cls = parsers.detect(relpath, content)
                self.assertIsNotNone(parser_cls)

                parser: BaseParser = parser_cls()
                fragments = list(parser.parse(relpath, content))

                # Replace UUIDs with sequence numbers, so they are stable
                for index, fragment in enumerate(fragments):
                    fragment.uuid = f'TEST-{index:02d}'

                # In case of documentation joining the fragments must reproduce the original document
                if not parser.is_code():
                    joined_texts = ''.join(fragment.text for fragment in fragments if fragment.type == 'documentation').replace('\r\n', '\n')
                    original_text = content.decode('utf-8').replace('\r\n', '\n')
                    self.assertEqual(original_text, joined_texts)

                actual = f'from model.fragment import Fragment\n\n# Parser: {parser_cls.__name__}\n\n' + ''.join(
                    f'f{i} = {pformat(fragment, width=120)}\n\n'
                    for i, fragment in enumerate(fragments)
                )

                actual_path = os.path.join(TEST_OUTPUT_DIR, f'{relpath}.actual.py')
                expected_path = os.path.join(TEST_OUTPUT_DIR, f'{relpath}.expected.py')

                good = False
                if not os.path.exists(expected_path):
                    with open(expected_path, 'wt') as _:
                        expected = ''
                else:
                    with open(expected_path, 'rt') as f:
                        expected = f.read()
                    good = actual == expected

                if good:
                    if os.path.exists(actual_path):
                        os.remove(actual_path)
                else:
                    failed.append((relpath, actual, expected))
                    with open(actual_path, 'wt') as f:
                        f.write(actual)

        if failed:
            print(f'FAILED {len(failed)} test files:')
            print()
            for relpath, actual, expected in failed:
                print('=' * 70)
                print(relpath)
                print('=' * 70)
                for line in difflib.unified_diff(expected.split('\n'), actual.split('\n')):
                    print(line)
                print()

        self.assertFalse(bool(failed))
