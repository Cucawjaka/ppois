from task2.IBidirectionalIterator import IBidirectionalIterator


class ReverseBidirectionalIterator[V](IBidirectionalIterator[V]):
    def __init__(self, elements: list[V], position: int | None = None) -> None:
        self._position: int = position or len(elements)
        self._elements: list[V] = elements

    def __next__(self) -> V:
        self._position -= 1

        if self._position < 0:
            raise StopIteration

        return self._elements[self._position]

    def prev(self) -> V:
        self._position += 1

        if self._position >= len(self._elements):
            raise StopIteration

        return self._elements[self._position]
