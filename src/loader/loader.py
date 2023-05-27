import asyncio
import os
import uuid
from traceback import print_exc
from typing import Iterator, List

import numpy as np
from quart import Quart

import doc_types
from common.constants import C
from common.doc import find_common_base_dir, remove_common_base_dir
from common.server import run_app
from common.timer import timer
from common.zip_support import extract_verify_documents, iter_files_from_zip
from doc_types.splitters.tokenization import tiktoken_len
from embed.embedder_client import EmbedderClient, STORE_EMBEDDERS, EmbedderError
from model.document import Document
from model.fragment import Fragment
from project.inventory import Inventory
from project.project import Project

EMBEDDER_CLIENT = EmbedderClient(STORE_EMBEDDERS)


class Toc:
    enable_n2p = True
    enable_p2n = False

    def __init__(self) -> None:
        self.n2p = {}
        self.p2n = {}
        self.paths = set()

    def add(self, fragment: Fragment):
        path = fragment.path
        self.paths.add(path)

        name = fragment.name
        if not name:
            return

        lineno = fragment.lineno

        if self.enable_n2p:
            paths = self.n2p.get(name)
            if paths is None:
                self.n2p[name] = paths = []
            paths.append((path, lineno))

        if self.enable_p2n:
            names = self.p2n.get(path)
            if names is None:
                self.p2n[path] = names = []
            names.append((name, lineno))

    def __iter__(self) -> Iterator[Fragment]:
        if not self.paths:
            return

        toc_path = self.get_free_toc_path()

        lineno = 1

        if self.n2p:
            yield Fragment(uuid=str(uuid.uuid4()), path=toc_path, lineno=lineno, text='Definitions in the project by fully qualified name:\n', name='')
            lineno += 1
            for name, paths in sorted(self.n2p.items()):
                lines = [f'  {name}:\n']
                lines.extend(f'    - {path} line {lineno}\n' for path, lineno in sorted(paths))

                text = ''.join(lines)
                while tiktoken_len(text) > C.SPLITTER_CHUNK_SIZE:
                    lines.pop()
                    text = ''.join(lines)

                yield Fragment(uuid=str(uuid.uuid4()), path=toc_path, lineno=lineno, text=text, name='')
                lineno += len(lines) + 1

        if self.p2n:
            yield Fragment(uuid=str(uuid.uuid4()), path=toc_path, lineno=lineno, text='Definitions of the project by file path:\n', name='')
            lineno += 1
            for path, names in sorted(self.p2n.items()):
                lines = [f'  {path}:\n']
                lines.extend(f'    - {name} -> Line {lineno}\n' for name, lineno in sorted(names))

                text = ''.join(lines)
                while tiktoken_len(text) > C.SPLITTER_CHUNK_SIZE:
                    lines.pop()
                    text = ''.join(lines)

                yield Fragment(uuid=str(uuid.uuid4()), path=toc_path, lineno=lineno, text=text, name='')

                lineno += len(lines) + 1

    def get_free_toc_path(self):
        filename = 'TOC.md'
        while filename in self.paths:
            filename = f'_{filename}'
        return filename


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

            toc = Toc() if C.INCLUDE_TOC else None

            for fragment in self.iter_fragments_from_documents(iter_docs):
                self.project.insert_fragment(cursor, fragment)
                if toc is not None:
                    toc.add(fragment)
                await asyncio.sleep(0)

            if toc is not None:
                if C.DEVELOPMENT:
                    print('>>> TOC:')
                for fragment in toc:
                    self.project.insert_fragment(cursor, fragment)
                    if C.DEVELOPMENT:
                        print(fragment.text, end='')
                    await asyncio.sleep(0)
                if C.DEVELOPMENT:
                    print('>>> /TOC')

        with self.project.cursor() as cursor:
            self.project.index_by_path(cursor)
            self.project.index_by_name(cursor)

        self.inventory.mark_project_extracted(self.project.project_id)

    def iter_fragments_from_documents(self, iter_docs: Iterator[Document]):
        for doc in iter_docs:

            doc_type_cls = doc_types.detect_by_extension(doc.path)
            if doc_type_cls is None:
                # print(f'Skipping unsupported document {doc.path!r} in project {self.project.project_id!r}')
                continue

            yield from doc_type_cls().load(doc.path, doc.data)


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


class Embedder:

    def __init__(self, inventory: Inventory, project: Project) -> None:
        self.inventory = inventory
        self.project = project

    async def embed(self):
        embedder_chunk_size = EMBEDDER_CLIENT.chunk_size

        max_tasks = 1 + EMBEDDER_CLIENT.server_count
        assert max_tasks > 0

        while 1:

            with self.project.cursor() as cursor:
                fragments: List[Fragment] = self.project.get_fragments_to_embed(cursor, 4096)

            if not fragments:
                break

            batches = [fragments[i:i + embedder_chunk_size] for i in range(0, len(fragments), embedder_chunk_size)]
            del fragments

            batches.reverse()

            tasks = set()
            while batches or tasks:

                # Add new task as needed
                if batches and len(tasks) < max_tasks:
                    fragments: List[Fragment] = batches.pop()
                    task = asyncio.create_task(self.embed_batch(fragments))
                    tasks.add(task)
                    continue

                # Wait for a task to complete
                done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED, timeout=30.0)

                # Collect results
                for task in done:

                    try:
                        uuids = task.result()
                    except EmbedderError as e:
                        print(f'Failed to embed batch, it will be retried: {e}')
                        continue

                    with self.project.cursor() as cursor:
                        self.project.mark_fragments_embedded(cursor, uuids)

                await asyncio.sleep(0)

        self.inventory.mark_project_embedded(self.project.project_id)

    async def embed_batch(self, fragments: List[Fragment]):
        embeddings_array: np.ndarray = await EMBEDDER_CLIENT.embed_fragments(fragments)
        embeddings = [row.tolist() for row in embeddings_array]
        uuids: List[str] = [fragment.uuid for fragment in fragments]
        await self.project.collection.store(uuids, embeddings)
        return uuids


async def embed_worker():
    print('Loader: Fragment embedder worker started')
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

        await asyncio.sleep(0)


app = Quart(__name__)
workers = [extract_worker, embed_worker]


@app.get('/')
async def canary():
    return 'OK', 200


if __name__ == "__main__":
    port = int(os.environ.get('HTTP_PORT', '40002'))
    asyncio.run(run_app(app, *[worker() for worker in workers], host='localhost', port=port, debug=C.DEVELOPMENT))
