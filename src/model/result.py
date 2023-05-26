from dataclasses import dataclass


@dataclass
class Result:
    uuid: str
    score: float
