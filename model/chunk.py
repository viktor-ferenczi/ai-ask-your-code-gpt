from dataclasses import dataclass


@dataclass
class Chunk:
    lineno: int
    text: str
    name: str
