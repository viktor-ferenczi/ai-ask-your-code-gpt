import unittest

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from parsers import PythonParser
from embed.embedder_model import EmbedderModel
from example_fragments import get_random_test_fragments, get_test_fragments


class TestEmbedding(unittest.IsolatedAsyncioTestCase):

    async def test_code_search(self):
        embedder_model = EmbedderModel()

        fragments = get_test_fragments()
        fragment_embeddings: np.ndarray = await embedder_model.embed_fragments(fragments)

        python_query_instruction = PythonParser.query_instruction

        query_embeddings: np.ndarray = await embedder_model.embed_query(python_query_instruction, 'class GMLExporter')
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        fragment_index = np.argmax(similarities)
        self.assertEqual(fragment_index, 0)

        query_embeddings: np.ndarray = await embedder_model.embed_query(python_query_instruction, 'class GMLExporter')
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        fragment_index = np.argmax(similarities)
        self.assertEqual(fragment_index, 0)

        query_embeddings: np.ndarray = await embedder_model.embed_query(python_query_instruction, 'class SomeOtherClass')
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        fragment_index = np.argmax(similarities)
        self.assertEqual(fragment_index, 1)

        query_embeddings: np.ndarray = await embedder_model.embed_query(python_query_instruction, 'export method')
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        self.assertTrue(np.all(np.abs(similarities - np.average(similarities)) < 0.02))
        self.assertTrue(np.all(similarities > 0.87))

        query_embeddings: np.ndarray = await embedder_model.embed_query(python_query_instruction, 'completely_different method')
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        self.assertTrue(np.all(np.abs(similarities - np.average(similarities)) < 0.05))
        self.assertTrue(np.all(similarities < 0.81))

    async def test_performance(self):
        embedder_model = EmbedderModel()
        fragments = get_random_test_fragments(600)
        fragment_embeddings: np.ndarray = await embedder_model.embed_fragments(fragments)
        self.assertEqual(fragment_embeddings.shape, (len(fragments), 768))
