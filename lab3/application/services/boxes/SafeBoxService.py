from core.utils.IDGenerator import IDGenerator
from domain.boxes.SafeBox import SafeBox
from exceptions.domain_errors import NotFoundError
from infrastructure.repositories.BoxRepository import BoxRepository


class SafeBoxService:
    def __init__(self, generator: IDGenerator, repo: BoxRepository) -> None:
        self._boxes_repo: BoxRepository = repo
        self._generator: IDGenerator = generator

    def create_box(self, price_per_month: int) -> SafeBox:
        new_id: int = self._generator.create_int_id()
        box: SafeBox = SafeBox(new_id, None, price_per_month)
        self._boxes_repo.create(box)
        return box

    def rent_box(self, box_id: int, owner_id: str, code: str, months: int) -> None:
        box = self._get_box(box_id)
        box.assign_owner(owner_id, code, months)

    def free_box(self, box_id: int) -> None:
        box: SafeBox = self._get_box(box_id)
        box.release()

    def _get_box(self, box_id: int) -> SafeBox:
        if box := self._boxes_repo.read(box_id):
            return box
        raise NotFoundError("Ячейка не найдена")
