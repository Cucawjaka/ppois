from dataclasses import dataclass

from core.enums.product import Product


@dataclass
class OrderItem:
    product: Product
    quantity: int
    unit_price: int
