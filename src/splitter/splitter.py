import asyncio
import os
from typing import Iterator, List, Dict

from quart import Response, Quart

import common.constants as C
import doc_types
from common.doc import find_common_base_dir, remove_common_base_dir
from common.extractor import extract_files
from embed.embedder_client import EmbedderClient
from model.document import Document

EMBEDDER_URLS = os.environ.get('EMBEDDER_URLS', 'http://127.0.0.1:40004').split()
EMBEDDER_CHUNK_SIZE = int(os.environ.get('EMBEDDER_CHUNK_SIZE', '1'))

EMBEDDER_CLIENT = EmbedderClient(EMBEDDER_URLS)

QDRANT_LOCATION = os.environ.get('QDRANT_LOCATION', 'localhost')
QDRANT_HTTP_PORT = int(os.environ.get('QDRANT_HTTP_PORT', '6333'))
QDRANT_GRPC_PORT = int(os.environ.get('QDRANT_GRPC_PORT', '6334'))





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
