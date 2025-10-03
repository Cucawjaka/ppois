from collections import defaultdict, deque
from datetime import datetime

from core.enums.product import Product
from core.exceptions import ProductionLineError
from domain.processes.core.production.production_order import ProductionOrder
from domain.processes.core.production.production_unit import ProductionUnit


class ProductionLine:
    def __init__(self, name: str, machines: list[ProductionUnit]) -> None:
        self._name: str = name
        self._current_order: ProductionOrder | None = None
        self._machines: list[ProductionUnit] = machines
        self._schedule: list[tuple[ProductionUnit, datetime]] = list()
        self._created_products: dict[Product, int] = defaultdict(int)


    @property
    def created_products(self) -> dict[Product, int]:
        return self._created_products


    def add_order(self, order: ProductionOrder) -> None:
        if self._current_order is not None:
            raise ProductionLineError(f"Линия {self._name} занята")
        self._current_order = order

        self._assign_tasks()


    def _assign_tasks(self) -> None:
        if not self._current_order:
            raise ProductionLineError(f"Линия {self._name} не имеет текущего заказа")
        
        for machine in self._machines:

            if machine.is_available():
                finish_time: datetime = machine.start_production(self._current_order.product)
                self._schedule.append((machine, finish_time))
                self._current_order.quantity -= 1


    def notify_machine_finished(self, machine: ProductionUnit) -> None:
        if not self._current_order:
            raise ProductionLineError(f"Линия {self._name} не имеет текущего заказа")
        product: Product = machine.finish_production()
        self._created_products[product] += 1
        self._assign_tasks()

        if not self._current_order.quantity and \
            all(machine.is_available() for machine in self._machines):
                self._current_order = None


    def can_execute_order(self, order: ProductionOrder) -> bool:
        return any(order.product in machine.capabilities for machine in self._machines)
