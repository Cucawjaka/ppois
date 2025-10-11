import pytest

from core.enums.Country import Country
from core.enums.Material import Material
from core.enums.Product import Product
from domain.processes.main_procceses.warehouse_logistics.CargoSortingPlan import (
    CargoSortingPlan,
)
from domain.processes.main_procceses.warehouse_logistics.LogisticCenter import (
    LogisticsCenter,
)
from domain.processes.main_procceses.warehouse_logistics.Warehouse import WareHouse


@pytest.fixture
def logistic_center() -> LogisticsCenter:
    return LogisticsCenter(Country.BELARUS)


@pytest.fixture
def sorting_plan(warehouse: WareHouse) -> CargoSortingPlan:
    return CargoSortingPlan(
        distribution_map={warehouse: {Material.STEEL: 5, Product.CAR: 5}}
    )
