import asyncio
import os
import shutil
import unittest
from pprint import pformat
from typing import List

from quart import Quart, send_file

from common.constants import C
from common.http import download_file
from downloader.downloader import app as downloader_app
from loader.loader import app as loader_app, workers as loader_workers
from model.fragment import Fragment
from parsers.registrations import PARSERS_BY_EXTENSION
from project.inventory import Inventory
from project.project import Project, ProjectError

MODULE_DIR = os.path.dirname(__file__)

REPOS = [
    # # Markdown, Python
    # ('dblayer', 'https://github.com/viktor-ferenczi/dblayer/archive/refs/tags/0.7.0.zip'),
    #
    # # Markdown, Python, GitHub Workflow, YAML
    # ('sentient-sims', 'https://github.com/matthewhand/sentient-sims/archive/refs/heads/main.zip'),
    #
    # # Markdown, PHP, HTML, CSS, JavaScript
    # ('hypedtask', 'https://github.com/thebestbradley/hypedtask/archive/refs/heads/master.zip'),
    #
    # # Dropbox, SOL files
    # ('redcoin', 'https://www.dropbox.com/s/uw99c6wa2ao1r4b/redcoin.zip?dl=1'),
    #
    # # Vim, C, Lua, CMake - THIS IS TOO LONG RIGHT NOW, MAYBE FREEZING
    # ('neovim', 'https://github.com/neovim/neovim/archive/refs/heads/master.zip'),
    #
    # # C++, CMake
    ('cpp-programming', 'https://github.com/Rustam-Z/cpp-programming/archive/refs/heads/main.zip'),
    #
    # # C#, Batch
    # ('toolbar-manager', 'https://github.com/viktor-ferenczi/toolbar-manager/archive/refs/heads/main.zip'),
    #
    # # Java
    # ('Game-of-Life', 'https://github.com/wrthmn/Hyperskill-Game-of-Life/archive/refs/heads/master.zip'),
    #
    # # Python, Shell, JSON, CSV, Python Notebook
    # ('tree-of-thought-llm', 'https://github.com/princeton-nlp/tree-of-thought-llm/archive/refs/tags/publish.zip'),
    #
    # # Python, Markdown
    # ('langchain', 'https://github.com/hwchase17/langchain/archive/refs/heads/master.zip'),

    # TypeScript
    # ('hyper', 'https://github.com/vercel/hyper/archive/refs/heads/canary.zip'),

    # Python, C++, CUDA
    # ('taso', 'https://github.com/jiazhihao/TASO/archive/refs/heads/master.zip'),

    # TypeScript, JavaScript, HTML
    # FIXME: Crashes tiktoken_len at a data.ts file:
    # \sanity-next\packages\sanity\src\core\form\__workshop__\_common\data.ts
    # ('sanity', 'https://github.com/sanity-io/sanity/archive/refs/heads/next.zip'),

    # Part of Unreal: C++, shader
    # ('unreal', 'http://rebecca.sh/PluginsShadersSourceTargets.zip'),
]


def normalize_fragments(fragments: List[Fragment]):
    for i, fragment in enumerate(fragments):
        fragment.uuid = f'NORMALIZED-{i:06d}'


