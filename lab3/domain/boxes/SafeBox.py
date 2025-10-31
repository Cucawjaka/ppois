from datetime import datetime, timedelta


class SafeBox:
    def __init__(self, box_id: int, owner_id: str | None, price_per_month: int) -> None:
        self._id: int = box_id
        self._owner_id: str | None = owner_id
        self._price_per_month: int = price_per_month
        self._is_occupied: bool = False
        self._access_code: str | None = None
        self._occuplied_until: datetime | None = None

    def assign_owner(self, owner_id: str, access_code: str, months: int):
        self._owner_id = owner_id
        self._access_code = access_code
        self._is_occupied = True
        self._occuplied_until = datetime.now() + timedelta(days=30 * months)

    def release(self):
        self._is_occupied = False
        self._access_code = None
        self._occuplied_until = None

    def verify_access(self, code: str) -> bool:
        return self._access_code == code

    @property
    def id(self) -> int:
        return self._id
