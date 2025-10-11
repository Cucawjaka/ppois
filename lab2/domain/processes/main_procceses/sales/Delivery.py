from typing import Literal
from core.exceptions import SaleOrderError
from core.utils.IDGenerator import IDGenerator
from domain.processes.main_procceses.sales.Order import Order


class Delivery:
    def __init__(self, order: Order, address: str) -> None:
        self._id: str = IDGenerator.create_uuid()
        self._order: Order = order
        self._address: str = address
        self._status: Literal["scheduled", "delivering", "delivered"] = "scheduled"

    def start(self) -> None:
        if self._order.status != "paid":
            raise SaleOrderError("Нельзя отправить неоплаченный заказ")
        self._status = "delivering"
        self._order.status = "shipped"

    def complete(self) -> None:
        self._status = "delivered"
        self._order.status = "delivered"

    @property
    def status(self) -> str:
        return self._status
