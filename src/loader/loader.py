import asyncio
import os
from traceback import print_exc
from typing import Iterator, List

import numpy as np
from aiohttp import ServerDisconnectedError
from quart import Quart

import parsers
from common.constants import C
from common.doc import find_common_base_dir, remove_common_base_dir
from common.server import run_app
from common.timer import timer
from common.zip_support import extract_verify_documents, iter_files_from_zip
from model.document import Document
from parsers import TextParser
from project.inventory import Inventory
from project.project import Project


class Extractor:

    def __init__(self, inventory: Inventory, project: Project) -> None:
        self.inventory = inventory
        self.project = project

    async def load(self):
        common_base_dir = find_common_base_dir(iter_files_from_zip(self.project.archive_path))
        print(f'Common base dir: {common_base_dir!r}')

        await asyncio.sleep(0)

        with self.project.cursor() as cursor:
            self.project.index_by_path(cursor)

        with self.project.cursor() as cursor:
            iter_docs = remove_common_base_dir(common_base_dir, extract_verify_documents(self.project.archive_path))

            for fragment in self.iter_fragments_from_documents(iter_docs):
                self.project.insert_fragment(cursor, fragment)
                await asyncio.sleep(0)

        with self.project.cursor() as cursor:
            self.project.index_by_lineno(cursor)
            self.project.index_by_name(cursor)

        self.inventory.mark_project_extracted(self.project.project_id)

    def iter_fragments_from_documents(self, iter_docs: Iterator[Document]):
        for doc in iter_docs:

            parser_cls = parsers.detect(doc.path, doc.content)
            if parser_cls is None:
                try:
                    doc.content.decode('ascii')
                except UnicodeDecodeError:
                    # print(f'Skipping unsupported document {doc.path!r} in project {self.project.project_id!r}')
                    continue
                except:
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
            project_id: str = inventory.get_next_project_to_extract()
            if not project_id:
                await asyncio.sleep(1.0)
                continue

            # noinspection PyBroadException
            try:
                project = Project(project_id)
                with timer(f'Extracted fragments of project {project_id!r}'):
                    loader = Extractor(inventory, project)
                    await loader.load()
                fragment_count = project.count_fragments()
                print(f'Fragment count: {fragment_count}')
            except KeyboardInterrupt:
                raise
            except Exception:
                print(f'Failed to load project {project_id!r}, removed it from the inventory')
                print_exc()
                inventory.delete_project(project_id)
                continue

        except KeyboardInterrupt:
            raise
        except Exception:
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
                with timer(f'Indexing {fragment_count} fragments for project {project_id!r}', count=fragment_count):
                    indexer = Indexer(inventory, project)
                    await indexer.index()
            except KeyboardInterrupt:
                raise
            except Exception:
                print(f'Failed to index project {project_id!r}, will retry')
                print_exc()
                await asyncio.sleep(5)
                continue

        except KeyboardInterrupt:
            raise
        except Exception:
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
