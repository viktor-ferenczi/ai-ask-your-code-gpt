from dataclasses import dataclass


@dataclass
class Fragment:
    uuid: str  # Unique identifier of the fragment, UUID4
    path: str  # Path of the source file
    lineno: int  # Line number inside the source file
    depth: int  # Depth in the logical structure of the code, 0 is the module global level
    category: str  # Type of the code construct, for example: function, class, interface, method, field, variable, macro
    name: str  # Name of the code construct
    body: str  # Definition of the code construct in case of definitions, empty string in case of usage

