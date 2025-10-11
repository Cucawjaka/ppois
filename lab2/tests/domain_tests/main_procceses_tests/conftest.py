import pytest

from core.enums.Country import Country
from core.enums.Material import Material
from core.enums.Product import Product
from domain.processes.main_procceses.warehouse_logistics.Cargo import Cargo
from domain.processes.main_procceses.warehouse_logistics.Warehouse import WareHouse


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
