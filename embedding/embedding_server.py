"""Embedding server
"""
import json
import time
from typing import Dict, List

from quart import Quart, request, Response

from embedding import Embedding
from model.fragment import Fragment

EMBEDDING = Embedding()

app = Quart(__name__)

MAX_BATCH_SIZE = 1024
MAX_INSTRUCTION_SIZE = 512
MAX_TEXT_SIZE = 8192

PORT = 0xa11e  ## AI Instructor Embedding


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
    response = dict(embeddings=[[float(x) for x in row] for row in embeddings])
    return Response(response=json.dumps(response), status=200)


@app.post("/embed/query")
async def embed_query():
    body: Dict[str, any] = await request.get_json(force=True)
    embeddings = await EMBEDDING.embed_query(body['query'])
    response = dict(embedding=[float(x) for x in embeddings[0]])
    return Response(response=json.dumps(response), status=200)


def main():
    app.run(debug=True, host="localhost", port=PORT)


if __name__ == "__main__":
    main()
