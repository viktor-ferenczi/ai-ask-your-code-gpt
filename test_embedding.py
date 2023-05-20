import unittest

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import embedding


class TestEmbedding(unittest.TestCase):

    def test_code_search(self):

        code_fragments = [
            ('a/b/test.py',
             '''\
class GMLExporter:

    def __init__(self, model):...
    def export(self, filepath):...
             '''),
            ('a/b/test.py',
             '''\
class SomeOtherClass:

    def __init__(self, model):...
    def export(self, filepath):...
             '''),
        ]

        fragment_embeddings: np.ndarray = embedding.embed_fragments(code_fragments)

        query_embeddings: np.ndarray = embedding.embed_query('*.py', 'class GMLExporter')
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        fragment_index = np.argmax(similarities)
        self.assertEqual(fragment_index, 0)

        query_embeddings: np.ndarray = embedding.embed_query('*.py', 'export method')
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        self.assertTrue(np.all(np.abs(similarities - np.average(similarities)) < 0.02))
        self.assertTrue(np.all(similarities > 0.70))

        query_embeddings: np.ndarray = embedding.embed_query('*.py', 'import method')
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        self.assertTrue(np.all(np.abs(similarities - np.average(similarities)) < 0.03))
        self.assertTrue(np.all(similarities < 0.66))
