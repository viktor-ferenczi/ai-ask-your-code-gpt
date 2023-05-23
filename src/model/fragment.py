import hashlib
from dataclasses import dataclass


@dataclass
class Fragment:
    uuid: str
    path: str
    lineno: int
    text: str
    name: str

    def __hash__(self) -> int:
        return hash(self.uuid) ^ hash(self.path) ^ self.lineno ^ hash(self.text) & hash(self.name)

    @property
    def text_hash(self) -> str:
        return hashlib.sha256(self.text).hexdigest()
