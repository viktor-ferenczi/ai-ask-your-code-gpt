import os
import pprint
import zipfile
from datetime import datetime, timedelta
from typing import List

from base_backend_test import BaseBackendTest
from common.constants import C
from logic.backend import Backend, TInfo
from model.hit import Hit
from services.cleanup import cleanup
from storage import projects

MODULE_DIR = os.path.dirname(__file__)


def normalize_hits(hits: List[Hit]) -> None:
    for i, hit in enumerate(hits):
        hit.uuid = str(i)


class TestBackend(BaseBackendTest):
    test_script = __file__
    test_project_dir = os.path.join(MODULE_DIR, 'test_parsers_data', 'input')
    zip_path = os.path.join(MODULE_DIR, 'TestProject.zip')

    async def asyncSetUp(self) -> None:
        await super().asyncSetUp()

        dir_len = len(self.test_project_dir) + 1
        with zipfile.ZipFile(self.zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.test_project_dir):
                for filename in files:
                    path = os.path.join(root, filename)
                    archive_path = path[dir_len:]
                    zipf.write(path, archive_path)

    async def asyncTearDown(self) -> None:
        try:
            os.remove(self.zip_path)
        except (IOError, OSError):
            pass

        await super().asyncTearDown()

    async def test_backend(self):
        await self.coordinate_test()

    async def actual_test(self):
        await self.download_error()
        await self.small_project('small_project_1')
        await self.small_project('small_project_2')
        await self.medium_project()

        self.assertAllSucceeded()

        await self.cleanup_projects()

    async def download_error(self):
        backend = await Backend.ensure_project(self.db, 'tester', 'download_error')
        info: TInfo = await backend.download('http://127.0.0.1:49000/this-will-fail', timeout=10.0)
        print(info)
        self.assertTrue('Failed to download' in info['status'])
        self.assertTrue('hint' in info)
        await self.scheduler.delete_all_tasks()

    async def small_project(self, project_name):
        backend = await Backend.ensure_project(self.db, 'tester', project_name)
        info: TInfo = await backend.download('http://127.0.0.1:49000/test.zip', timeout=2.0)
        print(info)
        self.assertTrue('Archive downloaded' in info['status'])

        await self.wait_for_processing(10.0)

        hits = await backend.search(tail='.py', name='Duplicates')
        normalize_hits(hits)
        self.verify('small-tail-py-name', hits)

        hits = await backend.search(path='/find_duplicates.py', limit=100)
        normalize_hits(hits)
        self.verify('small-path-find_duplicates.py', hits)

        hits = await backend.search(tail='.py', path='/find_duplicates.py', limit=100)
        normalize_hits(hits)
        self.verify('small-path-tail-py', hits)

        summary = await backend.summarize(path='/find_duplicates.py')
        self.verify('small-summary-find_duplicates_py', summary)

        hits = await backend.search(path='/README.md', limit=100)
        normalize_hits(hits)
        self.verify('small-path-README.md', hits)

        hits = await backend.search(tail='.md', text='standard set of source code files', limit=1)
        normalize_hits(hits)
        self.verify('small-tail-md-text', hits)

        hits = await backend.search(text='class Duplicates', limit=10)
        normalize_hits(hits)
        self.verify('small-text', hits)

        summary = await backend.summarize(tail='.md')
        self.verify('small-summary-md', summary)

        summary = await backend.summarize(tail='.py')
        self.verify('small-summary-py', summary)

    async def medium_project(self):
        backend = await Backend.ensure_project(self.db, 'tester', 'medium_project')
        info: TInfo = await backend.download('https://github.com/viktor-ferenczi/dblayer/archive/refs/tags/0.7.0.zip', timeout=5.0)
        print(info)
        self.assertTrue('Archive downloaded' in info['status'])

        await self.wait_for_processing(30.0)

        hits = await backend.search(path='/README.md', limit=100)
        normalize_hits(hits)
        self.verify('medium-path-README.md', hits)

        hits = await backend.search(tail='.py', name='Query', limit=100)
        normalize_hits(hits)
        self.verify('medium-tail-py-name', hits)

        summary = await backend.summarize(tail='.md')
        self.verify('medium-tail-md', summary)

        summary = await backend.summarize(path='/lib/dblayer', tail='.py')
        self.verify('medium-path-tail-py', summary)

    async def cleanup_projects(self):
        async with self.db.connection() as conn:
            for table in ('project', 'file', 'document', 'fragment'):
                count = await conn.fetchval(f'SELECT COUNT(1) FROM {table}')
                self.assertNotEqual(count, 0, table)

        expired_timestamp = datetime.utcnow() - (C.PROJECT_EXPIRATION_INTERVAL + timedelta(minutes=1))
        async with self.db.transaction() as conn:
            project_list = await projects.list_all(conn)
            for project in project_list:
                await projects.update_accessed(conn, project.id, expired_timestamp)

        assert C.CLEANUP_MAX_PROJECTS >= len(project_list)
        await cleanup(self.db)

        async with self.db.connection() as conn:
            for table in ('project', 'file', 'document', 'fragment'):
                count = await conn.fetchval(f'SELECT COUNT(1) FROM {table}')
                self.assertEqual(count, 0, table)
