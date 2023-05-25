import asyncio
import os
from typing import Iterator, List, Dict

from quart import Response, Quart

import common.constants as C
import doc_types
from common.doc import find_common_base_dir, remove_common_base_dir
from common.extractor import extract_files
from common.storage import FragmentStorage, ArchiveStorage, FragmentIndexStorage, FragmentsByPathStorage
from embed.embedder_client import EmbedderClient
from model.document import Document

EMBEDDER_URLS = os.environ.get('EMBEDDER_URLS', 'http://127.0.0.1:40004').split()
EMBEDDER_CHUNK_SIZE = int(os.environ.get('EMBEDDER_CHUNK_SIZE', '1'))

EMBEDDER_CLIENT = EmbedderClient(EMBEDDER_URLS)

QDRANT_LOCATION = os.environ.get('QDRANT_LOCATION', 'localhost')
QDRANT_HTTP_PORT = int(os.environ.get('QDRANT_HTTP_PORT', '6333'))
QDRANT_GRPC_PORT = int(os.environ.get('QDRANT_GRPC_PORT', '6334'))


class Splitter:

    def __init__(self, project_id: str) -> None:
        self.project_id = project_id

        self.archive_storage: ArchiveStorage = ArchiveStorage(project_id)
        self.fragment_storage: FragmentStorage = FragmentStorage(project_id)
        self.fragment_index_storage: FragmentIndexStorage = FragmentIndexStorage(project_id)
        self.fragments_by_path_storage: FragmentsByPathStorage = FragmentsByPathStorage(project_id)

    def extract_and_produce_fragments(self):
        if not self.archive_storage.exists:
            raise IOError(f'Archive is missing for project {self.project_id}')

        if self.fragment_storage and self.fragment_index_storage and self.fragments_by_path_storage:
            return

        fragment_uuids = []
        fragments_by_path = {}
        archive = self.archive_storage.load()
        common_base_dir = find_common_base_dir([doc.path for doc in extract_files(archive, verify_only=True)])
        iter_docs = remove_common_base_dir(common_base_dir, extract_files(archive))
        self.fragment_storage.save(self.__produce_fragments(iter_docs, fragment_uuids, fragments_by_path))
        self.fragments_by_path_storage.save(fragments_by_path)

        fragment_index = dict(zip(fragment_uuids, self.fragment_storage.iter_line_offsets()))
        self.fragment_index_storage.save(fragment_index)

    def __produce_fragments(self, iter_docs: Iterator[Document], fragment_uuids: List[str], fragments_by_path: Dict[str, List[str]]):
        for doc in iter_docs:

            doc_type_cls = doc_types.detect_by_extension(doc.path)
            if doc_type_cls is None:
                print(f'Skipping unsupported document {doc.path!r} in project {self.project_id!r}')
                continue

            doc_uuids: List[str] = []
            for fragment in doc_type_cls().load(doc):
                fragment_uuids.append(fragment.uuid)
                doc_uuids.append(fragment.uuid)
                yield fragment

            fragments_by_path[doc.path] = doc_uuids

            asyncio.sleep(0)


class Embedder:

    def __init__(self, project_id: str) -> None:
        self.project_id: str = project_id

        self.fragment_storage: FragmentStorage = FragmentStorage(project_id)

    def embed_all_fragments(self):
        if self.state_storage.exists:
            state: bytes = self.state_storage.load()
        else:
            self.state_storage.touch()
            state: bytes = b''

        batch = []
        for fragment in self.fragment_storage.load():
            if len(batch) < EMBEDDER_CHUNK_SIZE:
                batch.append(fragment)
            else:
                self.embed_batch(batch)

        if batch:
            self.embed_batch(batch)

    def embed_batch(self, batch):
        fragments: List[Fragment] = [Fragment(**fields) for fields in body['fragments']]
        embeddings = await EMBEDDER_MODEL.embed_fragments(fragments)
        response = dict(embeddings=embeddings.tolist())


app = Quart(__name__)


@app.get('/')
async def canary():
    return Response(response='OK', status=200)


@app.post("/project/<string:project_id>")
async def trigger(project_id: str):
    project_id = project_id.lower()
    if not RX.GUID.match(project_id):
        return Response(response='Invalid project_id, it must be a GUID', status=400)


def run():
    app.run(debug=True, host="localhost", port=PORT)


async def run_task():
    await app.run_task(debug=True, host="localhost", port=PORT)


if __name__ == "__main__":
    run()
