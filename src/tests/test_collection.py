import unittest
import uuid

import numpy as np
from grpc.aio import AioRpcError
from qdrant_client import QdrantClient

from embed.embedder_model import EmbedderModel
from example_fragments import get_test_fragments
from parsers import PythonParser
from project.collection import Collection
from tools import nums_from_results


class TestCollection(unittest.IsolatedAsyncioTestCase):

    async def test_collection(self):
        embedder_model = EmbedderModel()

        database = QdrantClient('localhost', port=6334, prefer_grpc=True, timeout=10.0)
        collection = Collection(database, f'TEST-{uuid.uuid4()}')

        await collection.delete()
        await collection.create()

        fragments = get_test_fragments()

        fragment_embeddings: np.ndarray = await embedder_model.embed_fragments(fragments)
        uuids = [fragment.uuid for fragment in fragments]
        embeddings = [row.tolist() for row in fragment_embeddings]
        await collection.store(uuids, embeddings)

        instruction = PythonParser.query_instruction

        query = 'class GMLExporter'
        query_embeddings = await embedder_model.embed_query(instruction, query)
        results = await collection.search(query_embeddings[0].tolist())
        nums = await nums_from_results(fragments, results)
        self.assertEqual(nums, [0, 1])

        query = 'class SomeOtherClass'
        query_embeddings = await embedder_model.embed_query(instruction, query)
        results = await collection.search(query_embeddings[0].tolist())
        nums = await nums_from_results(fragments, results)
        self.assertEqual(nums, [1, 0])

        query = 'class GMLExporter'
        query_embeddings = await embedder_model.embed_query(instruction, query)
        results = await collection.search(query_embeddings[0].tolist(), uuids=[fragments[0].uuid])
        nums = await nums_from_results(fragments, results)
        self.assertEqual(nums, [0])

        query = 'SomeOtherClass class'
        query_embeddings = await embedder_model.embed_query(instruction, query)
        results = await collection.search(query_embeddings[0].tolist(), uuids=[fragments[1].uuid])
        nums = await nums_from_results(fragments, results)
        self.assertEqual(nums, [1])
