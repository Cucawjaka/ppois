from core.enums.Country import Country
from core.enums.Material import Material
from core.enums.Product import Product
from core.exceptions import PurchaseOrderError
from domain.processes.main_procceses.procurement_logistics.PurchaseOrder import (
    PurchaseOrder,
)
from domain.processes.main_procceses.warehouse_logistics.Cargo import Cargo


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
