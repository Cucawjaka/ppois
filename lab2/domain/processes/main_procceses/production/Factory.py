from core.enums.Material import Material
from core.enums.Product import Product
from domain.processes.main_procceses.production.ProductionLine import ProductionLine
from domain.processes.main_procceses.production.ProductionOrder import ProductionOrder
from domain.processes.main_procceses.production.ProductionPlan import ProductionPlan
from domain.processes.main_procceses.warehouse_logistics.Warehouse import WareHouse
from core.exceptions import FactoryError


class Factory:
    def __init__(
        self, name: str, warehouse: WareHouse, lines: list[ProductionLine]
    ) -> None:
        self._name: str = name
        self._warehouse: WareHouse = warehouse
        self._lines: list[ProductionLine] = lines
        self._current_plan: ProductionPlan | None = None

    def set_plan(self, plan: ProductionPlan) -> None:
        self._current_plan = plan

    def _check_requirements(self, order: ProductionOrder) -> bool:
        requirements: dict[Product | Material, int] = order.get_required_materials()
        for item, quantity in requirements.items():
            if not self._warehouse.check_availability(item, quantity):
                return False
        return True

    def execute_plan(self) -> None:
        if self._current_plan is None:
            raise FactoryError("Нет назначенного плана")

        for order in self._current_plan.orders:
            if not self._check_requirements(order):
                raise FactoryError(
                    f"Недостаточно материалов для заказа {order.product}"
                )

            for item, quantity in order.get_required_materials().items():
                self._warehouse.consume_item(item, quantity)

            line = self._find_line_for_order(order)
            line.add_order(order)

    def _find_line_for_order(self, order: ProductionOrder) -> ProductionLine:
        for line in self._lines:
            if line.can_execute_order(order):
                return line
        raise FactoryError(f"Нет линии для продукта {order.product}")

    def store_finished_product(self) -> None:
        for line in self._lines:
            line_products: dict[Product, int] = line.created_products
            for product, quantity in line_products.items():
                self._warehouse.receive_item(product, quantity)
