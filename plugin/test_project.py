import asyncio
import os
import unittest
import zipfile

from quart import Quart, send_file

from project import Project, EMBEDDING_CLIENT

MODULE_DIR = os.path.dirname(__file__)


class TestPlugin(unittest.IsolatedAsyncioTestCase):
    test_project_dir = os.path.join(MODULE_DIR, '..', 'tests', 'TestProject')
    zip_path = os.path.join(MODULE_DIR, 'TestProject.zip')
    zip_server_port = 31854
    embedding_server_port = 41246

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

    async def run_embedding_server(self):
        from embed.embedding_server import app
        await app.run_task(debug=True, host='localhost', port=self.embedding_server_port)

    async def test_project(self):
        embedding_server_task = asyncio.create_task(self.run_embedding_server())
        zip_server_task = asyncio.create_task(self.serve_zip())
        actual_test = asyncio.create_task(self.actual_test())

        tasks = [
            embedding_server_task,
            zip_server_task,
            actual_test
        ]

        done, pending = await asyncio.wait(tasks, timeout=30.0, return_when=asyncio.FIRST_COMPLETED)

        self.assertIn(actual_test, done)
        self.assertIn(zip_server_task, pending)
        self.assertIn(embedding_server_task, pending)

        actual_test.result()
        zip_server_task.cancel()
        embedding_server_task.cancel()

    async def actual_test(self):
        project = Project('test', 'TEST-PROJECT-ID')

        await EMBEDDING_CLIENT.find_free_server()

        await project.initialize(f'http://localhost:{self.zip_server_port}/')

        hits = await project.search('class Duplicates', 3)
        self.assertEqual(len(hits), 3)

        scores = [hit.score for hit in hits]

        self.assertAlmostEqual(scores[0], 0.898, 3)
        self.assertAlmostEqual(scores[1], 0.847, 3)
        self.assertAlmostEqual(scores[2], 0.840, 3)

        await project.delete()
