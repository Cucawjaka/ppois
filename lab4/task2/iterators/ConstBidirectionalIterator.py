from task2.ConstContainer import ConstContainer
from task2.IBidirectionalIterator import IBidirectionalIterator


class ConstBidirectionalIterator[V](IBidirectionalIterator[V]):
    def __init__(self, elements: list[V], position: int = -1) -> None:
        self._position: int = position
        self._elements: list[V] = elements

    def __next__(self) -> ConstContainer[V] | V:
        self._position += 1

        if self._position >= len(self._elements):
            raise StopIteration
        if isinstance(
            self._elements[self._position],
            (int, float, str, bool, tuple, frozenset, bytes),
        ):
            return self._elements[self._position]
        return ConstContainer(self._elements[self._position])

    def prev(self) -> ConstContainer[V] | V:
        self._position -= 1

        if self._position < 0:
            raise StopIteration

        if isinstance(
            self._elements[self._position],
            (int, float, str, bool, tuple, frozenset, bytes),
        ):
            return self._elements[self._position]
        return ConstContainer(self._elements[self._position])
