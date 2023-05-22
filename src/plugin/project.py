import io
import os
import uuid
import zipfile
from traceback import print_exc
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

EMBEDDING_CLIENT = EmbeddingClient(os.environ.get('EMBEDDING_SERVER', 'http://127.0.0.1:41246').split())

QDRANT_LOCATION = os.environ.get('QDRANT_LOCATION', 'localhost')
QDRANT_HTTP_PORT = int(os.environ.get('QDRANT_HTTP_PORT', '6333'))
QDRANT_GRPC_PORT = int(os.environ.get('QDRANT_GRPC_PORT', '6334'))


class ProjectException(Exception):
    pass


class Project:

    def __init__(self, username: str, project_id: str) -> None:
        if not username.replace('-', '').replace('_', '').isalnum():
            username = '-no-user-'

        self.username: str = username
        self.project_id: str = project_id

        database = QdrantClient(location=QDRANT_LOCATION, port=QDRANT_HTTP_PORT, grpc_port=QDRANT_GRPC_PORT, prefer_grpc=True)
        self.collection = Collection(database, f'{username}-{project_id}')

    async def initialize(self, url: str):
        fragments = await self.__download(url)
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
        embedding = await EMBEDDING_CLIENT.embed_query(query, timeout=20.0)

        hits = await self.collection.search(embedding, limit)
        return hits

    async def __download(self, url: str) -> List[Fragment]:
        try:
            archive = await self.__get_archive(url)
        except KeyboardInterrupt:
            raise
        except Exception:
            print(f'Failed to download source archive: {url}')
            print_exc()
            raise ProjectException(f'Failed to download source archive: {url}')
        print(f'Downloaded archive: {url}')

        try:
            files = self.__extract_files(archive, url)
        except KeyboardInterrupt:
            raise
        except Exception:
            print(f'Failed extract source archive: {url}')
            print_exc()
            raise ProjectException(f'Failed extract source archive: {url}')
        print(f'Extracted {len(files)} files')

        try:
            fragments = self.__split_files(files)
        except KeyboardInterrupt:
            raise
        except Exception:
            print(f'Failed to process or store source text: {url}')
            print_exc()
            raise ProjectException(f'Failed to process or store source text: {url}')
        print(f'Split the files to {len(fragments)} fragments')

        return fragments

    async def __get_archive(self, url):
        async with aiohttp.ClientSession(headers=DOWNLOAD_HEADERS) as session:
            async with session.get(url) as response:
                content_length = int(response.headers['Content-Length'])
                if content_length < 1:
                    raise IOError('Empty archive')
                if content_length > MAX_ARCHIVE_SIZE:
                    raise IOError('Archive is too large (Content-Length)')
                archive = await response.content.readexactly(content_length)
        return archive

    def __extract_files(self, archive, url):
        files: List[Tuple[str, str]] = []
        try:
            total_size = 0
            with zipfile.ZipFile(io.BytesIO(archive), 'r') as zf:
                for filename in zf.namelist():
                    doc_type_cls = doc_types.detect_by_extension(filename)
                    if doc_type_cls is None:
                        print(f'Skipping file of unknown type: {filename}')
                        continue

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
                        print(f'Error decoding file as UTF-8: {filename}')
                        try:
                            text: str = data.decode('utf-8', errors='replace')
                        except UnicodeDecodeError:
                            print(f'Failed to decode file, skipping: {filename}')
                            continue

                    files.append((filename, text))

        except zipfile.BadZipfile as e:
            dump_filename = f'failed-archive-{uuid.uuid4()}.zip'
            print(f"[{e.__class__.__name__}] {e}; URL: {url}; Content: {dump_filename}")
            with open(dump_filename, 'wb') as f:
                f.write(archive)
            raise

        return files

    def __split_files(self, files: List[Tuple[str, str]]) -> List[Fragment]:
        fragments = []
        for path, text in files:
            doc_type_cls = doc_types.detect_by_extension(path)
            doc_type = doc_type_cls()
            fragments.extend(doc_type.split(path, text))
        return fragments
