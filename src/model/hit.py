from dataclasses import dataclass

from fragment import Fragment


@dataclass
class Hit(Fragment):
    score: float