class TestProject(unittest.IsolatedAsyncioTestCase):
    test_repos_dir = os.path.join(MODULE_DIR, '..', 'tests', 'TestRepos')

    def setUp(self) -> None:
        self.maxDiff = 32768

        Inventory.filename = 'test-inventory.sqlite'
        inventory = Inventory()
        inventory.drop_database()

        Project.dirname = 'test-projects'
        test_projects_dir = os.path.join(C.DATA_DIR, Project.dirname)
        if os.path.isdir(test_projects_dir):
            shutil.rmtree(test_projects_dir)

    async def serve_zip(self):
        self.app = Quart('test_zip_server')

        @self.app.route('/<string:filename>')
        async def serve_zip(filename: str):
            assert '..' not in filename
            assert '/' not in filename
            assert '\\' not in filename
            assert filename.endswith('.zip')
            return await send_file(os.path.join(self.test_repos_dir, filename), as_attachment=True)

        await self.app.run_task(debug=True, host='localhost', port=49001)

    async def test_repos(self):
        actual_test = asyncio.create_task(self.actual_test())
        zip_server_task = asyncio.create_task(self.serve_zip())
        downloader_task = asyncio.create_task(downloader_app.run_task(debug=True, host='localhost', port=40001))
        loader_task = asyncio.create_task(loader_app.run_task(debug=True, host='localhost', port=40002))
        loader_worker_tasks = [asyncio.create_task(worker()) for worker in loader_workers]

        tasks = [actual_test, zip_server_task, downloader_task, loader_task] + loader_worker_tasks

        await asyncio.wait(tasks, timeout=999999.0, return_when=asyncio.FIRST_COMPLETED)

        actual_test.result()
        for task in tasks:
            if task is not actual_test:
                task.cancel()

    async def actual_test(self):
        self.failures = []
        for name, zip_url in REPOS:
            await self.verify_repo(name, zip_url)

        if self.failures:
            for project_name, name, expected, actual in self.failures:
                # print('=' * 70)
                print(f'FAILED: {project_name} / {name}')
                # print('=' * 70)
                # for line in difflib.unified_diff(expected.split('\n'), actual.split('\n')):
                #     print(line)
                # print()

            self.fail('One of more output were not what was expected. See above.')

    async def verify_repo(self, name: str, zip_url: str):
        zip_path = os.path.join(self.test_repos_dir, f'{name}.zip')
        if not os.path.isfile(zip_path):
            zip_content, _ = await download_file(zip_url, max_size=C.MAX_ARCHIVE_SIZE)
            with open(zip_path, 'wb') as zip_file:
                zip_file.write(zip_content)

        self.project_name = name
        self.project_path = os.path.join(self.test_repos_dir, name)
        os.makedirs(f'{self.project_path}/actual', exist_ok=True)
        os.makedirs(f'{self.project_path}/expected', exist_ok=True)

        local_zip_url = f'http://127.0.0.1:49001/{name}.zip'
        project_id = await Project.download(local_zip_url)
        project = Project(project_id)

        await self.wait_for_processing(project)

        actual = ''.join(hit.text for hit in await project.search(path='/readme.md', limit=50))
        self.verify(f'README.md', actual)

        if name == 'hypedtask':
            actual = '\n'.join(hit.text for hit in await project.search(name='Kernel', limit=50))
            self.verify(f'name-Kernel', actual)

        if name == 'langchain':
            actual = '\n'.join(hit.text for hit in await project.search(name='PromptTemplate', limit=50))
            self.verify(f'name-PromptTemplate', actual)

        actual = await project.summarize(token_limit=999999999)
        self.verify(f'root-summary', actual)

        actual = await project.summarize(path='/readme.md', token_limit=999999999)
        self.verify(f'README-summary', actual)

        if name == 'redcoin':
            actual = await project.summarize(tail='.sol', token_limit=999999999)
            self.verify(f'summary.sol', actual)

        for extension in PARSERS_BY_EXTENSION:
            actual = await project.summarize(tail=f'.{extension}', token_limit=999999999)
            if actual:
                self.verify(f'summary.{extension}', actual)

        with project.cursor() as cursor:
            fragments = project.get_all_fragments(cursor)
            normalize_fragments(fragments)
        actual = '\n\n'.join(pformat(fragment) for fragment in fragments)
        self.verify('all-fragments', actual)

        if name == 'taso':
            try:
                await project.search(text='libtaso_runtime.so')
            except ProjectError as e:
                self.assertTrue('No hits with this search expression.' in str(e))

            hits = await project.search(text='using namespace taso', limit=10)
            normalize_fragments(hits)
            actual = '\n\n'.join(pformat(hit) for hit in hits)
            self.verify('fts5_using_namespace_taso.txt', actual)

        if name == 'unreal':
            actual = await project.summarize(path='/Plugins/FX/Niagara', tail='.h')
            self.verify('unreal_niagara_headers.txt', actual)

        pass

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

    def verify(self, name: str, actual: str):
        if len(actual) >= 50_000_000:

            half = len(actual) // 2
            while actual[half] != '\n':
                half += 1
            half += 1

            self.verify(f'{name}-1', actual[:half])
            self.verify(f'{name}-2', actual[half:])
            return

        actual_path = os.path.join(self.project_path, 'actual', f'{name}.txt')
        expected_path = os.path.join(self.project_path, 'expected', f'{name}.txt')

        good = False
        if not os.path.exists(expected_path):
            expected = ''
        else:
            with open(expected_path, 'rt', encoding='utf-8') as f:
                expected = f.read()
            good = actual == expected

        if good:
            if os.path.exists(actual_path):
                os.remove(actual_path)
        else:
            with open(actual_path, 'wb') as f:
                f.write(actual.encode('utf-8', errors='replace'))

            self.failures.append((self.project_name, name, expected, actual))
