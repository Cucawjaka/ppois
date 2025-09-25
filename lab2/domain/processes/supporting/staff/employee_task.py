from enum import StrEnum, auto

from core.utils.id_generator import IDGenerator


class Status(StrEnum):
    NOT_STARTED = auto()
    COMPLITED = auto()
    IN_PROCCES = auto()


class EmployeeTask:
    def __init__(self, description: str) -> None:
        self._id: str = IDGenerator.create_uuid()
        self._status: Status = Status.NOT_STARTED
        self._description: str = description

    @property
    def id(self):
        return self.id
    

    def start(self) -> None:
        self._status = Status.IN_PROCCES


    def finish(self) -> None:
        self._status = Status.COMPLITED