import asyncio
import os
import pprint
import unittest
import zipfile
from typing import List

from quart import Quart, send_file

from model.hit import Hit
from plugin.project import Project, EMBEDDING_CLIENT

MODULE_DIR = os.path.dirname(__file__)


async def run_embedding_server():
    from embed.embedder import run_task
    await run_task()


class TestPlugin(unittest.IsolatedAsyncioTestCase):
    test_project_dir = os.path.join(MODULE_DIR, '..', 'tests', 'TestProject')
    zip_path = os.path.join(MODULE_DIR, 'TestProject.zip')
    zip_server_port = 31854

    def setUp(self) -> None:
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
        # Prepare the Quart app and the route to serve the zip file
        self.app = Quart(__name__)

        @self.app.route('/')
        async def serve_zip():
            # Create a Zip file from TestProject directory

            return await send_file(self.zip_path, as_attachment=True)

        await self.app.run_task(debug=True, host='localhost', port=self.zip_server_port)

    async def test_project(self):
        embedding_server_task = asyncio.create_task(run_embedding_server())
        zip_server_task = asyncio.create_task(self.serve_zip())
        actual_test = asyncio.create_task(self.actual_test())

        tasks = [
            embedding_server_task,
            zip_server_task,
            actual_test
        ]

        done, pending = await asyncio.wait(tasks, timeout=60.0, return_when=asyncio.FIRST_COMPLETED)

        self.assertIn(actual_test, done)
        self.assertIn(zip_server_task, pending)
        self.assertIn(embedding_server_task, pending)

        actual_test.result()
        zip_server_task.cancel()
        embedding_server_task.cancel()

    async def actual_test(self):
        await self.small_project()
        await self.medium_project()

    async def small_project(self):
        project = Project('SMALL-TEST-PROJECT-ID')

        server = await EMBEDDING_CLIENT.find_free_server()
        self.assertIsNotNone(server)

        await project.download(f'http://localhost:{self.zip_server_port}/')

        hits = await project.search('class Duplicates', 3)
        self.verify_hits(hits, 3, contains=['class Duplicates'])

        hits = await project.search('.py', 10)
        self.verify_hits(hits, 6, path='find_duplicates.py')

        hits = await project.search('find_duplicates.py', 3)
        self.verify_hits(hits, 3, path='find_duplicates.py')

        hits = await project.search('find_duplicates.py class Duplicates', 1)
        self.verify_hits(hits, 1, path='find_duplicates.py', contains=['class Duplicates'])

        hits = await project.search('README.md', 10)
        self.verify_hits(hits, 4, path='README.md')

        await project.delete()

    async def medium_project(self):
        project = Project('MEDIUM-TEST-PROJECT-ID')

        server = await EMBEDDING_CLIENT.find_free_server()
        self.assertIsNotNone(server)

        await project.download(f'https://github.com/viktor-ferenczi/dblayer/archive/refs/tags/0.7.0.zip')

        hits = await project.search('README.md', 20)
        self.verify_hits(hits, 3, path='README.md')

        hits = await project.search('class Query', 10)
        self.verify_hits(hits, 10, contains=['class Query'])

        await project.delete()

    def verify_hits(self, hits: List[Hit], count: int, *, path: str = None, contains: List[str] = None):
        print(f'verify_hits(count={count!r}, path={path!r}, contains={contains!r})')

        self.assertEqual(len(hits), count)
        self.assertEqual(len(set(hit.fragment.uuid for hit in hits)), count)

        if path:
            for hit in hits:
                self.assertEqual(hit.fragment.path, path)

            self.assertEqual(hits, sorted(hits, key=lambda hit: (hit.fragment.path, hit.fragment.lineno, -hit.score)))

        else:
            self.assertEqual(hits, sorted(hits, key=lambda hit: -hit.score))

        if contains:
            for text in contains:
                self.assertTrue(any((text in hit.fragment.text) for hit in hits))
