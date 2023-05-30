from dataclasses import dataclass


@dataclass
class Fragment:
    uuid: str
    path: str
    lineno: int
    depth: int
    type: str
    name: str
    text: str
