import datetime
import pytest
from core.enums.product import Product
from core.exceptions import ProductionUnitError
from domain.processes.main_procceses.production.production_unit import ProductionUnit


def test_calculate_production_time(unit: ProductionUnit) -> None:
    assert unit.calculate_production_time(Product.CAR) == datetime.timedelta(days=5)


def test_start_production(unit: ProductionUnit) -> None:
    unit.start_production(Product.CAR)

    assert unit._status == "running"
    assert unit._current_task == Product.CAR


def test_start_production_with_error(unit: ProductionUnit) -> None:
    unit.start_production(Product.CAR)

    with pytest.raises(ProductionUnitError):
        unit.start_production(Product.CAR)


def test_stop_production(unit: ProductionUnit) -> None:
    unit.start_production(Product.CAR)

    unit.stop_production()

    assert unit._status == "stopped"
    assert not unit._current_task


def test_finish_production(unit: ProductionUnit) -> None:
    unit.start_production(Product.CAR)

    product: Product = unit.finish_production()

    assert unit._status == "free"
    assert product == Product.CAR


def test_finish_production_with_error(unit: ProductionUnit) -> None:
    with pytest.raises(ProductionUnitError):
        unit.finish_production()


def test_is_available(unit: ProductionUnit) -> None:
    assert unit.is_available


def test_get_status(unit: ProductionUnit) -> None:
    assert unit.get_status() == "Статус: free"
