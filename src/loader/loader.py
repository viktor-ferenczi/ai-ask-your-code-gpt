import asyncio
import os
from traceback import print_exc
from typing import Iterator

from quart import Quart

import doc_types
from common.doc import find_common_base_dir, remove_common_base_dir
from common.zip_support import extract_verify_documents
from common.server import run_app
from embed.embedder_client import EmbedderClient, STORE_EMBEDDERS
from model.document import Document
from project.inventory import Inventory
from project.project import Project


EMBEDDER_CLIENT = EmbedderClient(STORE_EMBEDDERS)


class Extractor:

    def __init__(self, project_id: str) -> None:
        self.project: Project = Project(project_id)

    async def load(self):
        self.project.create_database()

        common_base_dir = find_common_base_dir([doc.path for doc in extract_verify_documents(self.project.archive_path, max_file_count=None, verify_only=True)])
        await asyncio.sleep(0)
        with self.project.cursor() as cursor:
            iter_docs = remove_common_base_dir(common_base_dir, extract_verify_documents(self.project.archive_path, max_file_count=None))
            for fragment in self.iter_fragments_from_documents(iter_docs):
                self.project.insert_fragment(cursor, fragment)
                await asyncio.sleep(0)

    def iter_fragments_from_documents(self, iter_docs: Iterator[Document]):
        for doc in iter_docs:

            doc_type_cls = doc_types.detect_by_extension(doc.path)
            if doc_type_cls is None:
                print(f'Skipping unsupported document {doc.path!r} in project {self.project.project_id!r}')
                continue

            yield from doc_type_cls().load(doc)


async def extract_worker():
    inventory = Inventory()
    while True:
        try:
            project_id: str = inventory.get_next_project_to_extract()
            if not project_id:
                await asyncio.sleep(1.0)
                continue

            try:
                loader = Extractor(project_id)
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

    def __init__(self, project_id: str) -> None:
        self.project: Project = Project(project_id)

    async def embed(self):
        while 1:
            with self.project.cursor() as cursor:

                fragments = self.project.get_fragments_to_embed(cursor, EMBEDDER_CLIENT.chunk_size)
                if not fragments:
                    break

                embeddings = await EMBEDDER_CLIENT.embed_fragments(fragments)
                uuids = [fragment.uuid for fragment in fragments]
                await self.project.collection.store(uuids, embeddings)

            await asyncio.sleep(0)


async def embed_worker():
    inventory = Inventory()
    while True:
        try:
            project_id: str = inventory.get_next_project_to_embed()
            if not project_id:
                await asyncio.sleep(1.0)
                continue

            try:
                embedder = Embedder(project_id)
                await embedder.embed()
            except KeyboardInterrupt:
                raise
            except Exception:
                print(f'Failed to embed project {project_id!r}, it will be retry')
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


app = Quart(__name__)


@app.get('/')
async def canary():
    return 'OK', 200


if __name__ == "__main__":
    port = int(os.environ.get('HTTP_PORT', '40002'))
    run_app(app, extract_worker(), embed_worker(), host='localhost', port=port)
