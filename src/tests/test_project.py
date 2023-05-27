import asyncio
import os
import pprint
import shutil
import unittest
import uuid
import zipfile
from typing import List

from quart import Quart, send_file

from common.constants import C
from downloader.downloader import app as downloader_app
from embed.embedder import app as embedder_app
from loader.loader import app as loader_app, workers as loader_workers
from model.hit import Hit
from project.inventory import Inventory
from project.project import Project

MODULE_DIR = os.path.dirname(__file__)


class TestProject(unittest.IsolatedAsyncioTestCase):
    test_project_dir = os.path.join(MODULE_DIR, '..', 'tests', 'TestProject')
    zip_path = os.path.join(MODULE_DIR, 'TestProject.zip')

    def setUp(self) -> None:
        Inventory.filename = 'test-inventory.sqlite'
        inventory = Inventory()
        inventory.drop_database()

        Project.dirname = 'test-projects'
        test_projects_dir = os.path.join(C.DATA_DIR, Project.dirname)
        if os.path.isdir(test_projects_dir):
            shutil.rmtree(test_projects_dir)

        dir_len = len(self.test_project_dir) + 1
        with zipfile.ZipFile(self.zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.test_project_dir):
                for filename in files:
                    path = os.path.join(root, filename)
                    archive_path = path[dir_len:]
                    zipf.write(path, archive_path)

    def tearDown(self) -> None:
        try:
            os.remove(self.zip_path)
        except (IOError, OSError):
            pass

    async def serve_zip(self):
        self.app = Quart('test_zip_server')

        @self.app.route('/')
        async def serve_zip():
            return await send_file(self.zip_path, as_attachment=True)

        await self.app.run_task(debug=True, host='localhost', port=49001)

    async def test_project(self):
        actual_test = asyncio.create_task(self.actual_test())
        zip_server_task = asyncio.create_task(self.serve_zip())
        query_embedder_task = asyncio.create_task(embedder_app.run_task(debug=True, host='localhost', port=40100))
        store_embedder_tasks = [asyncio.create_task(embedder_app.run_task(debug=True, host='localhost', port=40200 + i)) for i in (0, 1)]
        downloader_task = asyncio.create_task(downloader_app.run_task(debug=True, host='localhost', port=40001))
        loader_task = asyncio.create_task(loader_app.run_task(debug=True, host='localhost', port=40002))
        loader_worker_tasks = [asyncio.create_task(worker()) for worker in loader_workers]

        tasks = [actual_test, zip_server_task, query_embedder_task, downloader_task, loader_task] + store_embedder_tasks + loader_worker_tasks

        await asyncio.wait(tasks, timeout=30.0, return_when=asyncio.FIRST_COMPLETED)

        actual_test.result()
        for task in tasks:
            if task is not actual_test:
                task.cancel()

    async def actual_test(self):
        await self.small_project()
        await self.medium_project()

    async def small_project(self):
        project = Project(str(uuid.uuid4()))

        await project.download(f'http://127.0.0.1:49001/')

        await self.wait_for_processing(project)

        hits, remarks = await project.search('class Duplicates', 3, 1)
        self.verify_hits(hits, 3, contains=['class Duplicates'])
        self.assertEqual(remarks, [])

        hits, remarks = await project.search('.py', 10, 1)
        self.verify_hits(hits, 6, path='find_duplicates.py')
        self.assertEqual(remarks, [])

        hits, remarks = await project.search('find_duplicates.py', 3, 1)
        self.verify_hits(hits, 3, path='find_duplicates.py')
        self.assertEqual(remarks, [])

        hits, remarks = await project.search('find_duplicates.py class Duplicates', 1, 1)
        self.verify_hits(hits, 1, path='find_duplicates.py', contains=['class Duplicates'])
        self.assertEqual(remarks, [])

        hits, remarks = await project.search('README.md', 10, 1)
        self.verify_hits(hits, 4, path='README.md')
        self.assertEqual(remarks, [])

        await project.delete()

    async def medium_project(self):
        project = Project(str(uuid.uuid4()))

        await project.download(f'https://github.com/viktor-ferenczi/dblayer/archive/refs/tags/0.7.0.zip')

        await self.wait_for_processing(project)

        hits, remarks = await project.search('README.md', 20, 1)
        self.verify_hits(hits, 3, path='README.md')
        self.assertEqual(remarks, [])

        hits, remarks = await project.search('README.md', 20, 2)
        self.verify_hits(hits, 0)

        hits, remarks = await project.search('.py class Query', 10, 1)
        self.verify_hits(hits, 10, contains=['class Query'])
        self.assertEqual(remarks, [])

        hits1, remarks = await project.search('query.py', 20, 1)
        self.verify_hits(hits1, 16, contains=['class Query'])
        self.assertEqual(remarks, [])

        hits2 = []
        for page in range(1, 101):
            hits, remarks = await project.search('query.py', 7, page)
            hits2.extend(hits)
            if len(hits) < 7:
                break
        self.assertEqual(hits1, hits2)

        hits, remarks = await project.search('.py class Query', 50, 50)
        self.verify_hits(hits, 0)

        await project.delete()

    def verify_hits(self, hits: List[Hit], count: int, *, path: str = None, contains: List[str] = None):
        print(f'verify_hits(count={count!r}, path={path!r}, contains={contains!r})')

        try:
            self.assertEqual(len(hits), count)
            self.assertEqual(len(set(hit.uuid for hit in hits)), count)

            if path:
                for hit in hits:
                    self.assertEqual(hit.path, path)

                self.assertEqual(hits, sorted(hits, key=lambda hit: (hit.path, hit.lineno, -hit.score)))

            else:
                self.assertEqual(hits, sorted(hits, key=lambda hit: (-hit.score, hit.path, hit.lineno)))

            if contains:
                for text in contains:
                    self.assertTrue(any((text in hit.text) for hit in hits))
        except AssertionError:
            print()
            print('hits = ')
            pprint.pprint(hits, width=120)
            print()
            raise

    async def wait_for_processing(self, project):
        inventory = Inventory()

        print('Waiting for extracting fragments...')
        while 1:
            if inventory.has_project_extracted(project.project_id):
                break
            await asyncio.sleep(0.2)
        print('Downloaded')

        print('Waiting for embedding fragments...')
        while 1:
            if inventory.has_project_embedded(project.project_id):
                break
            await asyncio.sleep(0.2)
        print('Embedded')
