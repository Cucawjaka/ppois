import pytest
from core.exceptions import NotFoundError, VehicleError
from domain.processes.main_procceses.transport_logistics.Carrier import Carrier
from domain.processes.main_procceses.transport_logistics.Shipment import Shipment
from domain.processes.main_procceses.transport_logistics.Vehicle import Vehicle
from domain.processes.main_procceses.warehouse_logistics.Cargo import Cargo


def test_register_vehicle(carrier: Carrier, vehicle: Vehicle) -> None:
    carrier.register_vehicle(vehicle)

    assert carrier._vehicles[0] == vehicle


def test_remove_vehicle(carrier: Carrier, vehicle: Vehicle) -> None:
    carrier.register_vehicle(vehicle)

    carrier.remove_vehicle(vehicle)

    assert len(carrier._vehicles) == 0


def test_remove_vehicle_with_error(carrier: Carrier, vehicle: Vehicle) -> None:
    with pytest.raises(NotFoundError):
        carrier.remove_vehicle(vehicle)


def test_choose_vehicle_with_error(carrier: Carrier, cargo: Cargo) -> None:
    with pytest.raises(VehicleError):
        carrier.choose_vehicle(cargo)


def test_add_shipment(carrier: Carrier, shipment: Shipment) -> None:
    carrier.add_shipment(shipment)

    assert carrier._shipments[0] == shipment
