import asyncio
import os
import unittest
import zipfile

from quart import Quart, send_file

from plugin.project import Project, EMBEDDING_CLIENT

MODULE_DIR = os.path.dirname(__file__)


async def run_embedding_server():
    from embed.embedding_server import run_task
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

        done, pending = await asyncio.wait(tasks, timeout=20.0, return_when=asyncio.FIRST_COMPLETED)

        self.assertIn(actual_test, done)
        self.assertIn(zip_server_task, pending)
        self.assertIn(embedding_server_task, pending)

        actual_test.result()
        zip_server_task.cancel()
        embedding_server_task.cancel()

    async def actual_test(self):
        project = Project('test', 'TEST-PROJECT-ID')

        server = await EMBEDDING_CLIENT.find_free_server()
        self.assertIsNotNone(server)

        await project.initialize(f'http://localhost:{self.zip_server_port}/')

        hits = await project.search('class Duplicates', 3)
        self.assertEqual(len(hits), 3)

        scores = [hit.score for hit in hits]
        print(scores)
        self.assertAlmostEqual(scores[0], 0.890, 3)
        self.assertAlmostEqual(scores[1], 0.867, 3)
        self.assertAlmostEqual(scores[2], 0.854, 3)

        hits1 = await project.search('class Duplicates find_duplicates.py', 1)
        self.assertEqual(len(hits1), 1)

        hits2 = await project.search('.py class Duplicates', 1)
        self.assertEqual(len(hits2), 1)

        self.assertTrue(hits1[0].fragment.text.startswith('class Duplicates:'))
        self.assertEqual(hits1[0].fragment.text, hits2[0].fragment.text)

        await project.delete()
