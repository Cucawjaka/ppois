from core.enums.material import Material
from core.enums.product import Product
from core.utils.id_generator import IDGenerator
from domain.processes.main_procceses.procurement_logistics.supplier import Supplier


class Contract:
    def __init__(
        self, supplier: Supplier, buyer: str, items: dict[Material | Product, int]
    ) -> None:
        self._id: str = IDGenerator.create_uuid()
        self._supplier: Supplier = supplier
        self._buyer: str = buyer
        self._items: dict[Material | Product, int] = items
        self._price: int = self._count_price()

    @property
    def items(self) -> dict[Material | Product, int]:
        return self._items

    def _count_price(self) -> int:
        total: int = 0
        for item, quantity in self._items.items():
            price: int | None = self._supplier.get_price(item)
            if price:
                total += quantity * price
        return total
