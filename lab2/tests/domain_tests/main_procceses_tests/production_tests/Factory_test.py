import pytest

from core.enums.Product import Product
from core.exceptions import FactoryError
from domain.processes.main_procceses.production.Factory import Factory
from domain.processes.main_procceses.production.ProductionPlan import ProductionPlan
from domain.processes.main_procceses.warehouse_logistics.Warehouse import WareHouse


def test_set_plan(factory: Factory, plan: ProductionPlan) -> None:
    factory.set_plan(plan)

    assert factory._current_plan == plan


def test_execute_paln_with_empty_plan_error(factory: Factory) -> None:
    with pytest.raises(FactoryError):
        factory.execute_plan()


def test_execute_plan_with_warehouse_error(
    factory: Factory, plan: ProductionPlan
) -> None:
    factory.set_plan(plan)

    with pytest.raises(FactoryError):
        factory.execute_plan()


def test_store_finished_product(factory: Factory, warehouse: WareHouse) -> None:
    factory._lines[0]._created_products = {Product.CAR: 5}

    factory.store_finished_product()

    assert warehouse._products[Product.CAR] == 5
