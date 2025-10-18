from typing import Any

from task2.errors.ConstContainerError import ConstContainerError


class ConstContainer[T]:
    __slots__ = ("_containered",)
    _containered: T

    def __init__(self, containered: T) -> None:
        object.__setattr__(self, "_containered", containered)

    def __getattribute__(self, name: str) -> Any:
        containered: T = object.__getattribute__(self, "_containered")
        try:
            return getattr(containered, name)
        except AttributeError:
            raise ConstContainerError("Невозможно менять поля у константы")

    def __setattr__(self, name: str, value: Any) -> None:
        raise ConstContainerError("Невозможно менять поля у константы")
