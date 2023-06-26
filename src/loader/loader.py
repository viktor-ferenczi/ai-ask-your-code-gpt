import asyncio
import os
import sqlite3
import sys
from traceback import print_exc
from typing import Iterator

from quart import Quart

from common.constants import C
from common.doc import find_common_base_dir, remove_common_base_dir
from common.server import run_app
from common.timer import timer
from common.zip_support import extract_verify_documents, iter_files_from_zip
from model.document import Document
from parsers.registrations import TextParser, detect
from project.inventory import Inventory
from project.project import Project

sys.setrecursionlimit(10000)


class Extractor:
    max_fragment_count = 1_000_000

    def __init__(self, inventory: Inventory, project: Project) -> None:
        self.inventory = inventory
        self.project = project

    async def load(self):
        common_base_dir = find_common_base_dir(iter_files_from_zip(self.project.archive_path))
        print(f'Common base dir: {common_base_dir!r}')

        await asyncio.sleep(0)

        with self.project.cursor() as cursor:
            self.project.index_by_path(cursor)
            self.project.index_by_lineno(cursor)
            self.project.index_by_name(cursor)

        with self.project.cursor() as cursor:
            already_inserted_fragment_count = self.project.count_fragments()
            # already_inserted_fragment_keys = set(self.project.get_inserted_fragment_keys(cursor))

        # Quick and dirty shortcut, so failed load attempts are not retried (reason: some of them can get the queue stuck)
        if already_inserted_fragment_count:
            self.inventory.mark_project_extracted(self.project.project_id)
            return

        iter_docs = remove_common_base_dir(common_base_dir, extract_verify_documents(self.project.archive_path))

        batch = []
        batch_size = 256
        fragment_count = 0

        def insert_batch():
            with self.project.cursor() as cursor:
                for f in batch:
                    self.project.insert_fragment(cursor, f)
            batch.clear()

        for fragment in self.iter_fragments_from_documents(iter_docs):

            # fragment_key = (fragment.path, fragment.type, fragment.lineno)
            # if fragment_key in already_inserted_fragment_keys:
            #     continue

            batch.append(fragment)

            if len(batch) >= batch_size:
                insert_batch()
                await asyncio.sleep(0)
                fragment_count += batch_size
                if fragment_count >= self.max_fragment_count:
                    break

        if batch:
            insert_batch()

        self.inventory.mark_project_extracted(self.project.project_id)

    def iter_fragments_from_documents(self, iter_docs: Iterator[Document]):
        for doc in iter_docs:

            parser_cls = detect(doc.path, doc.content)
            if parser_cls is None:
                try:
                    doc.content.decode('ascii')
                except UnicodeDecodeError:
                    # print(f'Skipping unsupported document {doc.path!r} in project {self.project.project_id!r}')
                    continue
                except:  # pragma: no cover
                    print('Unexpected failure during file type detection:')
                    print_exc()
                    continue
                else:
                    # Fallback
                    parser_cls = TextParser

            yield from parser_cls().parse(doc.path, doc.content)


async def extract_worker():
    print('Loader: Fragment extractor worker started')
    inventory = Inventory()
    while 1:
        # noinspection PyBroadException
        try:
            try:
                project_id: str = inventory.get_next_project_to_extract()
            except sqlite3.OperationalError:  # pragma: no cover
                await asyncio.sleep(1.0)
                continue

            if not project_id:
                await asyncio.sleep(0.5)
                continue

            # noinspection PyBroadException
            try:
                project = Project(project_id)
                with timer(f'Extracted fragments of project {project_id!r}'):
                    loader = Extractor(inventory, project)
                    await loader.load()
                fragment_count = project.count_fragments()
                print(f'Fragment count: {fragment_count}')
            except Exception:  # pragma: no cover
                print(f'Failed to load project {project_id!r}')
                print_exc()
                continue

        except Exception:  # pragma: no cover
            print('Unexpected failure')
            print_exc()
            await asyncio.sleep(9)
            continue

        await asyncio.sleep(0)


class Indexer:

    def __init__(self, inventory: Inventory, project: Project) -> None:
        self.inventory = inventory
        self.project = project

    async def index(self):
        with self.project.cursor() as cursor:
            cursor.execute('DROP TABLE IF EXISTS FragText;')
            cursor.execute('CREATE VIRTUAL TABLE FragText USING FTS5(uuid, text);')
            cursor.execute('INSERT INTO FragText (uuid, text) SELECT uuid, text from Fragment;')
            cursor.execute('UPDATE Fragment SET embedded=1;')

        self.inventory.mark_project_embedded(self.project.project_id)


async def indexer_worker():
    print('Loader: Fragment indexer worker started')
    inventory = Inventory()
    while 1:
        # noinspection PyBroadException
        try:
            project_id: str = inventory.get_next_project_to_embed()
            if not project_id:
                await asyncio.sleep(1.0)
                continue

            # noinspection PyBroadException
            try:
                project = Project(project_id)
                fragment_count = project.count_fragments()
                with timer(f'Indexed {fragment_count} fragments for project {project_id!r}', count=fragment_count):
                    indexer = Indexer(inventory, project)
                    await indexer.index()
            except Exception:  # pragma: no cover
                print(f'Failed to index project {project_id!r}, will retry')
                print_exc()
                await asyncio.sleep(5)
                continue

        except Exception:  # pragma: no cover
            print('Unexpected failure')
            print_exc()
            await asyncio.sleep(10)
            continue

        await asyncio.sleep(0)


app = Quart(__name__)
workers = [extract_worker, indexer_worker]


@app.get('/')
async def canary():
    return 'OK', 200


if __name__ == "__main__":
    port = int(os.environ.get('HTTP_PORT', '40002'))
    asyncio.run(run_app(app, *[worker() for worker in workers], host='localhost', port=port, debug=C.DEVELOPMENT))
