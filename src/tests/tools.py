from typing import List

from common.tools import find
from model.fragment import Fragment
from model.result import Result


async def nums_from_results(fragments: List[Fragment], results: List[Result]):
    return [find(fragments, lambda fragment: fragment.uuid == result.uuid) for result in results]
