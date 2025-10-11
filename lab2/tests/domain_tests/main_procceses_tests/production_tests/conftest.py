import datetime
import pytest

from core.enums.Material import Material
from core.enums.Product import Product
from domain.processes.main_procceses.production.Factory import Factory
from domain.processes.main_procceses.production.ProductionLine import ProductionLine
from domain.processes.main_procceses.production.ProductionOrder import ProductionOrder
from domain.processes.main_procceses.production.ProductionPlan import ProductionPlan
from domain.processes.main_procceses.production.ProductionUnit import ProductionUnit
from domain.processes.main_procceses.production.TechnologicalCard import (
    TechnologicalCard,
)
from domain.processes.main_procceses.warehouse_logistics.Warehouse import WareHouse


@pytest.fixture
def card() -> TechnologicalCard:
    return TechnologicalCard(Product.CAR, {Material.STEEL: 5})


@pytest.fixture
def order(card: TechnologicalCard) -> ProductionOrder:
    return ProductionOrder(5, card)


@pytest.fixture
def plan(order: ProductionOrder) -> ProductionPlan:
    return ProductionPlan([order])


@pytest.fixture
def unit() -> ProductionUnit:
    return ProductionUnit(
        capabilities={Product.CAR: datetime.timedelta(days=5)}, name="test"
    )


@pytest.fixture
def line(unit: ProductionUnit) -> ProductionLine:
    return ProductionLine("test", [unit])


@pytest.fixture
def factory(warehouse: WareHouse, line: ProductionLine) -> Factory:
    return Factory("test", warehouse, [line])
