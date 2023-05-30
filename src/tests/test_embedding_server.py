import asyncio
import time
import unittest

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from common.timer import timer
from embed.embedder import app
from embed.embedder_client import EmbedderClient, FREE
from example_fragments import get_random_test_fragments, get_test_fragments
from parsers import PythonParser

EMBEDDING_CLIENT = EmbedderClient(['http://127.0.0.1:40100'])


class TestEmbeddingServer(unittest.IsolatedAsyncioTestCase):

    async def test_embedding_server(self):
        server_task = asyncio.create_task(app.run_task(debug=True, host='localhost', port=40100))
        test_task = asyncio.create_task(self.actual_test())

        await asyncio.wait([server_task, test_task], timeout=30.0, return_when=asyncio.FIRST_COMPLETED)

        test_task.result()
        server_task.cancel()

    async def actual_test(self):
        deadline = time.time() + 20.0
        while time.time() < deadline:
            if await EMBEDDING_CLIENT.check_embedder(EMBEDDING_CLIENT.servers[0], timeout=0.5) == FREE:
                break
        else:
            self.fail('The embedder did not come online')

        server = await EMBEDDING_CLIENT.find_free_server()
        self.assertIsNotNone(server)

        await self.verify_logic()
        await self.measure_performance()

    async def verify_logic(self):
        fragments = get_test_fragments()

        fragment_embeddings = await EMBEDDING_CLIENT.embed_fragments(fragments)
        query_embeddings = await EMBEDDING_CLIENT.embed_query(PythonParser.query_instruction, 'class GMLExporter')

        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)

        fragment_index = np.argmax(similarities)
        self.assertEqual(fragment_index, 0)

    async def measure_performance(self):
        fragments = get_random_test_fragments(600)
        with timer(f'Embedded {len(fragments)} fragments', count=len(fragments), unit='fragment'):
            embeddings: np.ndarray = await EMBEDDING_CLIENT.embed_fragments(fragments)

        self.assertEqual(embeddings.shape, (len(fragments), 768))
