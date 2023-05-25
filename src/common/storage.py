import asyncio
import json
import os.path
import time
from pathlib import Path
from typing import Iterable, Iterator

import constants as C
from model.fragment import Fragment


class ProjectStorage:

    def __init__(self, project_id: str) -> None:
        assert C.RX_GUID.match(project_id)
        self.project_id: str = project_id
        self.data_subdir: str = os.path.join(C.PROJECTS_DIR, self.project_id[:2], self.project_id[2:4], self.project_id)
        self.semaphore = asyncio.Semaphore(1)


class FileProjectStorage(ProjectStorage):
    filename: str = ''

    def __init__(self, project_id: str) -> None:
        super().__init__(project_id)
        assert self.filename
        self.path: str = os.path.join(self.data_subdir, self.filename)

    @property
    def exist(self) -> bool:
        return os.path.isfile(self.path)

    @property
    def age(self) -> float:
        return max(0.0, time.time() - os.stat(self.path).st_mtime)

    def touch(self):
        Path(self.path).touch()


class FragmentStorage(FileProjectStorage):
    filename = 'fragments.jsonl'

    def save(self, fragments: Iterable[Fragment]):
        with self.semaphore:
            with open(self.path, 'wt', encoding='utf-8') as f:
                for fragment in fragments:
                    print(json.dumps(fragment.__dict__), file=f)

    def load(self) -> Iterator[Fragment]:
        with self.semaphore:
            with open(self.path, 'rt', encoding='utf-8') as f:
                yield from (Fragment(**json.loads(line)) for line in f.readlines())


class ProgressStorage(FileProjectStorage):

    @property
    def exist(self) -> bool:
        return os.path.isfile(self.path)

    def __init__(self, project_id: str, count: int) -> None:
        super().__init__(project_id)
        self.count: int = count

    @property
    def initial_state(self) -> bytes:
        return b'.' * self.count

    def save(self, state: bytes):
        assert len(state) == self.count
        with self.semaphore:
            with open(self.path, 'wb') as f:
                f.write(state)

    def load(self) -> bytes:
        with self.semaphore:
            with open(self.path, 'rb') as f:
                state: bytes = f.read()
        assert len(state) == self.count
        return state


class EmbeddingProgressStorage(ProgressStorage):
    filename = 'embedding-progress.txt'
