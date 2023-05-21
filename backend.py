import io
import uuid
import zipfile
from typing import List, Dict, Tuple

import aiohttp
import qdrant_client
from qdrant_client.conversions.common_types import Distance
from qdrant_client.http.models import Filter, FieldCondition, Match, VectorParams, Distance, Batch

import embedding
import fragmentation

MAX_ARCHIVE_SIZE = 1_000_000
MAX_FILE_SIZE = 10_000_000
MAX_SOURCE_SIZE = 10_000_000

QDRANT = ':memory:'
VDB = qdrant_client.QdrantClient(QDRANT)

DOWNLOAD_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
}


async def download(username: str, url: str) -> str:
    async with aiohttp.ClientSession(headers=DOWNLOAD_HEADERS) as session:
        async with session.get(url) as response:
            content_length = int(response.headers['Content-Length'])
            if content_length < 1:
                raise IOError('Empty archive')
            if content_length > MAX_ARCHIVE_SIZE:
                raise IOError('Archive is too large (Content-Length)')
            archive = await response.content.readexactly(content_length)

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

    project = fragmentation.Project()
    project.load_from_memory(files)

    blocks = [
        block
        for source in project.sources
        for block in source.blocks
    ]

    project_id = project.project_id

    block_ids = [block.block_id for block in blocks]

    embeddings = embedding.embed_fragments([
        (block.path, block.fragment)
        for block in blocks
    ])

    metas = [dict(text=block.fragment, meta=block.meta) for block in blocks]

    collection_name = f'user:{username}/{project_id}'

    VDB.create_collection(collection_name=collection_name, vectors_config=VectorParams(size=embeddings.shape[1], distance=Distance.DOT), timeout=10)
    VDB.upsert(
        collection_name=collection_name,
        points=Batch(
            ids=block_ids,
            vectors=[[float(v) for v in row] for row in embeddings],
            payloads=metas,
        ),
        timeout=10.0
    )

    coll = VDB.get_collection(collection_name)
    print(f'Added {coll.vectors_count} vectors to vector database collection {collection_name!r}')

    return project_id


async def delete(username, project_id):
    VDB.delete_collection(f'user:{username}/{project_id}')


async def search(username: str, project_id: str, text: str, limit: int = 1) -> List[Dict[str, any]]:
    query_vector = embedding.embed_fragments([(path, text)])[0]

    filter_conditions: List[FieldCondition] = []

    if path:
        condition = FieldCondition(
            key='path',
            range=Match(
                value=path
            )
        )
        filter_conditions.append(condition)

    query_filter = Filter(must=filter_conditions) if filter_conditions else None

    # FIXME: Async search!
    results = VDB.search(
        collection_name=f'user:{username}/{project_id}',
        query_vector=query_vector,
        query_filter=query_filter,
        limit=limit,
        with_payload=True
    )

    print(f'Backend search results: {results!r}')
    return [
        dict(
            score=hit.score,
            **hit.payload
        )
        for hit in results
    ]
