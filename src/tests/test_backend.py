import asyncio
import os
import pprint
import shutil
import unittest
import zipfile
from typing import List

from quart import Quart, send_file

from common.constants import C
from downloader.downloader import app as downloader_app, workers as downloader_workers
from loader.extractor import app as loader_app, workers as loader_workers
from model.hit import Hit
from project.inventory import Inventory
from project.backend import Project, ProjectError

MODULE_DIR = os.path.dirname(__file__)


class TestProject(unittest.IsolatedAsyncioTestCase):
    test_project_dir = os.path.join(MODULE_DIR, '..', 'tests', 'TestProject')
    zip_path = os.path.join(MODULE_DIR, 'TestProject.zip')

    def setUp(self) -> None:
        self.maxDiff = 32768

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

    def test_download_server_not_running(self):
        def should_fail():
            asyncio.run(Project.create('http://127.0.0.1:57575/anything', timeout=1.0))

        self.assertRaises(ProjectError, should_fail)

    async def serve_zip(self):
        self.app = Quart('test_zip_server')

        @self.app.route('/test.zip')
        async def serve_zip():
            return await send_file(self.zip_path, as_attachment=True)

        await self.app.run_task(debug=True, host='localhost', port=49001)

    async def test_project(self):
        actual_test = asyncio.create_task(self.actual_test())
        zip_server_task = asyncio.create_task(self.serve_zip())
        downloader_task = asyncio.create_task(downloader_app.run_task(debug=True, host='localhost', port=40001))
        loader_task = asyncio.create_task(loader_app.run_task(debug=True, host='localhost', port=40002))
        loader_worker_tasks = [asyncio.create_task(worker()) for worker in loader_workers]
        downloader_worker_tasks = [asyncio.create_task(worker()) for worker in downloader_workers]

        tasks = [actual_test, zip_server_task, downloader_task, loader_task] + loader_worker_tasks + downloader_worker_tasks

        await asyncio.wait(tasks, timeout=999999.0, return_when=asyncio.FIRST_COMPLETED)

        actual_test.result()
        for task in tasks:
            if task is not actual_test:
                task.cancel()

    async def actual_test(self):
        await self.download_error()

        # project_id = await self.github_user_content()
        # project = Project(project_id)
        # self.assertTrue(project.exists)
        # await project.delete()
        # self.assertFalse(project.exists)

        small_project_id = await self.small_project()

        project = Project(small_project_id)
        self.assertTrue(project.exists)
        await project.cleanup()
        self.assertFalse(project.exists)

        medium_project_id_1 = await self.medium_project()
        self.assertNotEquals(small_project_id, medium_project_id_1)
        project = Project(medium_project_id_1)

        await self.medium_project(medium_project_id_1)

        await project.cleanup()
        self.assertFalse(project.exists)

        await self.medium_project(medium_project_id_1, False)

        await project.delete()
        self.assertFalse(project.exists)

        medium_project_id_2 = await self.medium_project()
        self.assertNotEquals(medium_project_id_1, medium_project_id_2)

        project = Project(medium_project_id_2)
        await project.delete()
        self.assertFalse(project.exists)

    async def download_error(self):
        try:
            await Project.create('http://127.0.0.1:49001/this-wont-exist')
        except ProjectError as e:
            self.assertTrue('Failed to download' in str(e))
        else:
            self.fail("ProjectError not raised")

    async def small_project(self) -> str:
        project_id = await Project.create('http://127.0.0.1:49001/test.zip')
        project = Project(project_id)

        await self.wait_for_processing(project)

        hits = await project.search(tail='.py', name='Duplicates')
        self.verify_hits(hits, 1, contains=['class Duplicates'])

        hits = await project.search(path='/find_duplicates.py', limit=100)
        self.verify_hits(hits, 34, path='/find_duplicates.py')

        hits = await project.search(tail='.py', path='/find_duplicates.py', limit=100)
        self.verify_hits(hits, 34, path='/find_duplicates.py')

        hits = await project.search(path='/README.md', limit=100)
        self.verify_hits(hits, 5, path='/README.md')

        hits = await project.search(tail='.md', text='standard set of source code files', limit=1)
        self.verify_hits(hits, 1, path='/README.md', contains=['standard set of source code files'])

        hits = await project.search(text='class Duplicates', limit=10)
        self.verify_hits(hits, 2, path='/find_duplicates.py', contains=['class Duplicates:'])
        self.assertEqual(len([hit for hit in hits if hit.type == 'module']), 1)
        self.assertEqual(len([hit for hit in hits if hit.type == 'class']), 1)
        self.verify_hits(hits[:1], 1, path='/find_duplicates.py', contains=['class Duplicates:'])
        self.verify_hits(hits[1:], 1, path='/find_duplicates.py', contains=['class Duplicates:'])

        summary = await project.summarize(tail='.md')
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

        summary = await project.summarize(tail='.py')
        self.assertEqual('''\
File extensions: .py

Python: /find_duplicates.py
  Functions: main md5_checksum
  Classes: Duplicates
  Methods: __init__ collect
  Variables and usages: CHUNK_SIZE ProcessPoolExecutor append collections concurrent data defaultdict desc dirpath duplicates executor extend file_checksum file_checksums file_list file_path file_size filename filenames files files_by_checksum files_by_size first futures getsize hasher hashlib hexdigest input isdir items join open path pbar print read root_dir total total_size total_space_saved tqdm unit unit_scale update values walk

''', summary)

        return project_id

    async def medium_project(self, expect_project_id: str = '', expect_already_embedded: bool = True) -> str:
        project_id = await Project.create('https://github.com/viktor-ferenczi/dblayer/archive/refs/tags/0.7.0.zip')
        project = Project(project_id)

        if expect_project_id:
            self.assertEqual(project_id, expect_project_id)

        if not expect_project_id or not expect_already_embedded:
            await self.wait_for_processing(project)

        progress = await project.get_progress()
        self.assertEqual(progress, 100)

        hits = await project.search(path='/README.md', limit=100)
        self.verify_hits(hits, 9, path='/README.md')

        hits = await project.search(tail='.py', name='Query', limit=100)
        self.verify_hits(hits, 34, contains=['class Query'])

        summary = await project.summarize(tail='.md')
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

        summary = await project.summarize(path='/lib/dblayer', tail='.py')
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

        return project.project_name

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
            if inventory.has_project_extracted(project.project_name):
                break
            await asyncio.sleep(0.2)
        print('Downloaded')

        print('Waiting for embedding fragments...')
        while 1:
            if inventory.has_project_embedded(project.project_name):
                break
            await asyncio.sleep(0.2)
        print('Embedded')

    # async def github_user_content(self) -> str:
    #     url = 'https://raw.githubusercontent.com/manbearwiz/youtube-dl-server/main/youtube-dl-server.py'
    #     project_id = await Project.download(url)
    #     project = Project(project_id)
    #
    #     await self.wait_for_processing(project)
    #
    #     hits = await project.search(tail='.py')
    #     self.assertTrue(len(hits) > 0)
    #
    #     return project_id
