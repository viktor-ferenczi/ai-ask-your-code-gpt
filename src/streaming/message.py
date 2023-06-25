from dataclasses import dataclass


@dataclass
class Message:
    topic: str
    value: bytes
