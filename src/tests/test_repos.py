import os
import shutil
from pprint import pformat
from typing import List

from quart import Quart, send_file

from base_backend_test import BaseBackendTest
from common.constants import C
from common.http import download_into_memory
from model.fragment import Fragment
from model.hit import Hit
from parsers.registrations import PARSERS_BY_EXTENSION
from plugin.backend import Backend, TInfo, BackendError
from storage.fragments import get_all_fragments_in_project, Fragment as DbFragment

MODULE_DIR = os.path.dirname(__file__)

REPOS = [
    # Markdown, Python
    # ('dblayer', 'https://github.com/viktor-ferenczi/dblayer/archive/refs/tags/0.7.0.zip'),

    # Markdown, Python, GitHub Workflow, YAML
    # ('sentient-sims', 'https://github.com/matthewhand/sentient-sims/archive/refs/heads/main.zip'),

    # Markdown, PHP, HTML, CSS, JavaScript
    # ('hypedtask', 'https://github.com/thebestbradley/hypedtask/archive/refs/heads/master.zip'),

    # Dropbox, SOL files
    # ('redcoin', 'https://www.dropbox.com/s/uw99c6wa2ao1r4b/redcoin.zip?dl=1'),

    # Vim, C, Lua, CMake - THIS IS TOO LONG RIGHT NOW, MAYBE FREEZING
    # ('neovim', 'https://github.com/neovim/neovim/archive/refs/heads/master.zip'),

    # C++, CMake
    # ('cpp-programming', 'https://github.com/Rustam-Z/cpp-programming/archive/refs/heads/main.zip'),

    # C#, Batch
    # ('toolbar-manager', 'https://github.com/viktor-ferenczi/toolbar-manager/archive/refs/heads/main.zip'),

    # Java
    # ('Game-of-Life', 'https://github.com/wrthmn/Hyperskill-Game-of-Life/archive/refs/heads/master.zip'),

    # # Python, Shell, JSON, CSV, Python Notebook
    # ('tree-of-thought-llm', 'https://github.com/princeton-nlp/tree-of-thought-llm/archive/refs/tags/publish.zip'),

    # Python, Markdown
    ('langchain', 'https://github.com/hwchase17/langchain/archive/refs/heads/master.zip'),

    # TypeScript
    # ('hyper', 'https://github.com/vercel/hyper/archive/refs/heads/canary.zip'),

    # Python, C++, CUDA
    # ('taso', 'https://github.com/jiazhihao/TASO/archive/refs/heads/master.zip'),

    # TypeScript, JavaScript, HTML
    # FIXME: Crashes tiktoken_len at a data.ts file:
    # \sanity-next\packages\sanity\src\core\form\__workshop__\_common\data.ts
    # ('sanity', 'https://github.com/sanity-io/sanity/archive/refs/heads/next.zip'),

    # Part of Unreal: C++, shader
    # http://rebecca.sh/PluginsShadersSourceTargets.zip
    # ('unreal', 'http://askyourcode.ai/tests/unreal-xsj037hfd.zip'),
]


def normalize_fragments(fragments: List[Fragment]):
    for i, fragment in enumerate(fragments):
        fragment.id = -1


def normalize_hits(fragments: List[Hit]):
    for i, fragment in enumerate(fragments):
        fragment.uuid = f'NORMALIZED'


