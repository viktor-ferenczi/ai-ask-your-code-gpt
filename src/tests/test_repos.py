import os
from pprint import pformat
from typing import List

from quart import Quart, send_file

from base_backend_test import BaseBackendTest
from common.constants import C
from common.http import download_into_memory, DownloadResult
from logic.backend import Backend, TInfo, BackendError
from model.fragment import Fragment
from model.hit import Hit
from parsers.registrations import PARSERS_BY_EXTENSION
from storage.fragments import get_all_fragments_in_project, Fragment as DbFragment

REPOS = [
    # Markdown, Python
    ('dblayer', 'https://github.com/viktor-ferenczi/dblayer/archive/refs/tags/0.7.0.zip'),

    # Markdown, Python, GitHub Workflow, YAML
    ('sentient-sims', 'https://github.com/matthewhand/sentient-sims/archive/refs/heads/main.zip'),

    # Markdown, PHP, HTML, CSS, JavaScript
    ('hypedtask', 'https://github.com/thebestbradley/hypedtask/archive/refs/heads/master.zip'),

    # Dropbox, SOL files
    ('redcoin', 'https://www.dropbox.com/s/uw99c6wa2ao1r4b/redcoin.zip?dl=1'),

    # Vim, C, Lua, CMake - THIS IS TOO LONG RIGHT NOW, MAYBE FREEZING
    ('neovim', 'https://github.com/neovim/neovim/archive/refs/heads/master.zip'),

    # C++, CMake
    ('cpp-programming', 'https://github.com/Rustam-Z/cpp-programming/archive/refs/heads/main.zip'),

    # C#, Batch
    ('toolbar-manager', 'https://github.com/viktor-ferenczi/toolbar-manager/archive/refs/heads/main.zip'),

    # Java
    ('Game-of-Life', 'https://github.com/wrthmn/Hyperskill-Game-of-Life/archive/refs/heads/master.zip'),

    # # Python, Shell, JSON, CSV, Python Notebook
    ('tree-of-thought-llm', 'https://github.com/princeton-nlp/tree-of-thought-llm/archive/refs/tags/publish.zip'),

    # Python, Markdown
    ('langchain', 'https://github.com/hwchase17/langchain/archive/refs/heads/master.zip'),

    # TypeScript
    ('hyper', 'https://github.com/vercel/hyper/archive/refs/heads/canary.zip'),

    # Python, C++, CUDA
    ('taso', 'https://github.com/jiazhihao/TASO/archive/refs/heads/master.zip'),

    # TypeScript, JavaScript, HTML
    # FIXME: Crashes tiktoken_len at a data.ts file:
    # \sanity-next\packages\sanity\src\core\form\__workshop__\_common\data.ts
    ('sanity', 'https://github.com/sanity-io/sanity/archive/refs/heads/next.zip'),

    # Part of Unreal: C++, shader
    # http://rebecca.sh/PluginsShadersSourceTargets.zip
    ('unreal', 'http://askyourcode.ai/tests/unreal-xsj037hfd.zip'),

    # Part of Unreal: C++, shader
    ('TLC5916_Lite', 'https://github.com/dpnebert/TLC5916_Lite/archive/refs/heads/main.zip'),

    # TypeScript (.js, .ts, .tsx, .json)
    ('MI_AI_Revised', 'https://github.com/TheGameVIX/MI-AI_Revised/archive/refs/heads/main.zip'),

    # TypeScript (.js, .ts, .tsx, .json)
    ('SE', 'https://ferenczi.eu/download/hf3s90fm7xotvgi74/se-1.202.066.zip'),
][-1:]


def normalize_fragments(fragments: List[Fragment]) -> None:
    for i, fragment in enumerate(fragments):
        fragment.id = 1 + i


def normalize_hits(hits: List[Hit]) -> None:
    for i, hit in enumerate(hits):
        hit.uuid = str(i)


class TestRepos(BaseBackendTest):
    test_script = __file__
    use_multiprocessing = True

    @property
    def test_repos_dir(self):
        return os.path.join(self.data_dir, '_repos')

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
        for name, zip_url in REPOS:
            await self.verify_repo(name, zip_url)

        self.assertAllSucceeded()

    async def verify_repo(self, zip_name: str, zip_url: str):
        self.set_data_subdir(zip_name)

        zip_path = os.path.join(self.test_repos_dir, f'{zip_name}.zip')
        if not os.path.isfile(zip_path):
            download_result: DownloadResult = await download_into_memory(zip_url, max_size=C.MAX_ARCHIVE_SIZE)
            with open(zip_path, 'wb') as zip_file:
                zip_file.write(download_result.body)

        await self.wait_for_processing(300.0)

        backend = await Backend.ensure_project(self.db, 'tester', zip_name)
        local_zip_url = f'http://127.0.0.1:49000/{zip_name}.zip'
        info: TInfo = await backend.download(local_zip_url, timeout=60.0)
        print(info)
        self.assertTrue('Archive downloaded' in info['status'])

        await self.wait_for_processing(900.0)

        hits = await backend.search(path='/readme.md', limit=100)
        normalize_hits(hits)
        self.verify(f'README.md', hits)

        if zip_name == 'dblayer':
            actual = await backend.summarize(path='/lib/dblayer/model', tail='.py', token_limit=999999999)
            self.verify(f'summary-lib-dblayer-model.py', actual)

        if zip_name == 'hypedtask':
            hits = await backend.search(name='Kernel', limit=50)
            normalize_hits(hits)
            self.verify(f'name-Kernel', hits)

            actual = await backend.summarize(path='/public/assets/js', tail='.js', token_limit=999999999)
            self.verify(f'summary-public-assets-js.js', actual)

            actual = await backend.summarize(path='/app', tail='.php', token_limit=999999999)
            self.verify(f'summary-app.php', actual)

        if zip_name == 'langchain':
            hits = await backend.search(name='PromptTemplate', limit=50)
            normalize_hits(hits)
            self.verify(f'name-PromptTemplate', hits)

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

        if zip_name == 'MI_AI_Revised':
            actual = await backend.search(text='ProjectManagerView')
            self.verify(f'search-ProjectManagerView.tsx', actual)
            actual = await backend.summarize(path='/src/pages/index.tsx', token_limit=999999999)
            self.verify(f'summary-index.tsx', actual)

        for extension in PARSERS_BY_EXTENSION:
            actual = await backend.summarize(tail=f'.{extension}', token_limit=999999999)
            if actual:
                self.verify(f'summary.{extension}', actual)

        async with self.db.connection() as conn:
            fragments: List[DbFragment] = await get_all_fragments_in_project(conn, backend.project.id)
        fragments.sort(key=lambda f: (f.document_cs, f.summary, f.category, f.lineno, f.id))
        normalize_fragments(fragments)
        self.verify('all-fragments', fragments)

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
