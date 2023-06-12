from dataclasses import dataclass


@dataclass
class Name:
    category: str  # Category of the code object variable
    name: str  # Name of the code object (case-sensitive)
    definition: bool  # True if this is the definition, False if this is a usage

    def __hash__(self) -> int:
        return hash(self.category) ^ hash(self.name) ^ hash(self.definition)
