from dataclasses import dataclass

from model.fragment import Fragment


@dataclass
class Hit(Fragment):
    score: float
