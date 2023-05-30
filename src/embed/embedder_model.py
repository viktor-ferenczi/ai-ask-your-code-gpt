import asyncio
import os
from typing import List

import numpy as np
import torch
from InstructorEmbedding import INSTRUCTOR

import parsers
from common.timer import timer
from model.fragment import Fragment
from parsers import TextParser

EMBEDDING_BATCH_SIZE = int(os.environ.get('EMBEDDING_BATCH_SIZE', '32'))


def verify_torch():
    if not torch.cuda.is_available():
        raise EnvironmentError('CUDA is not available')
    print(f'Torch CUDA device: {torch.cuda.get_device_name(0)}')
    # noinspection PyUnresolvedReferences
    cudnn_version = torch.backends.cudnn.version()
    if not cudnn_version:
        raise EnvironmentError('cuDNN is not available')
    if cudnn_version < 8700:
        raise EnvironmentError(f'cuDNN version must be at least 8700, currently it is {cudnn_version}')


# noinspection SpellCheckingInspection
class EmbedderModel:
    # XL: 7.0 ms/embed, 6.2GB GPU RAM usage
    # model_name = 'hkunlp/instructor-xl'

    # XL: 2.2 ms/embed, 3GB GPU RAM usage
    model_name = 'hkunlp/instructor-large'

    def __init__(self) -> None:
        verify_torch()

        # TODO: Cite them properly!
        self.model = INSTRUCTOR(self.model_name)
        self.model.to('cuda:0')

        self.semaphore = asyncio.Semaphore()

    async def embed_fragments(self, fragments: List[Fragment]) -> np.ndarray:
        assert fragments

        doc_type_cls_list = [
            parsers.detect(fragment.path)
            for fragment in fragments
        ]

        instructions = [
            (doc_type_cls.store_instruction if doc_type_cls else TextParser.store_instruction)
            for doc_type_cls in doc_type_cls_list
        ]

        sentences = [
            [f'{instruction}:', fragment.text]
            for instruction, fragment in zip(instructions, fragments)
        ]

        async with self.semaphore:
            with timer(f'Embedded {len(fragments)} fragments', count=len(fragments), unit='fragment'):
                # noinspection PyTypeChecker
                embeddings = self.model.encode(sentences, batch_size=EMBEDDING_BATCH_SIZE)

        return embeddings

    async def embed_query(self, instruction: str, query: str) -> np.ndarray:
        assert instruction
        assert not instruction.endswith(':')
        assert query

        sentences = [[instruction + ':', query]]

        async with self.semaphore:
            with timer(f'Embedded a query'):
                # noinspection PyTypeChecker
                embeddings = self.model.encode(sentences, batch_size=1)

        return embeddings
