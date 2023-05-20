import sys
from typing import List, Dict

import qdrant_client
import requests
from qdrant_client.http.models import Batch

import embedding
import fragmentation

DEVELOPMENT = sys.platform == 'win32'
ARCHIVE_SIZE_LIMIT = 10_000_000


def download(username: str, url: str) -> str:
    if DEVELOPMENT and url.startswith('http://localhost/'):
        source_dir = fragmentation.SOURCE_DIR
    else:
        response = requests.get(url)
        if response.headers['Content-Length'] > ARCHIVE_SIZE_LIMIT:
            return f'!Archive file must be at most {ARCHIVE_SIZE_LIMIT} bytes in size'
        archive = response.content
        # TODO: Extract in memory, stop at size limit
        # Parse source from memory
        raise NotImplementedError()

    project = fragmentation.Project(source_dir)
    project.load_from_disk()

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

    metas = [block.meta for block in blocks]

    vdb = qdrant_client.QdrantClient()
    vdb.upsert(
        collection_name=f'user:{username}/{project_id}',
        points=Batch(
            ids=block_ids,
            vectors=embeddings,
            payloads=metas,
        )
    )

    return project_id


def delete(username, project_id):
    vdb = qdrant_client.QdrantClient()
    vdb.delete_collection(f'user:{username}/{project_id}')


def search(username: str, url: str, path_glob: str, name_tail: str, text_expression: str, limit: int) -> List[Dict[str, object]]:
    return []
