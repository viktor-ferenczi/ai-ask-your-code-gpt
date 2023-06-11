from typing import Iterator

from tree_sitter import TreeCursor, Node


def walk_children(cursor: TreeCursor, depth=0) -> Iterator[TreeCursor]:
    node: Node = cursor.node
    child_count = node.child_count
    if not child_count:
        return

    cursor.goto_first_child()
    for i in range(child_count):
        if i:
            cursor.goto_next_sibling()
        yield cursor, depth
        yield from walk_children(cursor, depth + 1)

    cursor.goto_parent()
