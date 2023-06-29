from dataclasses import dataclass


@dataclass
class Code:
    category: str  # Category of the code object variable
    name: str  # Name of the code object (case-sensitive)
    definition: str  # The whole definition or declaration, empty if this is only a usage
    lineno: int  # Line number in the original source file
    depth: int  # Depth in the source code's structure (useful to simplify output)

    def __hash__(self) -> int:
        return hash(self.category) ^ hash(self.name) ^ (self.lineno if self.definition else 0)
