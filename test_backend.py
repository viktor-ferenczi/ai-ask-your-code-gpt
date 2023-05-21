import asyncio
import os
import unittest
import zipfile

from quart import Quart, send_file

import backend


class TestBackend(unittest.IsolatedAsyncioTestCase):
    zip_path = 'TestProject.zip'
    port = 31854

    def setUp(self) -> None:
        with zipfile.ZipFile(self.zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            test_project_dir = 'TestProject'
            for root, dirs, files in os.walk(test_project_dir):
                for filename in files:
                    path = os.path.join(root, filename)
                    archive_path = path[len(test_project_dir) + 1:]
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

        await self.app.run_task(debug=True, host='127.0.0.1', port=self.port)

    async def test_download_search_delete(self):
        await self.download()
        await self.search()
        await self.delete()

    async def download(self):
        server_task = asyncio.create_task(self.serve_zip())
        download_task = asyncio.create_task(backend.download('test', f'http://127.0.0.1:{self.port}/'))
        done, pending = await asyncio.wait([server_task, download_task], timeout=10.0, return_when=asyncio.FIRST_COMPLETED)
        print(done)
        print(pending)
        self.project_id = download_task.result()
        server_task.cancel()

    async def search(self):
        results = await backend.search('test', self.project_id, text='class Duplicates')
        print(results)

    async def delete(self):
        await backend.delete('test', self.project_id)
        with self.assertRaises(ValueError):
            await self.search()
