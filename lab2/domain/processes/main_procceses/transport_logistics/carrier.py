from core.exceptions import VehicleError, NotFoundError
from domain.processes.main_procceses.transport_logistics.shipment import Shipment
from domain.processes.main_procceses.transport_logistics.vehicle import Vehicle
from domain.processes.main_procceses.warehouse_logistics.cargo import Cargo


class Carrier:
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._vehicles: list[Vehicle] = list()
        self._shipments: list[Shipment] = list()

    def register_vehicle(self, vehicle: Vehicle) -> None:
        self._vehicles.append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle) -> None:
        if vehicle not in self._vehicles:
            raise NotFoundError(f"транспорт {vehicle.vehicle_number} не найден")
        self._vehicles.remove(vehicle)

    def choose_vehicle(self, cargo: Cargo) -> Vehicle:
        for vehicle in self._vehicles:
            if not vehicle.is_busy and vehicle.can_carry(cargo):
                return vehicle
        raise VehicleError(f"{self._name} не имеет свободного транспорта")

    def add_shipment(self, shipment: Shipment) -> None:
        self._shipments.append(shipment)
