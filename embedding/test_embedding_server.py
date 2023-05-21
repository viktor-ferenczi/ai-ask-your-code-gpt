import asyncio
import json
import unittest

import aiohttp
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

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
        server_task.cancel()

    async def send_test_requests(self):
        async with aiohttp.ClientSession() as session:
            for i in range(50):
                try:
                    async with session.get(f'http://localhost:{self.port}/', headers={'Accept': 'text/plain'}) as response:
                        if response.status == 200:
                            break
                except KeyboardInterrupt:
                    raise
                except:
                    await asyncio.sleep(0.2)
            else:
                self.fail('Could not reach the embedding server')

            async with session.post(f'http://localhost:{self.port}/embed/fragments', data=json.dumps(dict(fragments=[fragment.__dict__ for fragment in FRAGMENTS]), indent=2), headers={'Accept': 'text/json'}) as response:
                content = await response.content.read()
                self.assertEqual(response.status, 200)
                data = json.loads(content.decode('utf-8'))
                fragment_embeddings = data['embeddings']
                self.assertEqual(len(fragment_embeddings), len(FRAGMENTS))
                for embedding in fragment_embeddings:
                    self.assertEqual(len(embedding), 768)

            async with session.post(f'http://localhost:{self.port}/embed/query', data=json.dumps(dict(query='class GMLExporter'), indent=2), headers={'Accept': 'text/json'}) as response:
                content = await response.content.read()
                self.assertEqual(response.status, 200)
                data = json.loads(content.decode('utf-8'))
                query_embeddings = data['embeddings']
                self.assertEqual(len(query_embeddings), 1)
                self.assertEqual(len(query_embeddings[0]), 768)

            fe = np.array(fragment_embeddings, np.float32)
            qe = np.array(query_embeddings, np.float32)
            similarities: np.ndarray = cosine_similarity(qe, fe)
            print(similarities)
            fragment_index = np.argmax(similarities)
            self.assertEqual(fragment_index, 0)
