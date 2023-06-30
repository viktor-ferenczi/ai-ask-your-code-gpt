import asyncio
import os
from time import time

from quart import Quart, send_file

from base_test_case import BaseTestCase
from services.downloader import app as downloader_app, workers as downloader_workers
from services.extractor import app as extractor_app, workers as extractor_workers
from services.indexer import app as indexer_app, workers as indexer_workers
from storage.scheduler import TaskState

MODULE_DIR = os.path.dirname(__file__)


class BaseBackendTest(BaseTestCase):
    zip_path = ''

    async def serve_zip(self):
        assert self.zip_path

        self.app = Quart('test_zip_server')

        @self.app.route('/test.zip')
        async def serve_zip():
            return await send_file(self.zip_path, as_attachment=True)

        await self.app.run_task(debug=True, host='localhost', port=49000)

    async def coordinate_test(self):
        coroutines = (
                [
                    self.actual_test(),
                    self.serve_zip(),
                    downloader_app.run_task(debug=True, host='localhost', port=40001),
                    extractor_app.run_task(debug=True, host='localhost', port=40002),
                    indexer_app.run_task(debug=True, host='localhost', port=40003),
                ] + [
                    worker() for worker in downloader_workers + extractor_workers + indexer_workers
                ]
        )
        tasks = [asyncio.create_task(coro) for coro in coroutines]

        await asyncio.wait(tasks, timeout=999999.0, return_when=asyncio.FIRST_COMPLETED)

        tasks[0].result()
        for task in tasks[1:]:
            task.cancel()

    async def actual_test(self):
        raise NotImplementedError()

    async def wait_for_processing(self, timeout):
        print('Waiting for all tasks to be processed...')
        deadline = time() + timeout
        while 1:
            count = await self.scheduler.count_tasks(TaskState.pending)
            if not count:
                break

            if time() > deadline:
                raise TimeoutError('Processing has not finished on time')

            print(f'Pending tasks: {count}')
            await asyncio.sleep(1.0)

        print('Processing finished, no pending tasks left.')
