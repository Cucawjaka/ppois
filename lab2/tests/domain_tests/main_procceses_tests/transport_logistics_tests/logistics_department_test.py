import pytest
from core.enums.country import Country
from core.exceptions import NotFoundError, VehicleError
from domain.processes.main_procceses.transport_logistics.carrier import Carrier
from domain.processes.main_procceses.transport_logistics.logistics_department import (
    LogisticsDepartment,
)
from domain.processes.main_procceses.transport_logistics.route import Route
from domain.processes.main_procceses.transport_logistics.shipment import Shipment
from domain.processes.main_procceses.warehouse_logistics.cargo import Cargo
from domain.processes.main_procceses.warehouse_logistics.logistic_center import (
    LogisticsCenter,
)


def test_add_center(
    department: LogisticsDepartment, origin_center: LogisticsCenter
) -> None:
    department.add_center(origin_center)

    assert department._centers[Country.BELARUS] == origin_center


def test_add_carrier(department: LogisticsDepartment, carrier: Carrier) -> None:
    department.add_carrier(carrier)

    assert department._carriers[0] == carrier


def test_plan_delivery(
    department: LogisticsDepartment,
    origin_center: LogisticsCenter,
    destination_center: LogisticsCenter,
) -> None:
    route: Route = department.plan_delivery(destination_center, origin_center)

    assert not route.checkpoints
    assert route.origin == origin_center
    assert route.destination == destination_center


def test_start_delivery_with_error(
    department: LogisticsDepartment, cargo: Cargo, route: Route
) -> None:
    with pytest.raises(VehicleError):
        department.start_delivery(cargo, route)


def test_track_cargo_with_error(
    department: LogisticsDepartment, shipment: Shipment
) -> None:
    with pytest.raises(NotFoundError):
        department.track_cargo("test")
