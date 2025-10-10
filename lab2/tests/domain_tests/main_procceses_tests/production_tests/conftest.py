import datetime
import pytest

from core.enums.material import Material
from core.enums.product import Product
from domain.processes.main_procceses.production.factory import Factory
from domain.processes.main_procceses.production.production_line import ProductionLine
from domain.processes.main_procceses.production.production_order import ProductionOrder
from domain.processes.main_procceses.production.production_plan import ProductionPlan
from domain.processes.main_procceses.production.production_unit import ProductionUnit
from domain.processes.main_procceses.production.technological_card import (
    TechnologicalCard,
)
from domain.processes.main_procceses.warehouse_logistics.warehouse import WareHouse


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
