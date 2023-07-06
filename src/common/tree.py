from typing import Iterator, Tuple, Optional, IO

from tree_sitter import TreeCursor, Node

from common.text import decode_normalize


def walk_children(cursor: TreeCursor, depth=0, max_depth=30) -> Iterator[TreeCursor]:
    if depth > max_depth:
        return

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


def walk_nodes(cursor: TreeCursor, *, debug: bool = False, debug_file: Optional[IO]) -> Iterator[Tuple[Node, int, int]]:
    for cur, depth in walk_children(cursor):
        node: Node = cur.node
        lineno = 1 + node.start_point[0]
        if debug and node.type.strip():
            print(f"|#{lineno:05d} {'  ' * depth}[{node.type}] {decode_normalize(node.text).rstrip()}", file=debug_file)
        yield node, lineno, depth
