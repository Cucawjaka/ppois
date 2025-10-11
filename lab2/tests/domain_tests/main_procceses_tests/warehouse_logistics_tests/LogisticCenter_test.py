from core.enums.Country import Country
from core.enums.Material import Material
from core.enums.Product import Product
from domain.processes.main_procceses.warehouse_logistics.Cargo import Cargo
from domain.processes.main_procceses.warehouse_logistics.CargoSortingPlan import (
    CargoSortingPlan,
)
from domain.processes.main_procceses.warehouse_logistics.LogisticCenter import (
    LogisticsCenter,
)
from domain.processes.main_procceses.warehouse_logistics.Warehouse import WareHouse


def test_country(logistic_center: LogisticsCenter) -> None:
    assert logistic_center.country == Country.BELARUS


def test_register_warehouse(
    logistic_center: LogisticsCenter, warehouse: WareHouse
) -> None:
    logistic_center.register_warehouse(warehouse)

    assert len(logistic_center._warehauses) == 1


def test_receive_cargo(
    logistic_center: LogisticsCenter, sorting_plan: CargoSortingPlan, cargo: Cargo
) -> None:
    logistic_center.receive_cargo(cargo, sorting_plan)

    assert cargo.customs_status == "import_cleared"
    assert logistic_center._cargos[0].items == {Material.STEEL: 5, Product.CAR: 5}


def test_send_cargo(
    logistic_center: LogisticsCenter,
    sorting_plan: CargoSortingPlan,
    warehouse: WareHouse,
) -> None:
    logistic_center.register_warehouse(warehouse)
    warehouse.receive_item(Material.STEEL, 5)
    warehouse.receive_item(Product.CAR, 5)

    new_cargo: Cargo = logistic_center.send_cargo(sorting_plan, "destination")

    assert new_cargo.customs_status == "export_cleared"
    assert warehouse._products[Product.CAR] == 0
    assert warehouse._inventory[Material.STEEL] == 0
    assert new_cargo.items == {Material.STEEL: 5, Product.CAR: 5}
