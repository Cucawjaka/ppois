from abc import ABC, abstractmethod
from typing import Self

from task2.ConstContainer import ConstContainer


class IBidirectionalIterator[V](ABC):
    _position: int
    _elements: list[V]

    @property
    def position(self) -> int:
        return self._position

    def __iter__(self) -> Self:
        return self

    @abstractmethod
    def __next__(self) -> V | ConstContainer[V] | V: ...

    @abstractmethod
    def prev(self) -> V | ConstContainer[V] | V: ...

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, type(self)):
            return False

        return self._elements == value._elements and self._position == value.position
