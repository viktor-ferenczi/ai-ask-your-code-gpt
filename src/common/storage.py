import asyncio
import json
import os.path
from typing import Iterable, Iterator

import constants as C
from model.fragment import Fragment


class ProjectStorage:

    def __init__(self, project_id: str) -> None:
        assert C.RX_GUID.match(project_id)
        self.project_id: str = project_id
        self.data_subdir: str = os.path.join(C.PROJECTS_DIR, self.project_id[:2], self.project_id[2:4], self.project_id)
        self.semaphore = asyncio.Semaphore(1)


class FragmentStorage(ProjectStorage):

    def __init__(self, project_id: str) -> None:
        super().__init__(project_id)
        self.path: str = os.path.join(self.data_subdir, 'fragments.jsonl')

    def save(self, fragments: Iterable[Fragment]):
        with self.semaphore:
            with open(self.path, 'wt', encoding='utf-8') as f:
                for fragment in fragments:
                    print(json.dumps(fragment.__dict__), file=f)

    def load(self) -> Iterator[Fragment]:
        with self.semaphore:
            with open(self.path, 'rt', encoding='utf-8') as f:
                yield from (Fragment(**json.loads(line)) for line in f.readlines())


class EmbeddingStateStorage(ProjectStorage):

    def __init__(self, project_id: str, fragment_count: int) -> None:
        super().__init__(project_id)
        self.path: str = os.path.join(self.data_subdir, 'embedding-state.txt')
        self.fragment_count: int = fragment_count

    @property
    def zero(self) -> bytes:
        return b'.' * self.fragment_count

    def save(self, state: bytes):
        assert len(state) == self.fragment_count
        with self.semaphore:
            with open(self.path, 'wb') as f:
                f.write(state)

    def load(self) -> bytes:
        with self.semaphore:
            with open(self.path, 'rb') as f:
                state: bytes = f.read()
        assert len(state) == self.fragment_count
        return state
