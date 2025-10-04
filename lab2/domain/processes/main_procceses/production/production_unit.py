from datetime import datetime, timedelta
from typing import Literal
from core.enums.product import Product
from core.exceptions import InvalidProductError, ProductionUnitError


class ProductionUnit:
    def __init__(self, capabilities: dict[Product, timedelta], name: str) -> None:
        self._name: str = name
        self._capabilities: dict[Product, timedelta] = capabilities
        self._status: Literal["free", "running", "stopped", "maintenance"] = "free"
        self._current_task: Product | None = None
        self._start_time: datetime | None = None
        self._expected_finish: datetime | None = None

    @property
    def capabilities(self) -> dict[Product, timedelta]:
        return self._capabilities

    @property
    def expected_finish(self) -> datetime | None:
        return self._expected_finish

    def calculate_production_time(self, product: Product) -> timedelta:
        if product not in self._capabilities:
            raise InvalidProductError(f"{self._name} не может производить {product}")
        return self._capabilities[product]

    def start_production(self, product: Product) -> datetime:
        if self._status == "running":
            raise ProductionUnitError("Станок уже занят")

        production_time = self.calculate_production_time(product)
        self._status = "running"
        self._current_task = product
        self._start_time = datetime.now()
        self._expected_finish = self._start_time + production_time
        return self._expected_finish

    def stop_production(self) -> None:
        self._status = "stopped"
        self._current_task = None
        self._start_time = None
        self._expected_finish = None

    def finish_production(self) -> Product:
        if self._current_task is None:
            raise ProductionUnitError("Станок ничего не производит")

        product: Product = self._current_task
        self._status = "free"
        self._current_task = None
        self._start_time = None
        self._expected_finish = None
        return product

    def is_available(self) -> bool:
        return self._status in ["free", "stopped"]

    def get_status(self) -> str:
        if self._status == "running":
            return f"Производит {self._current_task}, закончит через {self._expected_finish}"
        return f"Статус: {self._status}"
