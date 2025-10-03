from core.enums.material import Material
from core.enums.product import Product


class TechnologicalCard:
    def __init__(self,
                 product: Product,
                 required_materials: dict[Material | Product, int],
                 ) -> None:
        self._product: Product = product
        self._required_materials: dict[Material | Product, int] = required_materials


    @property
    def required_materials(self) -> dict[Material | Product, int]:
        return self._required_materials
    

    @property
    def product(self) -> Product:
        return self._product
