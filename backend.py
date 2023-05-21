import io
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

QDRANT = ':memory:'
VDB = qdrant_client.QdrantClient(QDRANT)


async def download(username: str, url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if int(resp.headers.get('Content-Length', '0')) > MAX_ARCHIVE_SIZE:
                raise IOError('Archive is too large (Content-Length)')
            archive = await resp.content.read(MAX_ARCHIVE_SIZE + 1)

    if len(archive) > MAX_ARCHIVE_SIZE:
        raise IOError('Archive is too large (actual download size)')

    files: List[Tuple[str, str]] = []
    with zipfile.ZipFile(io.BytesIO(archive), 'r') as zf:
        for filename in zf.namelist():
            file_info: zipfile.ZipInfo = zf.getinfo(filename)
            if file_info.file_size > MAX_FILE_SIZE:
                raise IOError(f'File too large: {filename}')
            text: str = zf.read(filename).decode('utf-8')
            files.append((filename, text))

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


async def search(username: str, project_id: str, text: str, path: str = '', limit: int = 1) -> List[Dict[str, object]]:
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
