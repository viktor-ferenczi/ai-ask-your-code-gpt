import hashlib
from dataclasses import dataclass


@dataclass
class Fragment:
    path: str
    lineno: int
    text: str
    name: str

    @property
    def text_hash(self) -> str:
        return hashlib.sha256(self.text).hexdigest()
