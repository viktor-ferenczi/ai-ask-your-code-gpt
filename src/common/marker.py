import os
from pathlib import Path


class Marker:

    def __init__(self, path: str) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.path = path

    def mark(self):
        Path(self.path).touch()

    def clear(self):
        try:
            os.remove(self.path)
        except (IOError, OSError):
            pass

    @property
    def is_marked(self):
        return os.path.exists(self.path)