class TestRepos(BaseBackendTest):
    test_repos_dir = os.path.join(MODULE_DIR, '..', 'tests', 'TestRepos')
    use_multiprocessing = True

    async def serve_zip(self):
        self.app = Quart('test_zip_server')

        @self.app.route('/<string:filename>')
        async def serve_zip(filename: str):
            assert '..' not in filename
            assert '/' not in filename
            assert '\\' not in filename
            assert filename.endswith('.zip')
            return await send_file(os.path.join(self.test_repos_dir, filename), as_attachment=True)

        await self.app.run_task(debug=True, host='localhost', port=49000)

    async def test_repos(self):
        await self.coordinate_test()

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

    async def verify_repo(self, zip_name: str, zip_url: str):
        zip_path = os.path.join(self.test_repos_dir, f'{zip_name}.zip')
        if not os.path.isfile(zip_path):
            zip_content, _ = await download_into_memory(zip_url, max_size=C.MAX_ARCHIVE_SIZE)
            with open(zip_path, 'wb') as zip_file:
                zip_file.write(zip_content)

        await self.wait_for_processing(300.0)

        self.project_name = zip_name
        self.project_path = os.path.join(self.test_repos_dir, zip_name)
        self.prepare_test_output_dirs()

        backend = await Backend.ensure_project(self.db, 'tester', zip_name)
        local_zip_url = f'http://127.0.0.1:49000/{zip_name}.zip'
        info: TInfo = await backend.download(local_zip_url, timeout=60.0)
        print(info)
        self.assertTrue('Archive downloaded' in info['status'])

        await self.wait_for_processing(600.0)

        actual = ''.join(hit.text for hit in await backend.search(path='/readme.md', limit=100))
        self.verify(f'README.md', actual)

        if zip_name == 'dblayer':
            actual = await backend.summarize(path='/lib/dblayer/model', tail='.py', token_limit=999999999)
            self.verify(f'summary-lib-dblayer-model.py', actual)

        if zip_name == 'hypedtask':
            actual = '\n'.join(hit.text for hit in await backend.search(name='Kernel', limit=50))
            self.verify(f'name-Kernel', actual)
            actual = await backend.summarize(path='/public/assets/js', tail='.js', token_limit=999999999)
            self.verify(f'summary-public-assets-js.js', actual)
            actual = await backend.summarize(path='/app', tail='.php', token_limit=999999999)
            self.verify(f'summary-app.php', actual)

        if zip_name == 'langchain':
            actual = '\n'.join(hit.text for hit in await backend.search(name='PromptTemplate', limit=50))
            self.verify(f'name-PromptTemplate', actual)

        actual = await backend.summarize(token_limit=999999999)
        self.verify(f'root-summary', actual)

        actual = await backend.summarize(path='/readme.md', token_limit=999999999)
        self.verify(f'README-summary', actual)

        if zip_name == 'redcoin':
            actual = await backend.summarize(tail='.sol', token_limit=999999999)
            self.verify(f'summary.sol', actual)

        if zip_name == 'sentient-sims':
            actual = await backend.summarize(path='/sentient_sims', tail='.py', token_limit=999999999)
            self.verify(f'summary-sentient-sims.py', actual)

        if zip_name == 'toolbar-manager':
            actual = await backend.summarize(path='/ToolbarManager/Gui', tail='.cs', token_limit=999999999)
            self.verify(f'summary-gui.cs', actual)

        if zip_name == 'neovim':
            actual = await backend.summarize(path='/src/nvim', tail='.c', token_limit=999999999)
            self.verify(f'summary-src-nvim.c', actual)
            actual = await backend.summarize(path='/src/nvim', tail='.h', token_limit=999999999)
            self.verify(f'summary-src-nvim.h', actual)

        for extension in PARSERS_BY_EXTENSION:
            actual = await backend.summarize(tail=f'.{extension}', token_limit=999999999)
            if actual:
                self.verify(f'summary.{extension}', actual)

        async with self.db.connection() as conn:
            fragments: List[DbFragment] = await get_all_fragments_in_project(conn, backend.project.id)
        fragments.sort(key=lambda f: (f.document_cs, f.lineno, f.id, f.category, f.summary))
        normalize_fragments(fragments)
        actual = '\n\n'.join(pformat(fragment) for fragment in fragments)
        self.verify('all-fragments', actual)

        if zip_name == 'taso':
            try:
                await backend.search(text='libtaso_runtime.so')
            except BackendError as e:
                self.assertTrue('No hits with this search expression.' in str(e))

            hits = await backend.search(text='using namespace taso', limit=10)
            normalize_hits(hits)
            actual = '\n\n'.join(pformat(hit) for hit in hits)
            self.verify('fts5_using_namespace_taso.txt', actual)

        if zip_name == 'unreal':
            actual = await backend.summarize(path='/Plugins/FX/Niagara', tail='.h')
            self.verify('unreal_niagara_headers.txt', actual)

    def prepare_test_output_dirs(self):
        self.actual_dir = os.path.join(self.project_path, 'actual')
        self.expected_dir = os.path.join(self.project_path, 'expected')

        if os.path.isdir(self.actual_dir):
            shutil.rmtree(self.actual_dir)

        os.makedirs(self.actual_dir)
        os.makedirs(self.expected_dir, exist_ok=True)

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
