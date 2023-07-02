import asyncio
import multiprocessing
import os
from pprint import pprint
from time import time
from typing import List

from quart import Quart, send_file

from base_test_case import BaseTestCase
from services.downloader import app as downloader_app, workers as downloader_workers
from services.extractor import app as extractor_app, workers as extractor_workers
from services.indexer import app as indexer_app, workers as indexer_workers, main as indexer_main
from storage.scheduler import TaskState

MODULE_DIR = os.path.dirname(__file__)


class BaseBackendTest(BaseTestCase):
    zip_path = ''
    indexer_count = os.cpu_count()
    use_multiprocessing = False

    async def serve_zip(self):
        assert self.zip_path

        self.app = Quart('test_zip_server')

        @self.app.route('/test.zip')
        async def serve_zip():
            return await send_file(self.zip_path, as_attachment=True)

        await self.app.run_task(debug=True, host='localhost', port=49000)

    async def coordinate_test(self):
        processes: List[multiprocessing.Process] = []
        if self.use_multiprocessing:
            processes = [
                multiprocessing.Process(target=indexer_main, args=(53000 + index,))
                for index in range(1, self.indexer_count)
            ]
            for process in processes:
                process.start()

        try:
            coroutines = (
                    [
                        self.actual_test(),
                        self.serve_zip(),
                        downloader_app.run_task(debug=True, host='localhost', port=51000),
                        extractor_app.run_task(debug=True, host='localhost', port=52000),
                        indexer_app.run_task(debug=True, host='localhost', port=53000),
                    ] + [
                        worker() for worker in downloader_workers + extractor_workers + indexer_workers
                    ]
            )
            tasks = [asyncio.create_task(coro) for coro in coroutines]

            await asyncio.wait(tasks, timeout=999999.0, return_when=asyncio.FIRST_COMPLETED)

            tasks[0].result()
            for task in tasks[1:]:
                task.cancel()
        finally:
            for process in processes:
                process.kill()
            processes.clear()

    async def actual_test(self):
        raise NotImplementedError()

    async def wait_for_processing(self, timeout):
        print('Waiting for all tasks to be processed...')
        started = time()
        deadline = started + timeout
        while 1:
            count = await self.scheduler.count_tasks(TaskState.pending)
            if not count:
                break

            if time() > deadline:
                raise TimeoutError('Processing has not finished on time')

            print(f'Pending tasks: {count}')
            await asyncio.sleep(1.0)

        duration = time() - started
        print(f'Processed all tasks in {duration:.3f}s')

        good = True
        for task in await self.scheduler.get_all_tasks():
            if task.state != TaskState.completed:
                if good:
                    print('Failed tasks:')
                pprint(task)
                good = False

        self.assertTrue(good, 'Failed tasks, see above.')
