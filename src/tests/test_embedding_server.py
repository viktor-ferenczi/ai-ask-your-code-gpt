import asyncio
import unittest

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from common.timer import timer
from doc_types import PythonDocType
from embed.embedder_client import EmbedderClient
from embed.embedder import app
from example_fragments import get_random_test_fragments, get_test_fragments

EMBEDDING_CLIENT = EmbedderClient([f'http://127.0.0.1:40100'])


class TestEmbeddingServer(unittest.IsolatedAsyncioTestCase):

    async def test_embedding_server(self):
        server_task = asyncio.create_task(app.run_task(debug=True, host='localhost', port=40100))
        test_task = asyncio.create_task(self.send_test_requests())

        await asyncio.wait([server_task, test_task], timeout=30.0, return_when=asyncio.FIRST_COMPLETED)

        test_task.result()
        server_task.cancel()

    async def send_test_requests(self):
        server = await EMBEDDING_CLIENT.find_free_server()
        self.assertIsNotNone(server)

        await self.verify_logic()
        await self.measure_performance()

    async def verify_logic(self):
        fragments = get_test_fragments()

        fragment_embeddings = await EMBEDDING_CLIENT.embed_fragments(fragments)
        query_embeddings = await EMBEDDING_CLIENT.embed_query(PythonDocType.query_instruction, 'class GMLExporter')

        fe = np.array(fragment_embeddings, np.float32)
        qe = np.array([query_embeddings], np.float32)

        similarities: np.ndarray = cosine_similarity(qe, fe)
        print(similarities)

        fragment_index = np.argmax(similarities)
        self.assertEqual(fragment_index, 0)

    async def measure_performance(self):
        fragments = get_random_test_fragments(600)
        with timer(f'Embedded {len(fragments)} fragments', count=len(fragments), unit='fragment'):
            fragment_embeddings = await EMBEDDING_CLIENT.embed_fragments(fragments)

        self.assertEqual(len(fragment_embeddings), len(fragments))
        self.assertEqual(len(fragment_embeddings[0]), 768)
