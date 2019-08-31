"""
Tree class.

May 01, 2019
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from typing import Dict, Optional, Generator, Any

from typedtree.node import Node, Edge
from typedtree.traversalmode import TraversalMode


class Tree:
    def __init__(self) -> None:
        self.__nodes: Dict[str, Node] = {}

    @property
    def nodes(self) -> Dict[str, Node]:
        return self.__nodes

    def add_node(
        self,
        identifier: str,
        parent_pointer: Optional[str] = None,
        node_type: Optional[str] = None,
        edge_type: Optional[str] = None,
        payload: Optional[Any] = None,
    ) -> Node:

        parent = None
        if parent_pointer is not None:
            parent = Edge(parent_pointer, edge_type)
            self[parent_pointer].add_child(Edge(identifier, edge_type))

        node = Node(identifier, parent=parent, type=node_type, payload=payload)
        self[identifier] = node

        return node

    def display(self, identifier: str, depth: int = 0) -> None:
        node = self[identifier]

        node_type = node.type if node.type else "*Undefined*"
        edge_type = node.parent.type or "*Undefined*" if node.parent else "*Undefined*"

        if depth == 0:
            print(f"{node.identifier} [{node_type}] - ({edge_type})")
        else:
            print("\t" * depth, f"{node.identifier} [{node_type}] - ({edge_type})")

        depth += 1
        for child in node.children:
            self.display(child.pointer, depth)  # Recursive call

    def traverse(
        self, identifier: str, mode: TraversalMode = TraversalMode.DEPTH
    ) -> Generator:
        # Loosely based on an algorithm from 'Essential LISP' by John R. Anderson, Albert T. Corbett
        # and Brian J. Reiser, page 239-241

        yield identifier
        queue = self[identifier].children
        while queue:
            yield queue[0].pointer
            expansion = self[queue[0].pointer].children
            if mode is TraversalMode.DEPTH:
                queue = expansion + queue[1:]  # Depth-first traversal
            elif mode is TraversalMode.BREADTH:
                queue = queue[1:] + expansion  # Breadth-first traversal

    def __getitem__(self, key: str) -> Node:
        return self.__nodes[key]

    def __setitem__(self, key: str, item: Node) -> None:
        self.__nodes[key] = item

    def __len__(self) -> int:
        return len(self.__nodes)
