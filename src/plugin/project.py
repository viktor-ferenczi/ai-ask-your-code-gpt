import io
import json
import os
import uuid
import zipfile
from traceback import print_exc
from typing import List, Tuple, Dict

import aiohttp
from grpc.aio import AioRpcError
from qdrant_client import QdrantClient

import doc_types
from common.constants import ARCHIVE_DOWNLOAD_FAKE_HEADERS, MAX_ARCHIVE_SIZE, MAX_FILE_SIZE, MAX_SOURCE_SIZE, MAX_QUERY_LENGTH, MAX_QUERY_LIMIT, PROJECT_FRAGMENTS_DIR
from database.collection import Collection
from embed.embedder_client import EmbedderClient
from model.fragment import Fragment
from model.hit import Hit
from utils.timer import timer


EMBEDDER_URLS = os.environ.get('EMBEDDER_URLS', 'http://127.0.0.1:40004').split()
EMBEDDER_CHUNK_SIZE = int(os.environ.get('EMBEDDER_CHUNK_SIZE', '1'))

EMBEDDER_CLIENT = EmbedderClient(EMBEDDER_URLS)


class ProjectException(Exception):
    pass


class Project:

    def __init__(self, project_id: str) -> None:
        self.project_id: str = project_id

        database = QdrantClient(location=QDRANT_LOCATION, port=QDRANT_HTTP_PORT, grpc_port=QDRANT_GRPC_PORT, prefer_grpc=True)
        self.collection = Collection(database, project_id)

    @property
    def fragments_path(self):
        return os.path.join(PROJECT_FRAGMENTS_DIR, f'{self.project_id}.json')

    @property
    def stored_marker_path(self):
        return os.path.join(PROJECT_FRAGMENTS_DIR, f'{self.project_id}.stored')

    async def download(self, url: str, app=None):
        fragments = await self.__download(url)
        if not fragments:
            raise ValueError('No fragments')

        self.save_fragments(fragments)

        if app is None:
            await background_embed_and_store_fragments(self, fragments)
        else:
            app.add_background_task(background_embed_and_store_fragments, self, fragments)

    @property
    def has_initialized(self):
        return os.path.isfile(self.fragments_path) and os.path.isfile(self.stored_marker_path)

    def save_fragments(self, fragments: List[Fragment]):
        os.makedirs(PROJECT_FRAGMENTS_DIR, exist_ok=True)
        with open(self.fragments_path, 'wt') as f:
            json.dump([fragment.__dict__ for fragment in fragments], f, indent=2)

    def load_fragments(self) -> List[Fragment]:
        with open(self.fragments_path, 'rt') as f:
            return [Fragment(**fields) for fields in json.load(f)]

    def delete_fragments(self):
        if os.path.isfile(self.fragments_path):
            os.remove(self.fragments_path)
        if os.path.isfile(self.stored_marker_path):
            os.remove(self.stored_marker_path)

    def mark_stored(self, stats: Dict[str, any]):
        with open(self.stored_marker_path, 'wt') as f:
            json.dump(stats, f, indent=2)

    async def delete(self):
        await self.collection.delete()
        self.delete_fragments()

    async def search(self, query: str, limit: int) -> List[Hit]:
        if not query.strip():
            # Empty query used by ChatGPT to check for the project's existence
            query = 'any documentation or code'

        if len(query) > MAX_QUERY_LENGTH:
            raise ValueError(f'The query must be at most {MAX_QUERY_LENGTH} characters')

        if limit > MAX_QUERY_LIMIT:
            raise ValueError(f'The limit must be at most {MAX_QUERY_LIMIT}')

        fragments = self.load_fragments()

        def match_path(part: str) -> List[Fragment]:
            if '.' not in part or len(part) < 2:
                return []
            return [fragment for fragment in fragments if fragment.path.lower().endswith(part.lower())]

        # def match_name(part: str) -> List[Fragment]:
        #     if len(part) < 3:
        #         return [fragment for fragment in fragments if fragment.name == part]
        #     return [fragment for fragment in fragments if fragment.name and fragment.name.endswith(part)]

        path_matches = set()
        # name_matches = set()
        vector_query = []

        for part in query.split():
            if not part:
                continue

            m = match_path(part)
            if m:
                path_matches.update(m)
                continue

            # m = match_name(part)
            # if m:
            #     name_matches.update(m)
            #     continue

            vector_query.append(part)

        path_matches = list(path_matches)
        # name_matches = list(name_matches)

        matching_fragments = path_matches  # | name_matches
        vector_query = ' '.join(vector_query) if vector_query else 'anything'

        # FIXME: Remove this once an instruction is passed down from here based on doc_type_cls!
        if path_matches:
            vector_query = f'{path_matches[0]} {vector_query}'

        uuid_filter = [fragment.uuid for fragment in matching_fragments]
        embedding = await EMBEDDER_CLIENT.embed_query(vector_query, timeout=20.0)

        hits = await self.collection.search(embedding, limit=limit, uuid_filter=uuid_filter)
        return hits

    async def __download(self, url: str) -> List[Fragment]:
        try:
            archive = await self.__get_archive(url)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(f'Failed to download source archive: {url}')
            print_exc()
            raise ProjectException(f'Failed to download source archive: {url}; Reason: {e}')
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
        async with aiohttp.ClientSession(headers=ARCHIVE_DOWNLOAD_FAKE_HEADERS) as session:
            async with session.get(url) as response:
                size = 0
                archive = []
                while 1:
                    chunk = await response.content.read(32768)
                    if not chunk:
                        break
                    archive.append(chunk)
                    size += len(chunk)
                    if size > MAX_ARCHIVE_SIZE:
                        raise IOError(f'Archive is too large, maximum is {MAX_ARCHIVE_SIZE >> 20}MiB')
                archive = b''.join(archive)
        return archive

    def __extract_files(self, archive, url):
        files: List[Tuple[str, str]] = []
        try:
            shortest = None
            total_size = 0
            with zipfile.ZipFile(io.BytesIO(archive), 'r') as zf:
                for filename in zf.namelist():
                    if filename.endswith('/'):
                        continue

                    doc_type_cls = doc_types.detect_by_extension(filename)
                    if doc_type_cls is None:
                        print(f'Skipping file of unknown type: {filename}')
                        continue

                    file_info: zipfile.ZipInfo = zf.getinfo(filename)
                    if file_info.file_size > MAX_FILE_SIZE:
                        print(f'Skipping large file: {filename}; maximum is {MAX_FILE_SIZE >> 20}MiB')
                        continue

                    total_size += file_info.file_size
                    if total_size > MAX_SOURCE_SIZE:
                        raise IOError(f'Extracted source is too large, maximum is {MAX_SOURCE_SIZE >> 20}MiB')

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

                    if shortest is None or len(filename) < len(shortest):
                        shortest = filename

                    files.append((filename, text))

            # Strip common folder at the top
            if shortest:
                if not shortest.endswith('/'):
                    shortest = shortest.rsplit('/')[0] + '/'
                if all(filename.startswith(shortest) for filename, text in files):
                    strip_len = len(shortest)
                    files = [(filename[strip_len:], text) for filename, text in files]

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


async def background_embed_and_store_fragments(project: Project, fragments: List[Fragment]) -> Dict[str, any]:
    collection = project.collection

    stats = {}
    with timer(f'Initialized project {project.project_id}', count=len(fragments), unit='fragment', stats=stats):
        try:
            await collection.create()
        except AioRpcError:
            pass

        for index in range(0, len(fragments), EMBEDDER_CHUNK_SIZE):
            chunk_of_fragments = fragments[index: index + EMBEDDER_CHUNK_SIZE]
            chunk_of_embeddings = await EMBEDDER_CLIENT.embed_fragments(chunk_of_fragments, timeout=30.0)
            await collection.store(chunk_of_fragments, chunk_of_embeddings)

    project.mark_stored(stats)
    return stats
