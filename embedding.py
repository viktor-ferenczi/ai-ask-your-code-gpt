from typing import List, Tuple

import numpy as np
import torch

# TODO: Cite them properly!
from InstructorEmbedding import INSTRUCTOR

if not torch.cuda.is_available():
    raise EnvironmentError('CUDA is not available')

USE_XL_MODEL = True

if USE_XL_MODEL:
    # XL: 7.0 ms/embedding, 6.2GB GPU RAM usage
    MODEL = INSTRUCTOR('hkunlp/instructor-xl')
else:
    # XL: 2.2 ms/embedding, 3GB GPU RAM usage
    MODEL = INSTRUCTOR('hkunlp/instructor-large')

MODEL.to('cuda')

INSTRUCTIONS = {
    '.py': 'Python code',
    '.sh': 'shell script',
    '.txt': 'documentation',
    '.md': 'documentation',
}


def get_file_type(relpath: str) -> str:
    relpath = relpath.lower()
    for extension, file_type in INSTRUCTIONS.items():
        if relpath.endswith(extension):
            return file_type
    return 'generic text'


def get_instruction(relpath: str) -> str:
    file_type = get_file_type(relpath)
    return f'Represent this {file_type} for retrieval:'


def embed_fragments(fragments: List[Tuple[str, str]]) -> np.numarray:
    # noinspection PyTypeChecker
    embeddings = MODEL.encode([[get_instruction(relpath), fragment] for relpath, fragment in fragments])
    return embeddings


def embed_query(glob: str, query: str) -> np.numarray:
    file_type = get_file_type(glob or '')
    instruction = f'Represent this {file_type} search expression:'
    # noinspection PyTypeChecker
    embeddings = MODEL.encode([[instruction, query]])
    return embeddings


