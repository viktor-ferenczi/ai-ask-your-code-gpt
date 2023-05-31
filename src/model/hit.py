from dataclasses import dataclass

from model.fragment import Fragment


@dataclass
class Hit(Fragment):
    score: float

    @staticmethod
    def from_fragment(score: float, fragment: Fragment) -> "Hit":
        return Hit(score=score, **fragment.__dict__)
