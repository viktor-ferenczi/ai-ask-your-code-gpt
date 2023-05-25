import asyncio
import io
import json
import os.path
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Iterable, Iterator, ContextManager

import constants as C
from model.fragment import Fragment


class ProjectStorage:
    filename: str = ''

    def __init__(self, project_id: str) -> None:
        assert self.filename
        assert C.RX_GUID.match(project_id)

        self.project_id: str = project_id

        self.data_subdir: str = os.path.join(C.PROJECTS_DIR, self.project_id[:2], self.project_id[2:4], self.project_id)
        os.makedirs(self.data_subdir, exist_ok=True)

        self.path: str = os.path.join(self.data_subdir, self.filename)

        self.semaphore = asyncio.Semaphore(1)

    @property
    def exists(self) -> bool:
        return os.path.isfile(self.path)

    @property
    def age(self) -> float:
        return max(0.0, time.time() - os.stat(self.path).st_mtime)

    def touch(self):
        Path(self.path).touch()

    @contextmanager
    def open(self, mode='r', buffering=None, encoding=None) -> ContextManager[io.FileIO]:
        with self.semaphore:
            with open(self.path, mode, buffering, encoding) as f:
                yield f


class BinaryStorage(ProjectStorage):

    def save(self, data: bytes):
        with self.open('wb') as f:
            f.write(data)

    def load(self) -> bytes:
        with self.open('rb') as f:
            return f.read()


class JsonStorage(ProjectStorage):

    def __init__(self, project_id: str, count: int) -> None:
        super().__init__(project_id)
        self.new_path = self.path + '.new'

    def save(self, value: object):
        with self.semaphore:
            with open(self.new_path, 'wt', encoding='utf-8') as f:
                json.dump(value, f)
            os.rename(self.new_path, self.path)

    def load(self) -> object:
        with self.open('rt', encoding='utf-8') as f:
            return json.load(f)


class ArchiveStorage(BinaryStorage):
    filename = 'archive.zip'


class FragmentIndexStorage(JsonStorage):
    filename = 'fragment-index.json'


class FragmentsByFileMapStorage(JsonStorage):
    filename = 'fragments-by-file.json'


class EmbeddingStateStorage(JsonStorage):
    filename = 'embedding-state.json'


class FragmentStorage(ProjectStorage):
    filename = 'fragments.jsonl'

    def save(self, fragments: Iterable[Fragment]):
        with self.open('wt', encoding='utf-8') as f:
            for fragment in fragments:
                print(json.dumps(fragment.__dict__), file=f)

    def load(self) -> Iterator[Fragment]:
        with self.open('rt', encoding='utf-8') as f:
            yield from (Fragment(**json.loads(line)) for line in f.readlines())
