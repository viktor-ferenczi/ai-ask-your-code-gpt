import asyncio
import unittest

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from embedding_client import EmbeddingClient
from test_embedding import FRAGMENTS


class TestEmbeddingServer(unittest.IsolatedAsyncioTestCase):
    port = 60381

    async def run_server(self):
        from embedding_server import app
        await app.run_task(debug=True, host='localhost', port=self.port)

    async def test_embedding_server(self):
        server_task = asyncio.create_task(self.run_server())
        test_task = asyncio.create_task(self.send_test_requests())
        done, pending = await asyncio.wait([server_task, test_task], timeout=10.0, return_when=asyncio.FIRST_COMPLETED)
        self.assertTrue(test_task in done)
        self.assertTrue(server_task in pending)
        test_task.result()
        server_task.cancel()

    async def send_test_requests(self):
        async with EmbeddingClient() as client:
            client.servers = [f'http://localhost:{self.port}']
            fragment_embeddings = await client.embed_fragments(FRAGMENTS)
            query_embeddings = await client.embed_query('class GMLExporter')
            fe = np.array(fragment_embeddings, np.float32)
            qe = np.array([query_embeddings], np.float32)
            similarities: np.ndarray = cosine_similarity(qe, fe)
            print(similarities)
            fragment_index = np.argmax(similarities)
            self.assertEqual(fragment_index, 0)
