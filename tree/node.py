"""
Node class.

May 01, 2019
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from typing import Optional, List, Any


class Node:
    # Based on this implementation: http://www.quesucede.com/page/show/id/python-3-tree-implementation

    def __init__(self, identifier: str, parent: Optional[str] = None, payload: Optional[Any] = None) -> None:
        self.__identifier = identifier

        self.parent = parent

        self.__payload = payload
        self.__children: List[str] = []

    @property
    def identifier(self) -> str:
        return self.__identifier

    @property
    def payload(self) -> Optional[Any]:
        return self.__payload

    @payload.setter
    def payload(self, value: Any) -> None:
        self.__payload = value

    @property
    def children(self) -> List[str]:
        return self.__children

    def add_child(self, identifier: str) -> None:
        self.__children.append(identifier)
