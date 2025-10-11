from core.enums.Advertisement import Advertisement


class AdvertisingChannel:
    def __init__(
        self,
        type_: Advertisement,
        name: str = "",
    ) -> None:
        self._name: str = name
        self._type: Advertisement = type_
        self._clicks: int = 0
        self._shows: int = 0
        self._conversions: int = 0
        self._budget: int = 0

    def set_budget(self, budget: int) -> None:
        if budget < 0:
            raise ValueError("Бюджет не может быть меньше 0")
        self._budget = budget

    def calculate_ctr(self) -> float:
        return self._clicks / self._shows * 100

    def calculate_cvr(self) -> float:
        return self._conversions / self._clicks * 100

    def record_conversions(self, count: int) -> None:
        self._conversions = count

    def record_shows(self, count: int) -> None:
        self._shows = count

    def record_clicks(self, count: int) -> None:
        self._clicks = count
