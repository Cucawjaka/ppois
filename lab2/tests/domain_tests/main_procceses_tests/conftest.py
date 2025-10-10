import pytest

from core.enums.country import Country
from core.enums.material import Material
from core.enums.product import Product
from domain.processes.main_procceses.warehouse_logistics.cargo import Cargo
from domain.processes.main_procceses.warehouse_logistics.warehouse import WareHouse


@pytest.fixture
def warehouse() -> WareHouse:
    return WareHouse(Country.BELARUS)


@pytest.fixture
def cargo() -> Cargo:
    new_cargo: Cargo = Cargo(
        items={Material.STEEL: 5, Product.CAR: 5},
        origin="from_warehouse",
        destination="to_warehouse",
        customs_status="custom_required",
    )

    return new_cargo
