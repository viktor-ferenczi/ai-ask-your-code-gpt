import unittest

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from model.fragment import Fragment
from embedding import Embedding

FRAGMENTS = [
    Fragment('a/b/test.py',
             1,
             '''\
class GMLExporter:

def __init__(self, model):...
def export(self, filepath):...
''',
             'GMLExporter'),
    Fragment('a/b/test.py',
             10,
             '''\
class SomeOtherClass:

def __init__(self, model):...
def export(self, filepath):...
''',
             'SomeOtherClass'),
]


class TestEmbedding(unittest.IsolatedAsyncioTestCase):

    async def test_code_search(self):
        embedding = Embedding()

        fragment_embeddings: np.ndarray = await embedding.embed_fragments(FRAGMENTS)

        query_embeddings: np.ndarray = await embedding.embed_query('class GMLExporter')
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        fragment_index = np.argmax(similarities)
        self.assertEqual(fragment_index, 0)

        query_embeddings: np.ndarray = await embedding.embed_query('.py class GMLExporter')
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        fragment_index = np.argmax(similarities)
        self.assertEqual(fragment_index, 0)

        query_embeddings: np.ndarray = await embedding.embed_query('.py class SomeOtherClass')
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        fragment_index = np.argmax(similarities)
        self.assertEqual(fragment_index, 1)

        query_embeddings: np.ndarray = await embedding.embed_query('.py export method')
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        self.assertTrue(np.all(np.abs(similarities - np.average(similarities)) < 0.02))
        self.assertTrue(np.all(similarities > 0.90))

        query_embeddings: np.ndarray = await embedding.embed_query('completely_different method')
        similarities: np.ndarray = cosine_similarity(query_embeddings, fragment_embeddings)
        print(similarities)
        self.assertTrue(np.all(np.abs(similarities - np.average(similarities)) < 0.05))
        self.assertTrue(np.all(similarities < 0.79))
