"""
Node class.

May 01, 2019
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from collections import namedtuple
from typing import Optional, List, Any

Edge = namedtuple("Edge", ["pointer", "type"])


class Node:
    def __init__(
        self,
        identifier: str,
        parent: Optional[Edge] = None,
        type: Optional[str] = None,
        payload: Optional[Any] = None,
    ) -> None:
        self.__identifier = identifier

        self.parent = parent
        self.type = type

        self.__payload = payload
        self.__children: List[Edge] = []

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
    def children(self) -> List[Edge]:
        return self.__children

    def add_child(self, edge: Edge) -> None:
        self.__children.append(edge)
