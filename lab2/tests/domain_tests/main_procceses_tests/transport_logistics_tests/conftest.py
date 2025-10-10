import pytest

from core.enums.country import Country
from domain.processes.main_procceses.transport_logistics.carrier import Carrier
from domain.processes.main_procceses.transport_logistics.logistics_department import (
    LogisticsDepartment,
)
from domain.processes.main_procceses.transport_logistics.route import Route
from domain.processes.main_procceses.transport_logistics.shipment import Shipment
from domain.processes.main_procceses.transport_logistics.vehicle import Vehicle
from domain.processes.main_procceses.warehouse_logistics.cargo import Cargo
from domain.processes.main_procceses.warehouse_logistics.logistic_center import (
    LogisticsCenter,
)


@pytest.fixture
def origin_center() -> LogisticsCenter:
    return LogisticsCenter(Country.BELARUS)


@pytest.fixture
def destination_center() -> LogisticsCenter:
    return LogisticsCenter(Country.BELARUS)


@pytest.fixture
def vehicle() -> Vehicle:
    return Vehicle("test", 100)


@pytest.fixture
def route(origin_center: LogisticsCenter, destination_center: LogisticsCenter) -> Route:
    return Route(origin_center, destination_center)


@pytest.fixture
def shipment(cargo: Cargo, route: Route, vehicle: Vehicle) -> Shipment:
    return Shipment(cargo, route, vehicle)


@pytest.fixture
def carrier() -> Carrier:
    return Carrier("test")


@pytest.fixture
def department() -> LogisticsDepartment:
    return LogisticsDepartment()
