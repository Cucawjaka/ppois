from core.enums.status import Status
from core.utils.id_generator import IDGenerator


class EmployeeTask:
    def __init__(self, description: str) -> None:
        self._id: str = IDGenerator.create_uuid()
        self._status: Status = Status.NOT_STARTED
        self._description: str = description

    @property
    def id(self) -> str:
        return self._id

    def start(self) -> None:
        self._status = Status.IN_PROCCES

    def finish(self) -> None:
        self._status = Status.COMPLITED
