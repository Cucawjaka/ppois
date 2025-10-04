from core.utils.id_generator import IDGenerator
from domain.processes.core.sales.order import Order


class Customer:
    def __init__(self, name: str, email: str, address: str) -> None:
        self._name: str = name
        self._email: str = email
        self._address: str = address
        self._orders: list[Order] = list()


    @property
    def name(self) -> str:
        return self._name


    def add_order(self, order: Order) -> None:
        self._orders.append(order)


    def order_history(self) -> list["Order"]:
        return self._orders
