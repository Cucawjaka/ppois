from dataclasses import dataclass

from core.enums.material import Material
from core.enums.product import Product
from domain.processes.main_procceses.warehouse_logistics.warehouse import WareHouse


@dataclass(frozen=True)
class CargoSortingPlan:
    distribution_map: dict[WareHouse, dict[Material | Product, int]]
