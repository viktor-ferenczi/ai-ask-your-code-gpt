from dataclasses import dataclass


@dataclass
class Document:
    path: str
    data: bytes
