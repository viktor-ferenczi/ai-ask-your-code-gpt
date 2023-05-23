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
