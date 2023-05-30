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

    @staticmethod
    def clone(fragment: "Fragment") -> "Fragment":
        return Fragment(
            fragment.uuid,
            fragment.path,
            fragment.lineno,
            fragment.depth,
            fragment.type,
            fragment.name,
            fragment.text,
        )
