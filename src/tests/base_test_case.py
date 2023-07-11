import os
import shutil
import unittest
from pprint import pformat
from typing import Any, Iterator, Tuple


class TestVerificationMixin:
    test_script: str = ''
    max_output_file_size = 20_000_000
    test_data_subdir: str = ''

    def init_test_verification(self) -> None:
        assert self.test_script, 'Please define `test_script = __file__` in your subclass'
        self.failures = []

        self.set_data_subdir('')

    def set_data_subdir(self, subdir: str) -> None:
        assert '..' not in subdir
        self.test_data_subdir = subdir

        # Sanity checks, so the code does not delete or litter itself
        assert f'_data/{subdir}' in self.actual_dir.replace('\\', '/')
        assert f'_data/{subdir}' in self.expected_dir.replace('\\', '/')

        if os.path.isdir(self.actual_dir):
            shutil.rmtree(self.actual_dir)

    def assertEqual(self, first: Any, second: Any, msg: Any = ...) -> None:
        super().assertEqual(second, first, msg)

    def assertNotEqual(self, first: Any, second: Any, msg: Any = ...) -> None:
        super().assertNotEqual(second, first, msg)

    def assertAllSucceeded(self):
        self.assertTrue(not self.failures, f"Failed verifications: {', '.join(self.failures)}")

    @property
    def data_dir(self) -> str:
        return f'{self.test_script[:-3]}_data'

    @property
    def input_dir(self) -> str:
        if self.test_data_subdir:
            return os.path.join(self.data_dir, self.test_data_subdir, 'input')
        return os.path.join(self.data_dir, 'input')

    @property
    def actual_dir(self) -> str:
        if self.test_data_subdir:
            return os.path.join(self.data_dir, self.test_data_subdir, 'actual')
        return os.path.join(self.data_dir, 'actual')

    @property
    def expected_dir(self) -> str:
        if self.test_data_subdir:
            return os.path.join(self.data_dir, self.test_data_subdir, 'expected')
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

    def verify(self, name: str, actual: Any, extension: str = '') -> None:
        default_extension = 'txt'
        if not isinstance(actual, str):
            actual = pformat(actual)
            default_extension = 'py'

        extension = (extension or default_extension).lstrip('.')

        if len(actual) >= self.max_output_file_size:

            half = len(actual) // 2
            while actual[half] != '\n':
                half += 1
            half += 1

            self.verify(f'{name}-1', actual[:half], extension)
            self.verify(f'{name}-2', actual[half:], extension)
            return

        os.makedirs(self.actual_dir, exist_ok=True)
        os.makedirs(self.expected_dir, exist_ok=True)

        actual_path = os.path.join(self.actual_dir, f'{name}.{extension}')
        expected_path = os.path.join(self.expected_dir, f'{name}.{extension}')

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

            if self.test_data_subdir:
                self.failures.append(f'{self.test_data_subdir}/{name}')
            else:
                self.failures.append(name)


class BaseSyncTestCase(unittest.TestCase, TestVerificationMixin):

    def setUp(self) -> None:
        self.init_test_verification()
        self.maxDiff = 1_000_000
        super().setUp()


class BaseAsyncTestCase(unittest.IsolatedAsyncioTestCase, TestVerificationMixin):

    async def asyncSetUp(self) -> None:
        self.init_test_verification()
        self.maxDiff = 1_000_000
        return await super().asyncSetUp()
