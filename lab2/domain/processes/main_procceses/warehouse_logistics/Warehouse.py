from collections import defaultdict
from core.enums.Country import Country
from core.enums.Material import Material
from core.enums.Product import Product
from core.exceptions import WrongDestinationError
from core.utils.IDGenerator import IDGenerator

from domain.processes.main_procceses.warehouse_logistics.Cargo import Cargo


class WareHouse:
    def __init__(self, location: Country) -> None:
        self._id: str = IDGenerator.create_uuid()
        self._location: Country = location
        self._inventory: dict[Material, int] = defaultdict(int)
        self._products: dict[Product, int] = defaultdict(int)

    def get_cargo(self, cargo: Cargo) -> None:
        if cargo.destination != self._id:
            raise WrongDestinationError("Неверная точка назначения")
        for item, quantity in cargo.items.items():
            if isinstance(item, Material):
                self._inventory[item] += quantity
        if isinstance(item, Product):
            self._products[item] += quantity

    def receive_item(self, item: Material | Product, quantity: int) -> None:
        if isinstance(item, Material):
            self._inventory[item] += quantity
        if isinstance(item, Product):
            self._products[item] += quantity

    def consume_item(self, item: Material | Product, quantity: int) -> None:
        if isinstance(item, Material):
            self._inventory[item] -= quantity
        if isinstance(item, Product):
            self._products[item] -= quantity

    def check_availability(self, item: Material | Product, quantity: int) -> bool:
        if isinstance(item, Material):
            return self._inventory[item] >= quantity
        if isinstance(item, Product):
            return self._products[item] >= quantity

    def inventory_report(self, materials: list[Material]) -> dict[Material, int]:
        report: dict[Material, int] = dict()

        for material in materials:
            report[material] = self._inventory[material]

        return report
