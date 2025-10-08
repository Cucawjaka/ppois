from typing import Self


class UserClass:
    def __init__(self, value: int) -> None:
        self._value: int = value

    @property
    def value(self) -> int:
        return self._value

    def __lt__(self, other: Self, /) -> bool:
        return self._value < other.value

    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, UserClass):
            return self._value == other.value
        return False

    def __gt__(self, other: Self, /) -> bool:
        return self._value > other.value
