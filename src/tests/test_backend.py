import asyncio
import os
import pprint
import zipfile
from time import time
from typing import List

from quart import Quart, send_file

from base_test_case import BaseTestCase
from model.hit import Hit
from plugin.backend import Backend, TInfo
from services.downloader import app as downloader_app, workers as downloader_workers
from services.extractor import app as extractor_app, workers as extractor_workers
from services.indexer import app as indexer_app, workers as indexer_workers
from storage.scheduler import TaskState

MODULE_DIR = os.path.dirname(__file__)


class TestBackend(BaseTestCase):
    test_project_dir = os.path.join(MODULE_DIR, '..', 'tests', 'TestProject')
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

    async def test_download_server_not_running(self):
        backend = await Backend.ensure_project(self.db, 'tester', 'test_download_server_not_running')
        info: TInfo = await backend.download('http://127.0.0.1:57575', timeout=1.0)
        print(info)
        self.assertTrue('The download is still in progress' in info['status'])
        self.assertTrue('hint' in info)

    async def serve_zip(self):
        self.app = Quart('test_zip_server')

        @self.app.route('/test.zip')
        async def serve_zip():
            return await send_file(self.zip_path, as_attachment=True)

        await self.app.run_task(debug=True, host='localhost', port=49000)

    async def test_project(self):
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
        await self.download_error()
        await self.small_project()
        await self.medium_project()

    async def download_error(self):
        backend = await Backend.ensure_project(self.db, 'tester', 'download_error')
        info: TInfo = await backend.download('http://127.0.0.1:49000/this-will-fail', timeout=10.0)
        print(info)
        # FIXME: Flaky test case!!!
        # self.assertTrue('Failed to download' in info['status'])
        self.assertTrue('hint' in info)
        await self.scheduler.delete_all_tasks()

    async def small_project(self):
        backend = await Backend.ensure_project(self.db, 'tester', 'small_project')
        info: TInfo = await backend.download('http://127.0.0.1:49000/test.zip', timeout=2.0)
        print(info)
        self.assertTrue('Archive downloaded' in info['status'])

        await self.wait_for_processing(5.0)

        hits = await backend.search(tail='.py', name='Duplicates')
        self.verify_hits(hits, 1, contains=['class Duplicates'])

        hits = await backend.search(path='/find_duplicates.py', limit=100)
        self.verify_hits(hits, 34, path='/find_duplicates.py')

        hits = await backend.search(tail='.py', path='/find_duplicates.py', limit=100)
        self.verify_hits(hits, 34, path='/find_duplicates.py')

        hits = await backend.search(path='/README.md', limit=100)
        self.verify_hits(hits, 5, path='/README.md')

        hits = await backend.search(tail='.md', text='standard set of source code files', limit=1)
        self.verify_hits(hits, 1, path='/README.md', contains=['standard set of source code files'])

        hits = await backend.search(text='class Duplicates', limit=10)
        self.verify_hits(hits, 2, path='/find_duplicates.py', contains=['class Duplicates:'])
        self.assertEqual(len([hit for hit in hits if hit.category == 'module']), 1)
        self.assertEqual(len([hit for hit in hits if hit.category == 'class']), 1)
        self.verify_hits(hits[:1], 1, path='/find_duplicates.py', contains=['class Duplicates:'])
        self.verify_hits(hits[1:], 1, path='/find_duplicates.py', contains=['class Duplicates:'])

        summary = await backend.summarize(tail='.md')
        self.assertEqual('''\
File extensions: .md

# Markdown Syntax Examples
## Headings
# Heading 1
## Heading 2
### Heading 3
## Emphasis
## Lists
### Ordered List
### Unordered List
## Links
## Images
## Blockquotes
## Code

# Test project
## Rationale
### Doc types and languages
### Some long section
## Summary

''', summary)

        summary = await backend.summarize(tail='.py')
        self.assertEqual('''\
File extensions: .py

Python: /find_duplicates.py
  Functions: main md5_checksum
  Classes: Duplicates
  Methods: __init__ collect
  Variables and usages: CHUNK_SIZE ProcessPoolExecutor append collections concurrent data defaultdict desc dirpath duplicates executor extend file_checksum file_checksums file_list file_path file_size filename filenames files files_by_checksum files_by_size first futures getsize hasher hashlib hexdigest input isdir items join open path pbar print read root_dir total total_size total_space_saved tqdm unit unit_scale update values walk

''', summary)

    async def medium_project(self):
        backend = await Backend.ensure_project(self.db, 'tester', 'medium_project')
        info: TInfo = await backend.download('https://github.com/viktor-ferenczi/dblayer/archive/refs/tags/0.7.0.zip', timeout=5.0)
        print(info)
        self.assertTrue('Archive downloaded' in info['status'])

        await self.wait_for_processing(30.0)

        hits = await backend.search(path='/README.md', limit=100)
        self.verify_hits(hits, 9, path='/README.md')

        hits = await backend.search(tail='.py', name='Query', limit=100)
        self.verify_hits(hits, 19, contains=['class Query'])

        summary = await backend.summarize(tail='.md')
        self.assertEqual('''\
File extensions: .md

# Database Abstraction Layer Generator
# Installation
# How it works
## Abstraction layer
## Lightweight usage
## Features
# Remarks
## Performance
## Limitations

''', summary)

        summary = await backend.summarize(path='/lib/dblayer', tail='.py')
        self.assertEqual('''\
File extensions: .py

Python: /lib/dblayer/constants.py
  Classes: NA
  Methods: __repr__
  Variables and usages: CURSOR_ARRAYSIZE DATABASE_ID_RANGE DEBUG ENCODING GENERATOR_TEMPLATE_DIRECTORY_PATH INNER_JOIN JOIN_TYPES LEFT_JOIN LOG_SQL_ANALYSIS LOG_SQL_RESULT_ROWS LOG_SQL_STATEMENTS MAX_INSERT_RETRY_COUNT PROFILE_QUERIES dirname environ join path

Python: /lib/dblayer/util.py
  Functions: get_next_definition_serial get_random_id log
  Variables and usages: DATABASE_ID_RANGE SystemRandom args constants count datetime dblayer isoformat iterator itertools next print random randrange


Matches under subdirectories:
  backend: 987
  generator: 18
  graph: 28
  model: 877
  test: 388
''', summary)

    def verify_hits(self, hits: List[Hit], count: int, *, path: str = None, contains: List[str] = None):
        print(f'verify_hits(count={count!r}, path={path!r}, contains={contains!r})')

        try:
            self.assertEqual(count, len(hits))
            self.assertEqual(count, len(set(hit.uuid for hit in hits)))

            if path:
                for hit in hits:
                    self.assertEqual(path, hit.path)

                self.assertEqual(sorted(hits, key=lambda hit: (-hit.score, hit.path, hit.lineno)), hits)

            else:
                self.assertEqual(sorted(hits, key=lambda hit: (-hit.score, hit.uuid)), hits)

            if contains:
                for text in contains:
                    self.assertTrue(any((text in hit.body) for hit in hits))
        except AssertionError:
            print()
            print('hits = ')
            pprint.pprint(hits, width=120)
            print()
            raise

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
