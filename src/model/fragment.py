from dataclasses import dataclass

from model.chunk import Chunk


@dataclass
class Fragment(Chunk):
    uuid: str
    path: str

    @classmethod
    def clone(cls, other: "Fragment") -> "Fragment":
        return Fragment(other.lineno, other.text, other.name, other.uuid, other.path)

    def __hash__(self) -> int:
        return Chunk.__hash__(self) ^ hash(self.uuid) ^ hash(self.path)
