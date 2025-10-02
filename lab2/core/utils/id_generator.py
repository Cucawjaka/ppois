import uuid


class IDGenerator:
    def __init__(self) -> None:
        self._counter = 0


    def create_int_id(self) -> int:
        self._counter += 1
        return self._counter


    @staticmethod
    def create_uuid() -> str:
        return str(uuid.uuid4())