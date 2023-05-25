import unittest
import uuid
from typing import List

from grpc.aio import AioRpcError
from qdrant_client import QdrantClient

from database.collection import Collection
from embed.embedder_model import EmbedderModel
from example_fragments import get_test_fragments
from model.fragment import Fragment
from model.hit import Hit


class TestCollection(unittest.IsolatedAsyncioTestCase):

    async def test_collection(self):
        embedder_model = EmbedderModel()

        database = QdrantClient('localhost', port=6334, prefer_grpc=True, timeout=5.0)
        collection = Collection(database, f'TEST-{uuid.uuid4()}')

        try:
            await collection.delete()
        except AioRpcError:
            pass

        await collection.create()

        fragments = get_test_fragments()

        fragment_embeddings = await embedder_model.embed_fragments(fragments)
        await collection.store(fragments, fragment_embeddings.tolist())

        query = 'class GMLExporter'
        query_embeddings = await embedder_model.embed_query(query)
        hits = await collection.search(query_embeddings[0].tolist())

        self.verify_and_normalize_hits(hits)

        self.assertEqual(
            [
                Hit(score=0.0,
                    fragment=Fragment(uuid='',
                                      path='a/b/test.py',
                                      lineno=1,
                                      text='class GMLExporter:\n'
                                           '\n'
                                           'def __init__(self, model):...\n'
                                           'def export(self, filepath):...\n',
                                      name='GMLExporter')),
                Hit(score=0.0,
                    fragment=Fragment(uuid='',
                                      path='a/b/other.py',
                                      lineno=10,
                                      text='class SomeOtherClass:\n'
                                           '\n'
                                           'def __init__(self, model):...\n'
                                           'def export(self, filepath):...\n',
                                      name='SomeOtherClass')),
            ],
            hits
        )

        query = 'class SomeOtherClass'
        query_embeddings = await embedder_model.embed_query(query)
        hits = await collection.search(query_embeddings[0].tolist())

        self.verify_and_normalize_hits(hits)

        self.assertEqual(
            [
                Hit(score=0.0,
                    fragment=Fragment(uuid='',
                                      path='a/b/other.py',
                                      lineno=10,
                                      text='class SomeOtherClass:\n'
                                           '\n'
                                           'def __init__(self, model):...\n'
                                           'def export(self, filepath):...\n',
                                      name='SomeOtherClass')),
                Hit(score=0.0,
                    fragment=Fragment(uuid='',
                                      path='a/b/test.py',
                                      lineno=1,
                                      text='class GMLExporter:\n'
                                           '\n'
                                           'def __init__(self, model):...\n'
                                           'def export(self, filepath):...\n',
                                      name='GMLExporter')),
            ],
            hits
        )

        query = 'class GMLExporter'
        query_embeddings = await embedder_model.embed_query(query)
        hits = await collection.search(query_embeddings[0].tolist(), uuid_filter=[fragments[0].uuid])

        self.verify_and_normalize_hits(hits)

        self.assertEqual(
            [
                Hit(score=0.0,
                    fragment=Fragment(uuid='',
                                      path='a/b/test.py',
                                      lineno=1,
                                      text='class GMLExporter:\n'
                                           '\n'
                                           'def __init__(self, model):...\n'
                                           'def export(self, filepath):...\n',
                                      name='GMLExporter')),
            ],
            hits
        )

        query = 'SomeOtherClass class'
        query_embeddings = await embedder_model.embed_query(query)
        hits = await collection.search(query_embeddings[0].tolist(), uuid_filter=[fragments[1].uuid])

        self.verify_and_normalize_hits(hits)

        self.assertEqual(
            [
                Hit(score=0.0,
                    fragment=Fragment(uuid='',
                                      path='a/b/other.py',
                                      lineno=10,
                                      text='class SomeOtherClass:\n'
                                           '\n'
                                           'def __init__(self, model):...\n'
                                           'def export(self, filepath):...\n',
                                      name='SomeOtherClass'))
            ],
            hits
        )

    def verify_and_normalize_hits(self, hits: List[Hit]):
        if not hits:
            return

        scores = [hit.score for hit in hits]
        self.assertEqual(sorted(scores, reverse=True), scores)

        uuids = [hit.uuid for hit in hits]
        self.assertEqual(sorted(uuids), sorted(set(uuids)))

        for hit in hits:
            hit.score = 0.0
            hit.uuid = ''
