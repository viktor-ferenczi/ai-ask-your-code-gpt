import asyncio
import json
import os
from traceback import print_exc
from typing import Dict, List, Type, Iterator

import quart
from quart import Quart, request, Response

import common.constants as C
import doc_types
from common import extractor
from common.http import download_file
from common.storage import FragmentStorage, EmbeddingProgressStorage
from common.timer import timer
from embed.embedder_client import EmbedderClient
from model.document import Document
from model.fragment import Fragment

app = Quart(__name__)

PORT = int(os.environ.get('HTTP_PORT', '40001'))

EMBEDDER_URLS = os.environ.get('EMBEDDER_URLS', 'http://127.0.0.1:40004').split()
EMBEDDER_CHUNK_SIZE = int(os.environ.get('EMBEDDER_CHUNK_SIZE', '1'))

EMBEDDER_CLIENT = EmbedderClient(EMBEDDER_URLS)

QDRANT_LOCATION = os.environ.get('QDRANT_LOCATION', 'localhost')
QDRANT_HTTP_PORT = int(os.environ.get('QDRANT_HTTP_PORT', '6333'))
QDRANT_GRPC_PORT = int(os.environ.get('QDRANT_GRPC_PORT', '6334'))


class LoaderException(Exception):
    pass


class Loader:

    def __init__(self, project_id: str, url: str) -> None:
        self.project_id: str = project_id
        self.url: str = url
        self.fragment_storage: FragmentStorage = FragmentStorage(project_id)

    def download_verify_split(self):
        with timer(f'Downloaded archive for project {self.project_id!r}'):
            archive = self.__download()

        asyncio.sleep(0)

        files = self.__extract(archive)
        del archive

        asyncio.sleep(0)

        with timer(f'Extracted archive for project {self.project_id!r}'):
            self.fragment_storage.save(self.__split(files))

    def __download(self) -> bytes:
        try:
            archive: bytes = await download_file(self.url, max_size=C.MAX_ARCHIVE_SIZE)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(f'Failed to download archive {self.url!r} for project {self.project_id!r}')
            print_exc()
            raise LoaderException(f'Failed to download archive {self.url!r}: {e}')
        print(f'Downloaded archive of {len(archive)}B size for project {self.project_id!r} from {self.url!r}')
        return archive

    def __extract(self, archive: bytes) -> List[Document]:
        try:
            documents = extractor.extract_files(archive)
        except KeyboardInterrupt:
            raise
        except Exception:
            print(f'Failed extract source archive {self.url!r} for project {self.project_id!r}')
            print_exc()
            raise LoaderException(f'Failed extract source archive: {self.url!r}')
        print(f'Extracted {len(documents)} files')
        return documents

    def __split(self, documents: List[Document]) -> Iterator[Fragment]:
        path = ''
        fragment_count = 0
        try:
            for path, data in documents:

                doc_type_cls = doc_types.detect_by_extension(path)
                if doc_type_cls is None:
                    print(f'Skipping unsupported document {path!r} in project {self.project_id!r}')
                    continue

                for fragment in doc_type_cls().load(path, data):
                    fragment_count += 1
                    yield fragment

                asyncio.sleep(0)

        except KeyboardInterrupt:
            raise
        except Exception:
            print(f'Failed to load file {path!r} in project {self.project_id!r}')
            print_exc()
            raise LoaderException(f'Failed to load file: {path!r}')
        print(f'Loaded {len(documents)} files into {fragment_count} fragments')


class Embedder:

    def __init__(self, project_id: str) -> None:
        self.project_id: str = project_id
        self.fragment_storage: FragmentStorage = FragmentStorage(project_id)
        self.state_storage: EmbeddingProgressStorage = EmbeddingProgressStorage(project_id)

    def embed_all_fragments(self):
        if self.state_storage.exist:
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



@app.get('/')
async def canary():
    return Response(response='OK', status=200)


@app.post("/download/<string:project_id>")
async def download(project_id: str):
    project_id = project_id.lower()
    if not C.RX_GUID.match(project_id):
        return quart.Response(response='Invalid project_id, it must be a GUID', status=400)

    body: Dict[str, any] = await request.get_json(force=True)
    url = body.get('url')
    if not url:
        return quart.Response(response='Missing url', status=400)

    with timer(f'Loaded project {project_id!r}'):

        downloader = Loader(project_id, url)
        downloader.download_verify_split()

        embedder = Embedder(project_id)
        embedder.embed_all_fragments()

    return Response(response='OK', status=200)


@app.post("/embed/query")
async def embed_query():
    body: Dict[str, any] = await request.get_json(force=True)
    query = body.get('query', '')

    if not query.strip():
        return Response(response='Empty or missing query', status=400)

    # FIXME: Move this up the call chain to the Project level,
    # this level must receive a ready to use instruction text
    doc_type_cls: Type = None
    if query.startswith('.') and ' ' in query:
        ext, query = query.split(' ', 1)
        doc_type_cls = doc_types.detect_by_extension(ext.lower())

    embeddings = await EMBEDDER_MODEL.embed_query(query, doc_type_cls)
    response = dict(embedding=embeddings[0].tolist())

    return Response(response=json.dumps(response), status=200)


def run():
    app.run(debug=True, host="localhost", port=PORT)


async def run_task():
    await app.run_task(debug=True, host="localhost", port=PORT)


if __name__ == "__main__":
    run()
