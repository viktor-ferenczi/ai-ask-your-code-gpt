import io
import os
import uuid
import zipfile
from typing import List, Tuple

import aiohttp
from grpc.aio import AioRpcError
from qdrant_client import QdrantClient

import doc_types
from database.collection import Collection
from embed.embedding_client import EmbeddingClient
from model.fragment import Fragment
from model.hit import Hit

DOWNLOAD_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
}

MAX_ARCHIVE_SIZE = 1_000_000
MAX_FILE_SIZE = 10_000_000
MAX_SOURCE_SIZE = 10_000_000

EMBEDDING_CLIENT = EmbeddingClient()
EMBEDDING_CLIENT.servers = os.environ.get('EMBEDDING_SERVER', 'http://127.0.0.1:41246').split()

QDRANT_LOCATION = os.environ.get('QDRANT_LOCATION', 'localhost')
QDRANT_HTTP_PORT = int(os.environ.get('QDRANT_HTTP_PORT', '6333'))
QDRANT_GRPC_PORT = int(os.environ.get('QDRANT_GRPC_PORT', '6334'))


class Project:

    def __init__(self, username: str, project_id: str) -> None:
        if not username.replace('-', '').replace('_', '').isalnum():
            username = '-no-user-'

        self.username: str = username
        self.project_id: str = project_id

        database = QdrantClient(location=QDRANT_LOCATION, port=QDRANT_HTTP_PORT, grpc_port=QDRANT_GRPC_PORT, prefer_grpc=True)
        self.collection = Collection(database, f'{username}-{project_id}')

    async def initialize(self, url: str):
        fragments = await self.download(url)
        if not fragments:
            raise ValueError('No fragments')

        embeddings = await EMBEDDING_CLIENT.embed_fragments(fragments, timeout=30.0)

        try:
            await self.collection.create()
        except AioRpcError:
            pass

        await self.collection.store(fragments, embeddings)

    async def delete(self):
        await self.collection.delete()

    async def search(self, query: str, limit: int) -> List[Hit]:
        embedding = await EMBEDDING_CLIENT.embed_query(query, timeout=30.0)

        hits = await self.collection.search(embedding, limit)
        return hits

    async def download(self, url: str) -> List[Fragment]:
        archive = await self.get_archive(url)
        print(f'Downloaded archive: {url}')

        files = self.extract_files(archive, url)
        print(f'Extracted {len(files)} files')

        fragments = self.split_files(files)
        print(f'Split the files to {len(fragments)} fragments')
        return fragments

    async def get_archive(self, url):
        async with aiohttp.ClientSession(headers=DOWNLOAD_HEADERS) as session:
            async with session.get(url) as response:
                content_length = int(response.headers['Content-Length'])
                if content_length < 1:
                    raise IOError('Empty archive')
                if content_length > MAX_ARCHIVE_SIZE:
                    raise IOError('Archive is too large (Content-Length)')
                archive = await response.content.readexactly(content_length)
        return archive

    def extract_files(self, archive, url):
        files: List[Tuple[str, str]] = []
        try:
            total_size = 0
            with zipfile.ZipFile(io.BytesIO(archive), 'r') as zf:
                for filename in zf.namelist():
                    file_info: zipfile.ZipInfo = zf.getinfo(filename)
                    if file_info.file_size > MAX_FILE_SIZE:
                        raise IOError(f'File too large: {filename}')
                    total_size += file_info.file_size
                    if total_size > MAX_SOURCE_SIZE:
                        raise IOError(f'Extracted source is too large')
                    data: bytes = zf.read(filename)
                    try:
                        text: str = data.decode('utf-8')
                    except UnicodeDecodeError:
                        try:
                            text: str = data.decode('latin-1')
                        except UnicodeDecodeError:
                            print(f'Could not decode file, skipping: {filename}')
                            continue
                    files.append((filename, text))
        except zipfile.BadZipfile as e:
            dump_filename = f'failed-archive-{uuid.uuid4()}.zip'
            print(f"[{e.__class__.__name__}] {e}; URL: {url}; Content: {dump_filename}")
            with open(dump_filename, 'wb') as f:
                f.write(archive)
            raise
        return files

    def split_files(self, files: List[Tuple[str, str]]) -> List[Fragment]:
        fragments = []
        for path, text in files:
            doc_type_cls = doc_types.detect_by_extension(path)
            doc_type = doc_type_cls()
            fragments.extend(doc_type.split(path, text))
        return fragments
