import pytest

from core.enums.country import Country
from core.enums.material import Material
from core.enums.product import Product
from domain.processes.main_procceses.warehouse_logistics.cargo_sorting_plan import (
    CargoSortingPlan,
)
from domain.processes.main_procceses.warehouse_logistics.logistic_center import (
    LogisticsCenter,
)
from domain.processes.main_procceses.warehouse_logistics.warehouse import WareHouse


@pytest.fixture
def logistic_center() -> LogisticsCenter:
    return LogisticsCenter(Country.BELARUS)


@pytest.fixture
def sorting_plan(warehouse: WareHouse) -> CargoSortingPlan:
    return CargoSortingPlan(
        distribution_map={warehouse: {Material.STEEL: 5, Product.CAR: 5}}
    )
