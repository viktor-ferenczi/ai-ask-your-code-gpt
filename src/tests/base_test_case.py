import os
import unittest


class BaseTestCase(unittest.TestCase):
    test_script: str = ''
    max_output_file_size = 20_000_000

    def setUp(self) -> None:
        super().setUp()
        self.failures = []
        assert self.test_script

    def assertNoFailures(self):
        self.assertFalse(bool(self.failures), f"Failed examples: {', '.join(self.failures)}")

    @property
    def data_dir(self) -> str:
        return f'{self.test_script[:-3]}_data'

    def verify(self, name: str, actual: str):
        if len(actual) >= self.max_output_file_size:

            half = len(actual) // 2
            while actual[half] != '\n':
                half += 1
            half += 1

            self.verify(f'{name}-1', actual[:half])
            self.verify(f'{name}-2', actual[half:])
            return

        data_dir = self.data_dir

        actual_dir = os.path.join(data_dir, 'actual')
        expected_dir = os.path.join(data_dir, 'expected')

        os.makedirs(actual_dir, exist_ok=True)
        os.makedirs(expected_dir, exist_ok=True)

        actual_path = os.path.join(actual_dir, f'{name}.py')
        expected_path = os.path.join(expected_dir, f'{name}.py')

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
