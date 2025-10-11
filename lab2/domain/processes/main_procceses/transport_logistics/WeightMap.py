from core.enums.Material import Material
from core.enums.Product import Product
from core.exceptions import UnknownInformationError


class WeightMap:
    weight_map: dict[Product | Material, float]

    @classmethod
    def add_weight(cls, item: Product | Material, weight: float) -> None:
        cls.weight_map[item] = weight

    @classmethod
    def get_weight(cls, item: Product | Material) -> float:
        if item not in cls.weight_map:
            raise UnknownInformationError(f"Вес {item} неизвестен")
        return cls.weight_map[item]
