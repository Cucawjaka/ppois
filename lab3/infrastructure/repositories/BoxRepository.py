from domain.boxes.SafeBox import SafeBox
from exceptions.infrastructure_errors import RepositoryError


class BoxRepository:
    boxes: dict[int, SafeBox] = {}

    def create(self, item: SafeBox) -> None:
        self.boxes[item.id] = item

    def read(self, key: int) -> SafeBox:
        if customer := self.boxes.get(key, None):
            return customer
        raise RepositoryError("Ячейка не найдена")

    def delete(self, key: int) -> None:
        del self.boxes[key]
