from core.enums.Country import Country
from core.exceptions import NotFoundError, VehicleError
from core.utils.IDGenerator import IDGenerator
from domain.processes.main_procceses.transport_logistics.Carrier import Carrier
from domain.processes.main_procceses.transport_logistics.Route import Route
from domain.processes.main_procceses.transport_logistics.Shipment import Shipment
from domain.processes.main_procceses.transport_logistics.Vehicle import Vehicle
from domain.processes.main_procceses.warehouse_logistics.Cargo import Cargo
from domain.processes.main_procceses.warehouse_logistics.LogisticCenter import (
    LogisticsCenter,
)


class LogisticsDepartment:
    def __init__(self) -> None:
        self._id: str = IDGenerator.create_uuid()
        self._centers: dict[Country, LogisticsCenter] = dict()
        self._carriers: list[Carrier] = list()
        self._shipments: dict[str, Shipment] = dict()

    def add_center(self, center: LogisticsCenter) -> None:
        self._centers[center.country] = center

    def add_carrier(self, carrier: Carrier) -> None:
        self._carriers.append(carrier)

    def plan_delivery(
        self,
        destination: LogisticsCenter,
        origin: LogisticsCenter,
        checkpoints: list[LogisticsCenter] | None = None,
    ) -> Route:
        route = Route(origin, destination, checkpoints)
        return route

    def start_delivery(self, cargo: Cargo, route: Route) -> None:
        vehicle: Vehicle | None = None
        for carrier in self._carriers:
            try:
                vehicle = carrier.choose_vehicle(cargo)
            except VehicleError:
                continue

        if not vehicle:
            raise VehicleError("Нет доступного перевозчика для маршрута")

        shipment = Shipment(cargo, route, vehicle)
        carrier.add_shipment(shipment)
        self._shipments[shipment.id] = shipment
        shipment.start()

    def track_cargo(self, shipment_id: str) -> str:
        shipment: Shipment | None = self._shipments.get(shipment_id, None)
        if not shipment:
            raise NotFoundError(f"Перевозка с id {shipment_id} не найдена")
        return shipment.status
