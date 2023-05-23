from dataclasses import dataclass


@dataclass
class Chunk:
    lineno: int
    text: str
    name: str

    def __hash__(self) -> int:
        return self.lineno ^ hash(self.text) & hash(self.name)
