import pytest
from core.exceptions import TransportError
from domain.processes.main_procceses.transport_logistics.vehicle import Vehicle


def test_assign(vehicle: Vehicle) -> None:
    pass


def test_assing_with_error(vehicle: Vehicle) -> None:
    vehicle._is_busy = True

    with pytest.raises(TransportError):
        vehicle.assign()


def test_release(vehicle: Vehicle) -> None:
    vehicle._is_busy = True

    vehicle.release()

    assert not vehicle._is_busy
