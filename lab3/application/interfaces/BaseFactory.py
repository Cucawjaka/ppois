from abc import ABC

from exceptions.application_errors import FactoryError


class BaseFactory[T](ABC):
    """Базовая фабрика с общей логикой создания объектов."""

    _registry: dict[str, type[T]]
    _error_msg: str = "Неизвестный тип"

    def create(self, key: str, *args: object, **kwargs: object) -> T:
        """Функция создания объекта."""
        cls = self._registry.get(key)
        if not cls:
            msg = f"{self._error_msg}: {key}"
            raise FactoryError(msg)
        return cls(*args, **kwargs)
