from typing import List

from model.fragment import Fragment


def uuid_of_fragments(fragments: List[Fragment]) -> List[str]:
    return [fragment.uuid for fragment in fragments]
