import asyncio
import unittest

# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity

from embed.embedding_client import EmbeddingClient
# from example_fragments import FRAGMENTS

EMBEDDING_CLIENT = EmbeddingClient([f'http://127.0.0.1:41246'])


async def run_embedding_server():
    from embed.embedding_server import run_task
    await run_task()


class TestEmbeddingServer(unittest.IsolatedAsyncioTestCase):

    async def test_embedding_server(self):
        server_task = asyncio.create_task(run_embedding_server())
        test_task = asyncio.create_task(self.send_test_requests())

        done, pending = await asyncio.wait([server_task, test_task], timeout=20.0, return_when=asyncio.FIRST_COMPLETED)

        self.assertTrue(test_task in done)
        self.assertTrue(server_task in pending)

        test_task.result()
        server_task.cancel()

    async def send_test_requests(self):
        server = await EMBEDDING_CLIENT.find_free_server()
        self.assertIsNotNone(server)

        # fragment_embeddings = await EMBEDDING_CLIENT.embed_fragments(FRAGMENTS)
        # query_embeddings = await EMBEDDING_CLIENT.embed_query('class GMLExporter')
        #
        # fe = np.array(fragment_embeddings, np.float32)
        # qe = np.array([query_embeddings], np.float32)
        #
        # similarities: np.ndarray = cosine_similarity(qe, fe)
        # print(similarities)
        #
        # fragment_index = np.argmax(similarities)
        # self.assertEqual(fragment_index, 0)
