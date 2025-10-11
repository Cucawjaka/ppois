from core.enums.Material import Material
from domain.processes.main_procceses.production.ProductionOrder import ProductionOrder
from domain.processes.main_procceses.production.ProductionPlan import ProductionPlan


def test_add_order(plan: ProductionPlan, order: ProductionOrder) -> None:
    plan.add_order(order)

    assert plan._orders[1] == order


def test_get_requirements(plan: ProductionPlan, order: ProductionOrder) -> None:
    plan.add_order(order)

    assert plan.get_requirements() == {Material.STEEL: 50}
