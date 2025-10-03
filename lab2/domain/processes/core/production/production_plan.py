from core.enums.material import Material
from core.enums.product import Product
from domain.processes.core.production.production_order import ProductionOrder
from domain.processes.core.production.technological_card import TechnologicalCard

class ProductionPlan:
    def __init__(self, orders: list[ProductionOrder]) -> None:
        self._orders: list[ProductionOrder] = orders


    @property
    def orders(self) -> list[ProductionOrder]:
        return self._orders


    def add_order(self, order: ProductionOrder) -> None:
        self._orders.append(order)


    def get_requirements(self) -> dict:
        requirements: dict[Product | Material, int] = {}
        for order in self._orders:
            for item, quantity in order.get_required_materials().items():
                requirements[item] = requirements.get(item, 0) + quantity
        return requirements
