import unittest

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from doc_types import PythonDocType
from embed.embedding import Embedding
from example_fragments import get_random_test_fragments, get_test_fragments


class TestEmbedding(unittest.IsolatedAsyncioTestCase):

    async def test_code_search(self):
        embedding = Embedding()

        fragments = get_test_fragments()
        fragment_embeddings: np.ndarray = await embedding.embed_fragments(fragments)

        query_embeddings: np.ndarray = await embedding.embed_query('class GMLExporter')
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        fragment_index = np.argmax(similarities)
        self.assertEqual(fragment_index, 0)

        query_embeddings: np.ndarray = await embedding.embed_query('class GMLExporter', PythonDocType)
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        fragment_index = np.argmax(similarities)
        self.assertEqual(fragment_index, 0)

        query_embeddings: np.ndarray = await embedding.embed_query('class SomeOtherClass', PythonDocType)
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        fragment_index = np.argmax(similarities)
        self.assertEqual(fragment_index, 1)

        query_embeddings: np.ndarray = await embedding.embed_query('export method', PythonDocType)
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        self.assertTrue(np.all(np.abs(similarities - np.average(similarities)) < 0.02))
        self.assertTrue(np.all(similarities > 0.87))

        query_embeddings: np.ndarray = await embedding.embed_query('completely_different method', PythonDocType)
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        self.assertTrue(np.all(np.abs(similarities - np.average(similarities)) < 0.05))
        self.assertTrue(np.all(similarities < 0.81))

    async def test_performance(self):
        embedding = Embedding()
        fragments = get_random_test_fragments(600)
        fragment_embeddings: np.ndarray = await embedding.embed_fragments(fragments)
        self.assertEqual(fragment_embeddings.shape, (len(fragments), 768))
