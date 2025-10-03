from core.enums.material import Material
from core.enums.product import Product
from core.utils.id_generator import IDGenerator
from domain.processes.core.production.technological_card import TechnologicalCard


class ProductionOrder:
    def __init__(self, product: Product, quantity: int, technological_card: TechnologicalCard) -> None: 
        self._id = IDGenerator.create_uuid()
        self._product: Product = product
        self._quantity: int = quantity
        self._technological_card: TechnologicalCard = technological_card


    def get_required_materials(self) -> dict[Material | Product, int]:
        return {m: q * self._quantity for m, q \
                in self._technological_card.required_materials.items()}
    

    @property
    def quantity(self) -> int:
        return self._quantity
    

    @property
    def product(self) -> Product:
        return self._product
    

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        if quantity > self._quantity:
            raise ValueError("Количество единиц заказа не может быть увеличено")
        self._quantity = quantity

