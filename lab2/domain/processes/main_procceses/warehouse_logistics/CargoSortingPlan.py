from dataclasses import dataclass

from core.enums.Material import Material
from core.enums.Product import Product
from domain.processes.main_procceses.warehouse_logistics.Warehouse import WareHouse


@dataclass(frozen=True)
class CargoSortingPlan:
    distribution_map: dict[WareHouse, dict[Material | Product, int]]
