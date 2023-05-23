"""Embedding server
"""
import json
import time
from typing import Dict, List, Type

from quart import Quart, request, Response

import doc_types
from embed.embedding import Embedding
from model.fragment import Fragment

EMBEDDING = Embedding()

app = Quart(__name__)

MAX_BATCH_SIZE = 1024
MAX_INSTRUCTION_SIZE = 512
MAX_TEXT_SIZE = 8192

PORT = 41246  ## 0xa11e: AI Instructor Embedding


@app.get('/')
async def ping():
    started = time.time()
    try:
        async with EMBEDDING.semaphore:
            pass
    finally:
        duration = time.time() - started
        print(f'Locking the semaphore took {duration:.3f}s')
    return Response(response='OK', status=200)


@app.post("/embed/fragments")
async def embed_fragments():
    body: Dict[str, any] = await request.get_json(force=True)
    fragments: List[Fragment] = [Fragment(**fields) for fields in body['fragments']]
    embeddings = await EMBEDDING.embed_fragments(fragments)
    response = dict(embeddings=embeddings.tolist())
    return Response(response=json.dumps(response), status=200)


@app.post("/embed/query")
async def embed_query():
    body: Dict[str, any] = await request.get_json(force=True)
    query = body.get('query', '')

    if not query.strip():
        return Response(response='Empty or missing query', status=400)

    # FIXME: Extend this to turn all paths, filenames and extensions in the
    #        query string into proper metadata search conditions.
    doc_type_cls: Type = None
    if query.startswith('.') and ' ' in query:
        ext, query = query.split(' ', 1)
        doc_type_cls = doc_types.detect_by_extension(ext.lower())

    embeddings = await EMBEDDING.embed_query(query, doc_type_cls)
    response = dict(embedding=embeddings[0].tolist())

    return Response(response=json.dumps(response), status=200)


def run():
    app.run(debug=True, host="localhost", port=PORT)


async def run_task():
    await app.run_task(debug=True, host="localhost", port=PORT)


if __name__ == "__main__":
    run()
