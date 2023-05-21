import difflib
import os
import unittest
from pprint import pformat
from typing import Iterator

from fragmentation import Project

SOURCE_DIR = os.path.join(os.path.dirname(__file__), 'TestProject')
ACTUAL_PATH = f'{os.path.abspath(__file__)[:-3]}.actual.txt'
REFERENCE_PATH = f'{os.path.abspath(__file__)[:-3]}.reference.txt'


class TestFragmentation(unittest.TestCase):

    def test_fragmentation(self):
        project = Project()
        project.load_from_disk()

        normalize_project(project)

        actual = list(dump_project(project))

        with open(REFERENCE_PATH, 'rt') as f:
            reference = f.readlines()

        try:
            self.assertTrue(actual == reference)
        except AssertionError:
            with open(ACTUAL_PATH, 'wt') as f:
                f.writelines(actual)
            print_diff(actual, reference)


def normalize_project(project: Project):
    for source in project.sources:
        source.project_id = 'PROJECT-ID'
        source.text = ''
        for block in source.blocks:
            block.project_id = 'PROJECT-ID'
            block.block_id = 'BLOCK-ID'


def dump_project(project: Project) -> Iterator[str]:
    for source in project.sources:
        yield from yield_lines(pformat(source))
        yield '\n'
        for block in source.blocks:
            yield from yield_lines(pformat(block))
            yield '\n'
        yield '\n'
        yield '\n'


def yield_lines(text: str) -> Iterator[str]:
    for line in text.split('\n'):
        yield f'{line}\n'


def print_diff(actual, reference):
    for line in difflib.context_diff(reference, actual):
        print(line, end='')
