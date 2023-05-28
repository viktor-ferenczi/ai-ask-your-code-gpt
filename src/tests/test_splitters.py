import difflib
import os
import unittest
from pprint import pformat

from doc_types import detect_by_extension

MODULE_DIR = os.path.dirname(__file__)
TEST_PROJECT_DIR = os.path.join(MODULE_DIR, 'TestProject')
TEST_OUTPUT_DIR = os.path.join(MODULE_DIR, 'TestOutput')


class TestSplitters(unittest.TestCase):

    def test_splitters(self):
        failed = []
        for root, dirs, files in os.walk(TEST_PROJECT_DIR):
            for filename in files:
                path = os.path.join(root, filename)
                output_subdir = os.path.dirname(path)
                os.makedirs(output_subdir, exist_ok=True)

                doc_type_cls = detect_by_extension(path)
                self.assertIsNotNone(doc_type_cls)
                doc_type = doc_type_cls()

                with open(path, 'rb') as f:
                    data: bytes = f.read()

                relpath = path[len(TEST_PROJECT_DIR) + 1:]
                fragments = list(doc_type.load(relpath, data))

                # Replace UUIDs with sequence numbers, so they are stable
                for index, fragment in enumerate(fragments):
                    fragment.uuid = f'TEST-{index:02d}'

                if doc_type_cls.code:
                    # In case of code there is verified reference output, because of "..." in place of bodies
                    actual = ''.join(fragment.text for fragment in fragments)

                    actual_path = os.path.join(TEST_OUTPUT_DIR, f'{relpath}.text-actual')
                    expected_path = os.path.join(TEST_OUTPUT_DIR, f'{relpath}.text-expected')

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
                else:
                    # In case of documentation joining the fragments must reproduce the original document
                    joined_texts = ''.join(fragment.text for fragment in fragments).replace('\r\n', '\n')
                    original_text = data.decode('utf-8').replace('\r\n', '\n')
                    self.assertEqual(original_text, joined_texts)

                actual = pformat(fragments, width=160)

                actual_path = os.path.join(TEST_OUTPUT_DIR, f'{relpath}.fragments-actual')
                expected_path = os.path.join(TEST_OUTPUT_DIR, f'{relpath}.fragments-expected')

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
