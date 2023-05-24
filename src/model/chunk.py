import hashlib
from dataclasses import dataclass


@dataclass
class Chunk:
    lineno: int
    text: str
    name: str

    @classmethod
    def clone(cls, other: "Chunk") -> "Chunk":
        return Chunk(other.lineno, other.text, other.name)

    def __hash__(self) -> int:
        return self.lineno ^ hash(self.text) & hash(self.name)

    @property
    def text_hash(self) -> str:
        return hashlib.sha256(self.text).hexdigest()
