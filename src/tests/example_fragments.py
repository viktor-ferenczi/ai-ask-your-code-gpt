from model.fragment import Fragment

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
