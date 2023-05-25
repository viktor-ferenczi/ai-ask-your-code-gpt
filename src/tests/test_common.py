import unittest

from common.doc import find_common_base_dir, remove_common_base_dir


class TestCommonDoc(unittest.TestCase):

    def test_find_common_base_dir(self):
        self.assertEqual(find_common_base_dir(['a/b/c', 'b/c/d']), '')
        self.assertEqual(find_common_base_dir(['/a/b/c', '/b/c/d']), '/')

        self.assertEqual(find_common_base_dir(['a/b/c', 'a/c/d']), 'a/')
        self.assertEqual(find_common_base_dir(['/a/b/c', '/a/c/d']), '/a/')

        self.assertEqual(find_common_base_dir(['a/b/c', 'a/b/d']), 'a/b/')
        self.assertEqual(find_common_base_dir(['/a/b/c', '/a/b/d']), '/a/b/')
