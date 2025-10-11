import pytest
from core.enums.Material import Material
from core.enums.Product import Product
from domain.processes.main_procceses.production.ProductionOrder import ProductionOrder


def test_get_required_materials(order: ProductionOrder) -> None:
    assert order.get_required_materials() == {Material.STEEL: 25}


def test_quantity(order: ProductionOrder) -> None:
    assert order.quantity == 5


def test_quantity_setter(order: ProductionOrder) -> None:
    order.quantity = 3


def test_setter_with_error(order: ProductionOrder) -> None:
    with pytest.raises(ValueError):
        order.quantity = 6


def test_product(order: ProductionOrder) -> None:
    assert order.product == Product.CAR
