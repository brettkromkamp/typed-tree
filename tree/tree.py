"""
Tree class.

May 01, 2019
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from typing import Dict, Optional, Generator, Any

from tree.node import Node, Edge
from tree.treeconstant import TreeConstant


class Tree:
    # Based on this implementation: http://www.quesucede.com/page/show/id/python-3-tree-implementation

    def __init__(self) -> None:
        self.__nodes: Dict = {}

    @property
    def nodes(self) -> Dict:
        return self.__nodes

    def add_node(self, identifier: str,
                 parent: Optional[str] = None,
                 node_type: Optional[str] = None,
                 edge_type: Optional[str] = None,
                 payload: Optional[Any] = None) -> Node:
        node = Node(identifier, parent=parent, type=node_type, payload=payload)
        self[identifier] = node

        if parent is not None:
            self[parent].add_child(Edge(identifier, edge_type))

        return node

    def display(self, identifier: str, depth: int = 0) -> None:
        node = self[identifier]
        if depth == 0:
            print(f"{node.identifier} [{str(node.type)}]")
        else:
            print("\t" * depth, f"{node.identifier} [{str(node.type)}]")

        depth += 1
        for child in node.children:
            self.display(child.pointer, depth)  # Recursive call.

    def traverse(self, identifier: str, mode: TreeConstant = TreeConstant.DEPTH) -> Generator:
        # Python generator. Loosely based on an algorithm from 'Essential LISP'
        # by John R. Anderson, Albert T. Corbett, and Brian J. Reiser, page 239-241.

        yield identifier
        queue = self[identifier].children
        while queue:
            yield queue[0].pointer
            expansion = self[queue[0].pointer].children
            if mode is TreeConstant.DEPTH:
                queue = expansion + queue[1:]  # Depth-first traversal.
            elif mode is TreeConstant.BREADTH:
                queue = queue[1:] + expansion  # Breadth-first traversal.

    def __getitem__(self, key: str) -> Node:
        return self.__nodes[key]

    def __setitem__(self, key: str, item: Node) -> None:
        self.__nodes[key] = item

    def __len__(self) -> int:
        return len(self.__nodes)
