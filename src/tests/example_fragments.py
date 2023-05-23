import random
import uuid
from typing import List

from model.fragment import Fragment

FRAGMENTS = [
    Fragment('65dfd13f-d6fb-414e-be39-230bd8cb02f2',
             'a/b/test.py',
             1,
             '''\
class GMLExporter:

def __init__(self, model):...
def export(self, filepath):...
''',
             'GMLExporter'),
    Fragment('c125349d-c83b-4bd8-a5fa-1bc266918870',
             'a/b/other.py',
             10,
             '''\
class SomeOtherClass:

def __init__(self, model):...
def export(self, filepath):...
''',
             'SomeOtherClass'),
]


def get_test_fragments() -> List[Fragment]:
    fragments = [Fragment.clone(fragment) for fragment in FRAGMENTS]
    randomize_uuids_set_lineno(fragments)
    return fragments


def get_random_test_fragments(count: int) -> List[Fragment]:
    fragments = [Fragment.clone(random.choice(FRAGMENTS)) for _ in range(500)]
    randomize_uuids_set_lineno(fragments)
    return fragments


def randomize_uuids_set_lineno(fragments):
    for index, fragment in enumerate(FRAGMENTS):
        fragment.uuid = str(uuid.uuid4())
        fragment.lineno = 1 + index * 5
