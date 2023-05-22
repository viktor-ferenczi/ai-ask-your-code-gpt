import asyncio
from typing import List

import numpy as np
import torch
from InstructorEmbedding import INSTRUCTOR

import doc_types
from doc_types import TextDocType
from model.fragment import Fragment


class Embedding:
    # XL: 7.0 ms/embed, 6.2GB GPU RAM usage
    # model_name = 'hkunlp/instructor-xl'

    # XL: 2.2 ms/embed, 3GB GPU RAM usage
    model_name = 'hkunlp/instructor-large'

    def __init__(self) -> None:
        if not torch.cuda.is_available():
            raise EnvironmentError('CUDA is not available')

        # TODO: Cite them properly!
        self.model = INSTRUCTOR(self.model_name)
        self.model.to('cuda')

        self.semaphore = asyncio.Semaphore()

    async def embed_fragments(self, fragments: List[Fragment]) -> np.numarray:
        assert fragments

        async with self.semaphore:
            # noinspection PyTypeChecker
            embeddings = self.model.encode([[doc_types.detect_by_extension(fragment.path).store_instruction + ':', fragment.text] for fragment in fragments])

        return embeddings

    async def embed_query(self, text: str) -> np.numarray:
        assert text

        if text.startswith('.'):
            extension = text.split(' ')[0].lower()[1:]
            instruction = doc_types.detect_by_extension(extension).query_instruction
        else:
            instruction = TextDocType.query_instruction

        async with self.semaphore:
            # noinspection PyTypeChecker
            embeddings = self.model.encode([[instruction + ':', text]])

        return embeddings
