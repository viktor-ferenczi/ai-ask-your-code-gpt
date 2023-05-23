from dataclasses import dataclass

from model.fragment import Fragment


@dataclass
class Hit:
    score: float
    fragment: Fragment

    def __hash__(self) -> int:
        return hash(self.fragment)
