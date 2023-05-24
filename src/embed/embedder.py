import json
from typing import Dict, List, Type

from quart import Quart, request, Response

import doc_types
from embed.embedder_model import EmbedderModel
from model.fragment import Fragment
from common.timer import timer

EMBEDDER_MODEL = EmbedderModel()

app = Quart(__name__)

PORT = 41246  ## 0xa11e: AI Instructor Embedding


@app.get('/')
async def canary():
    with timer('Locked the semaphore'):
        async with EMBEDDER_MODEL.semaphore:
            pass
    return Response(response='OK', status=200)


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
    query = body.get('query', '')

    if not query.strip():
        return Response(response='Empty or missing query', status=400)

    # FIXME: Move this up the call chain to the Project level,
    # this level must receive a ready to use instruction text
    doc_type_cls: Type = None
    if query.startswith('.') and ' ' in query:
        ext, query = query.split(' ', 1)
        doc_type_cls = doc_types.detect_by_extension(ext.lower())

    embeddings = await EMBEDDER_MODEL.embed_query(query, doc_type_cls)
    response = dict(embedding=embeddings[0].tolist())

    return Response(response=json.dumps(response), status=200)


def run():
    app.run(debug=True, host="localhost", port=PORT)


async def run_task():
    await app.run_task(debug=True, host="localhost", port=PORT)


if __name__ == "__main__":
    run()
