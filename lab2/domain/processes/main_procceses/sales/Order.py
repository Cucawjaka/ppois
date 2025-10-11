from typing import Literal
from core.exceptions import SaleOrderError
from core.utils.IDGenerator import IDGenerator
from domain.processes.main_procceses.sales.OrderItem import OrderItem


class Order:
    def __init__(self) -> None:
        self._id: str = IDGenerator.create_uuid()
        self._items: list[OrderItem] = list()
        self._status: Literal[
            "pending", "paid", "shipped", "delivered", "cancelled"
        ] = "pending"

    @property
    def status(self) -> Literal["pending", "paid", "shipped", "delivered", "cancelled"]:
        return self._status

    @status.setter
    def status(
        self, status: Literal["pending", "paid", "shipped", "delivered", "cancelled"]
    ) -> None:
        self._status = status

    @property
    def id(self) -> str:
        return self._id

    def calculate_total(self) -> int:
        return sum(item.unit_price * item.quantity for item in self._items)

    def cancel(self) -> None:
        self._status = "cancelled"

    def add_item(self, item: OrderItem) -> None:
        self._items.append(item)

    def remove_item(self, item: OrderItem) -> None:
        if item not in self._items:
            raise SaleOrderError("Позиции в заказе не существует")
