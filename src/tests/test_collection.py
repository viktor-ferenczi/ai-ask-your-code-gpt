import unittest
import uuid
from typing import List

import numpy as np
from grpc.aio import AioRpcError
from qdrant_client import QdrantClient

from doc_types import PythonDocType
from embed.embedder_model import EmbedderModel
from example_fragments import get_test_fragments
from model.hit import Hit
from project.collection import Collection
from tools import nums_from_results


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

        fragment_embeddings: np.ndarray = await embedder_model.embed_fragments(fragments)
        uuids = [fragment.uuid for fragment in fragments]
        embeddings = [row.tolist() for row in fragment_embeddings]
        await collection.store(uuids, embeddings)

        instruction = PythonDocType.query_instruction

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
