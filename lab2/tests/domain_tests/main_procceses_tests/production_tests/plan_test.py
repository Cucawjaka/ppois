from core.enums.material import Material
from domain.processes.main_procceses.production.production_order import ProductionOrder
from domain.processes.main_procceses.production.production_plan import ProductionPlan


def test_add_order(plan: ProductionPlan, order: ProductionOrder) -> None:
    plan.add_order(order)

    assert plan._orders[1] == order


def test_get_requirements(plan: ProductionPlan, order: ProductionOrder) -> None:
    plan.add_order(order)

    assert plan.get_requirements() == {Material.STEEL: 50}
