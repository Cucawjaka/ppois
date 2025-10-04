from typing import Literal
from core.enums.material import Material
from core.enums.product import Product
from core.utils.id_generator import IDGenerator


class PurchaseOrder:
    def __init__(self, buyer: str, items: dict[Material | Product, int]) -> None:
        self._id: str = IDGenerator.create_uuid()
        self._buyer: str = buyer
        self._items: dict[Material | Product, int] = items
        self._status: Literal["pending", "approved", "shipped", "delivered", "cancelled"] = "pending"


    @property
    def buyer(self) -> str:
        return self._buyer
    

    @property
    def id(self) -> str:
        return self._id


    def approve(self) -> None:
        self._status = "approved"


    def cancel(self) -> None:
        self._status = "cancelled"


    def mark_shipped(self) -> None:
        self._status = "shipped"


    def mark_delivered(self) -> None:
        self._status = "delivered"