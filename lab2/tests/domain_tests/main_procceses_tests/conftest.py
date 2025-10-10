import pytest

from core.enums.country import Country
from domain.processes.main_procceses.warehouse_logistics.warehouse import WareHouse


@pytest.fixture
def warehouse() -> WareHouse:
    return WareHouse(Country.BELARUS)
