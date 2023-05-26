import asyncio
import os
from traceback import print_exc
from typing import Iterator, List

from quart import Quart

import doc_types
from common.doc import find_common_base_dir, remove_common_base_dir
from common.server import run_app
from common.timer import timer
from common.zip_support import extract_verify_documents, iter_files_from_zip
from embed.embedder_client import EmbedderClient, STORE_EMBEDDERS
from model.document import Document
from model.fragment import Fragment
from project.inventory import Inventory
from project.project import Project

EMBEDDER_CLIENT = EmbedderClient(STORE_EMBEDDERS)


class Extractor:

    def __init__(self, inventory: Inventory, project: Project) -> None:
        self.inventory = inventory
        self.project = project

    async def load(self):
        common_base_dir = find_common_base_dir(iter_files_from_zip(self.project.archive_path))
        print(f'Common base dir: {common_base_dir!r}')

        await asyncio.sleep(0)

        with self.project.cursor() as cursor:
            iter_docs = remove_common_base_dir(common_base_dir, extract_verify_documents(self.project.archive_path))
            for fragment in self.iter_fragments_from_documents(iter_docs):
                self.project.insert_fragment(cursor, fragment)
                await asyncio.sleep(0)

        self.inventory.mark_project_as_extracted(self.project.project_id)

    def iter_fragments_from_documents(self, iter_docs: Iterator[Document]):
        for doc in iter_docs:

            doc_type_cls = doc_types.detect_by_extension(doc.path)
            if doc_type_cls is None:
                # print(f'Skipping unsupported document {doc.path!r} in project {self.project.project_id!r}')
                continue

            yield from doc_type_cls().load(doc.path, doc.data)


async def extract_worker():
    print('Loader: Fragment extractor worker starter')
    inventory = Inventory()
    while 1:
        try:
            project_id: str = inventory.get_next_project_to_extract()
            if not project_id:
                await asyncio.sleep(1.0)
                continue

            try:
                project = Project(project_id)
                with timer(f'Extracted fragments of project {project_id!r}'):
                    loader = Extractor(inventory, project)
                    await loader.load()
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

        await asyncio.sleep(1)


class Embedder:

    def __init__(self, inventory: Inventory, project: Project) -> None:
        self.inventory = inventory
        self.project = project

    async def embed(self):
        more = True
        tasks = set()
        max_tasks = 1 + EMBEDDER_CLIENT.server_count
        assert max_tasks > 0
        while tasks or more:

            with self.project.cursor() as cursor:

                # Add new task as needed
                if more and len(tasks) < max_tasks:
                    fragments: List[Fragment] = self.project.get_fragments_to_embed(cursor, EMBEDDER_CLIENT.chunk_size)
                    if not fragments:
                        more = False
                        continue
                    task = asyncio.create_task(self.embed_batch(fragments))
                    tasks.add(task)
                    continue

                # Collect results
                done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED, timeout=30.0)
                for task in done:
                    uuids = task.result()
                    self.project.mark_fragments_embedded(cursor, uuids)

            await asyncio.sleep(0)

        self.inventory.mark_project_as_embedded(self.project.project_id)

    async def embed_batch(self, fragments: List[Fragment]):
        embeddings: List[List[float]] = await EMBEDDER_CLIENT.embed_fragments(fragments)
        uuids: List[str] = [fragment.uuid for fragment in fragments]
        await self.project.collection.store(uuids, embeddings)
        return uuids


async def embed_worker():
    print('Loader: Fragment embedder worker starter')
    inventory = Inventory()
    while 1:
        try:
            project_id: str = inventory.get_next_project_to_embed()
            if not project_id:
                await asyncio.sleep(1.0)
                continue

            try:
                project = Project(project_id)
                fragment_count = project.count_fragments()
                with timer(f'Embedded {fragment_count} fragments for project {project_id!r}', count=fragment_count):
                    embedder = Embedder(inventory, project)
                    await embedder.embed()
            except KeyboardInterrupt:
                raise
            except Exception:
                print(f'Failed to embed project {project_id!r}, will retry')
                print_exc()
                inventory.delete_project(project_id)
                await asyncio.sleep(5)
                continue

        except KeyboardInterrupt:
            raise
        except Exception:
            print('Unexpected failure')
            print_exc()
            await asyncio.sleep(10)
            continue


app = Quart(__name__)
workers = [extract_worker, embed_worker]


@app.get('/')
async def canary():
    return 'OK', 200


if __name__ == "__main__":
    port = int(os.environ.get('HTTP_PORT', '40002'))
    run_app(app, *[worker() for worker in workers], host='localhost', port=port)
