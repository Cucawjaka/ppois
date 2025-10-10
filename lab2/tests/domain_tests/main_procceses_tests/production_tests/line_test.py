import pytest
from core.enums.product import Product
from core.exceptions import ProductionLineError
from domain.processes.main_procceses.production.production_line import ProductionLine
from domain.processes.main_procceses.production.production_order import ProductionOrder
from domain.processes.main_procceses.production.production_unit import ProductionUnit


def test_add_order(line: ProductionLine, order: ProductionOrder) -> None:
    line.add_order(order)

    assert line._current_order == order


def test_add_order_with_error(line: ProductionLine, order: ProductionOrder) -> None:
    line.add_order(order)

    with pytest.raises(ProductionLineError):
        line.add_order(order)


def test_notify_machine_finished(
    line: ProductionLine, unit: ProductionUnit, order: ProductionOrder
) -> None:
    line.add_order(order)

    line.notify_machine_finished(unit)

    assert line._created_products[Product.CAR] == 1


def test_can_execute_order(line: ProductionLine, order: ProductionOrder) -> None:
    assert line.can_execute_order(order)
