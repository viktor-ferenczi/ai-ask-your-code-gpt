import os
import unittest
from typing import Any, Iterator, Tuple


class BaseTestCase(unittest.TestCase):
    test_script: str = ''
    max_output_file_size = 20_000_000

    def setUp(self) -> None:
        super().setUp()
        self.maxDiff = 1_000_000
        self.failures = []
        assert self.test_script, 'Please define `test_script = __file__` in your subclass'

    def assertAllSucceeded(self):
        self.assertTrue(not self.failures, f"Failed examples: {', '.join(self.failures)}")

    def assertEqual(self, first: Any, second: Any, msg: Any = ...) -> None:
        super().assertEqual(second, first, msg)

    def assertNotEqual(self, first: Any, second: Any, msg: Any = ...) -> None:
        super().assertNotEqual(second, first, msg)

    @property
    def data_dir(self) -> str:
        return f'{self.test_script[:-3]}_data'

    @property
    def input_dir(self) -> str:
        return os.path.join(self.data_dir, 'input')

    @property
    def actual_dir(self) -> str:
        return os.path.join(self.data_dir, 'actual')

    @property
    def expected_dir(self) -> str:
        return os.path.join(self.data_dir, 'expected')

    def format_test_file_path(self, filename: str) -> str:
        return os.path.join(self.input_dir, filename)

    def walk_test_files(self) -> Iterator[Tuple[str, str]]:
        input_dir = os.path.join(self.data_dir, 'input')
        strip_len = len(input_dir) + 1
        for dirpath, _, filenames in os.walk(input_dir):
            for filename in filenames:
                path = os.path.join(dirpath, filename)
                relpath = path[strip_len:]
                yield path, relpath

    def read_test_file_as_text(self, filename: str) -> str:
        path = self.format_test_file_path(filename)
        with open(path, 'rt', encoding='utf-8') as f:
            return f.read()

    def read_test_file_as_bytes(self, filename: str) -> bytes:
        path = self.format_test_file_path(filename)
        with open(path, 'rb') as f:
            return f.read()

    def verify(self, name: str, actual: str):
        if len(actual) >= self.max_output_file_size:

            half = len(actual) // 2
            while actual[half] != '\n':
                half += 1
            half += 1

            self.verify(f'{name}-1', actual[:half])
            self.verify(f'{name}-2', actual[half:])
            return

        os.makedirs(self.actual_dir, exist_ok=True)
        os.makedirs(self.expected_dir, exist_ok=True)

        actual_path = os.path.join(self.actual_dir, f'{name}.py')
        expected_path = os.path.join(self.expected_dir, f'{name}.py')

        good = False
        if os.path.exists(expected_path):
            with open(expected_path, 'rt', encoding='utf-8') as f:
                expected = f.read()
            good = actual == expected

        if good:
            if os.path.exists(actual_path):
                os.remove(actual_path)
        else:
            with open(actual_path, 'wb') as f:
                f.write(actual.encode('utf-8', errors='replace'))

            self.failures.append(name)
