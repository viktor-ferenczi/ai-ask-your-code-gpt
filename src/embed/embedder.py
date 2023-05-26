import json
import os
from typing import Dict, List

from quart import Quart, request, Response

from common.server import run_app
from common.timer import timer
from embed.embedder_model import EmbedderModel
from model.fragment import Fragment

EMBEDDER_MODEL = EmbedderModel()

app = Quart(__name__)


@app.get('/')
async def canary():
    with timer('Locked the semaphore', minimum=3.0):
        async with EMBEDDER_MODEL.semaphore:
            pass
    return Response(response='OK', status=200)


@app.get('/check')
async def is_free():
    if EMBEDDER_MODEL.semaphore.locked():
        return Response(response='BUSY', status=429)
    return Response(response='FREE', status=200)


@app.post("/embed/fragments")
async def embed_fragments():
    body: Dict[str, any] = await request.get_json(force=True)
    fragments: List[Fragment] = [Fragment(**fields) for fields in body['fragments']]
    embeddings = await EMBEDDER_MODEL.embed_fragments(fragments)
    response = dict(embeddings=embeddings.tolist())
    return Response(response=json.dumps(response), status=200)


@app.post("/embed/query")
async def embed_query():
    body: Dict[str, any] = await request.get_json(force=True)
    instruction = body.get('instruction', '')
    query = body.get('query', '')

    if not instruction.strip():
        return Response(response='Empty or missing instruction', status=400)

    if not query.strip():
        return Response(response='Empty or missing query', status=400)

    embeddings = await EMBEDDER_MODEL.embed_query(instruction, query)
    response = dict(embedding=embeddings[0].tolist())

    return Response(response=json.dumps(response), status=200)


if __name__ == "__main__":
    port = int(os.environ.get('HTTP_PORT', '40002'))
    run_app(app, host='localhost', port=port)
