import unittest

from common.doc import find_common_base_dir
from common.http import download_into_memory, NotModified, DownloadError


class TestCommonDoc(unittest.TestCase):

    def test_find_common_base_dir(self):
        self.assertEqual(find_common_base_dir(['a']), '')
        self.assertEqual(find_common_base_dir(['/a']), '/')

        self.assertEqual(find_common_base_dir(['a/b']), 'a/')
        self.assertEqual(find_common_base_dir(['/a/b']), '/a/')

        self.assertEqual(find_common_base_dir(['a/b/c', 'b/c/d']), '')
        self.assertEqual(find_common_base_dir(['/a/b/c', '/b/c/d']), '/')

        self.assertEqual(find_common_base_dir(['a/b/c', 'a/c/d']), 'a/')
        self.assertEqual(find_common_base_dir(['/a/b/c', '/a/c/d']), '/a/')

        self.assertEqual(find_common_base_dir(['a/b/c', 'a/b/d']), 'a/b/')
        self.assertEqual(find_common_base_dir(['/a/b/c', '/a/b/d']), '/a/b/')

        self.assertEqual(find_common_base_dir(['a/b/c', 'a/b/d', 'a/c']), 'a/')
        self.assertEqual(find_common_base_dir(['/a/b/c', '/a/b/d', '/a/c']), '/a/')

        dblayer_files = ['dblayer-0.7.0/', 'dblayer-0.7.0/.gitignore', 'dblayer-0.7.0/README.md', 'dblayer-0.7.0/lib/', 'dblayer-0.7.0/lib/MANIFEST.in', 'dblayer-0.7.0/lib/PKG-INFO', 'dblayer-0.7.0/lib/dblayer/', 'dblayer-0.7.0/lib/dblayer/__init__.py', 'dblayer-0.7.0/lib/dblayer/backend/', 'dblayer-0.7.0/lib/dblayer/backend/__init__.py', 'dblayer-0.7.0/lib/dblayer/backend/base/', 'dblayer-0.7.0/lib/dblayer/backend/base/__init__.py', 'dblayer-0.7.0/lib/dblayer/backend/base/clauses.py', 'dblayer-0.7.0/lib/dblayer/backend/base/database.py', 'dblayer-0.7.0/lib/dblayer/backend/base/error.py', 'dblayer-0.7.0/lib/dblayer/backend/base/format.py', 'dblayer-0.7.0/lib/dblayer/backend/base/record.py', 'dblayer-0.7.0/lib/dblayer/backend/postgresql/', 'dblayer-0.7.0/lib/dblayer/backend/postgresql/__init__.py', 'dblayer-0.7.0/lib/dblayer/backend/postgresql/clauses.py', 'dblayer-0.7.0/lib/dblayer/backend/postgresql/database.py', 'dblayer-0.7.0/lib/dblayer/backend/postgresql/error.py',
                         'dblayer-0.7.0/lib/dblayer/backend/postgresql/format.py', 'dblayer-0.7.0/lib/dblayer/backend/postgresql/inspector.py', 'dblayer-0.7.0/lib/dblayer/backend/postgresql/record.py', 'dblayer-0.7.0/lib/dblayer/constants.py', 'dblayer-0.7.0/lib/dblayer/generator/', 'dblayer-0.7.0/lib/dblayer/generator/__init__.py', 'dblayer-0.7.0/lib/dblayer/generator/generator.py', 'dblayer-0.7.0/lib/dblayer/generator/template/', 'dblayer-0.7.0/lib/dblayer/generator/template/database.tpl', 'dblayer-0.7.0/lib/dblayer/graph/', 'dblayer-0.7.0/lib/dblayer/graph/__init__.py', 'dblayer-0.7.0/lib/dblayer/graph/gml.py', 'dblayer-0.7.0/lib/dblayer/model/', 'dblayer-0.7.0/lib/dblayer/model/__init__.py', 'dblayer-0.7.0/lib/dblayer/model/aggregate.py', 'dblayer-0.7.0/lib/dblayer/model/column.py', 'dblayer-0.7.0/lib/dblayer/model/constraint.py', 'dblayer-0.7.0/lib/dblayer/model/database.py', 'dblayer-0.7.0/lib/dblayer/model/function.py', 'dblayer-0.7.0/lib/dblayer/model/index.py',
                         'dblayer-0.7.0/lib/dblayer/model/procedure.py', 'dblayer-0.7.0/lib/dblayer/model/query.py', 'dblayer-0.7.0/lib/dblayer/model/table.py', 'dblayer-0.7.0/lib/dblayer/model/trigger.py', 'dblayer-0.7.0/lib/dblayer/test/', 'dblayer-0.7.0/lib/dblayer/test/__init__.py', 'dblayer-0.7.0/lib/dblayer/test/constants.py', 'dblayer-0.7.0/lib/dblayer/test/model.py', 'dblayer-0.7.0/lib/dblayer/test/test_abstraction.py', 'dblayer-0.7.0/lib/dblayer/util.py', 'dblayer-0.7.0/lib/dblayer/version.py', 'dblayer-0.7.0/lib/setup.cfg', 'dblayer-0.7.0/lib/setup.py']
        self.assertEqual(find_common_base_dir(dblayer_files), 'dblayer-0.7.0/')


class TestCommonHttp(unittest.IsolatedAsyncioTestCase):

    async def test_download_file(self):
        url = 'https://github.com/viktor-ferenczi/dblayer/archive/refs/heads/master.zip'

        data1, checksum1 = await download_into_memory(url)
        self.assertTrue(bool(data1))

        try:
            await download_into_memory(url, cached_etag=checksum1)
        except NotModified:
            pass
        else:
            self.fail('NotModified was not raised')

        try:
            await download_into_memory(url, max_size=len(data1) - 1)
        except DownloadError:
            pass
        else:
            self.fail('DownloadError was not raised')
