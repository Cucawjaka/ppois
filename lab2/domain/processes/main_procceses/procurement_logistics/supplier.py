from core.enums.country import Country
from core.enums.material import Material
from core.enums.product import Product
from core.exceptions import PurchaseOrderError
from domain.processes.main_procceses.procurement_logistics.purchase_order import (
    PurchaseOrder,
)
from domain.processes.main_procceses.warehouse_logistics.cargo import Cargo


class Supplier:
    def __init__(
        self, name: str, country: Country, catalog: dict[Material | Product, int]
    ) -> None:
        self._name: str = name
        self._country: Country = country
        self._catalog: dict[Material | Product, int] = catalog

    def get_price(self, item: Material | Product) -> int | None:
        return self._catalog.get(item, None)

    def supply_order(self, order: PurchaseOrder) -> Cargo:
        if order._status != "approved":
            raise PurchaseOrderError("Заказ не одобрен для выполнения")
        order.mark_shipped()
        cargo = Cargo(order._items, self._name, order.buyer, "custom_required")
        return cargo
