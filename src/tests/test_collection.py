import unittest
import uuid

from grpc.aio import AioRpcError
from qdrant_client import QdrantClient

from database.collection import Collection
from embed.embedding import Embedding
from model.fragment import Fragment
from model.hit import Hit
from example_fragments import FRAGMENTS


class TestCollection(unittest.IsolatedAsyncioTestCase):

    async def test_collection(self):
        embedding = Embedding()

        database = QdrantClient('localhost', port=6334, prefer_grpc=True, timeout=5.0)
        collection = Collection(database, f'TEST-{uuid.uuid4()}')

        try:
            await collection.delete()
        except AioRpcError:
            pass

        await collection.create()

        fragment_embeddings = await embedding.embed_fragments(FRAGMENTS)
        await collection.store(FRAGMENTS, fragment_embeddings.tolist())

        query = 'class GMLExporter'
        query_embeddings = await embedding.embed_query(query)
        hits = await collection.search(query, query_embeddings[0].tolist())

        await collection.delete()

        self.assertEqual(
            [
                Hit(score=0.9402979612350464,
                    fragment=Fragment(path='a/b/test.py',
                                      lineno=1,
                                      text='class GMLExporter:\n'
                                           '\n'
                                           'def __init__(self, model):...\n'
                                           'def export(self, filepath):...\n',
                                      name='GMLExporter')),
                Hit(score=0.8443304896354675,
                    fragment=Fragment(path='a/b/test.py',
                                      lineno=10,
                                      text='class SomeOtherClass:\n'
                                           '\n'
                                           'def __init__(self, model):...\n'
                                           'def export(self, filepath):...\n',
                                      name='SomeOtherClass')),
            ],
            hits
        )
