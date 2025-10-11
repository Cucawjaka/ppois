import pytest
from core.enums.Material import Material
from core.enums.Product import Product
from core.exceptions import WrongDestinationError
from domain.processes.main_procceses.warehouse_logistics.Cargo import Cargo
from domain.processes.main_procceses.warehouse_logistics.Warehouse import WareHouse


def test_get_cargo(warehouse: WareHouse, cargo: Cargo) -> None:
    cargo.destination = warehouse._id

    warehouse.get_cargo(cargo)

    assert warehouse._products[Product.CAR] == 5
    assert warehouse._inventory[Material.STEEL] == 5


def test_get_cargo_with_error(warehouse: WareHouse, cargo: Cargo) -> None:
    with pytest.raises(WrongDestinationError):
        warehouse.get_cargo(cargo)


def test_receive_product(warehouse: WareHouse) -> None:
    warehouse.receive_item(Product.CAR, 5)

    assert warehouse._products[Product.CAR] == 5


def test_inventory_report(warehouse: WareHouse) -> None:
    warehouse.receive_item(Material.STEEL, 5)

    assert warehouse.inventory_report([Material.STEEL]) == {Material.STEEL: 5}
