from core.enums.country import Country
from core.exceptions import NotFoundError, VehicleError
from core.utils.id_generator import IDGenerator
from domain.processes.main_procceses.transport_logistics.carrier import Carrier
from domain.processes.main_procceses.transport_logistics.route import Route
from domain.processes.main_procceses.transport_logistics.shipment import Shipment
from domain.processes.main_procceses.transport_logistics.vehicle import Vehicle
from domain.processes.main_procceses.warehouse_logistics.cargo import Cargo
from domain.processes.main_procceses.warehouse_logistics.logistic_center import (
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
        checkpoints: list[LogisticsCenter] | None,
    ) -> Route:
        route = Route(origin, destination, checkpoints)
        return route

    def start_delivery(self, cargo: Cargo, route: Route) -> None:
        for carrier in self._carriers:
            try:
                vehicle: Vehicle = carrier.choose_vehicle(cargo)
            except VehicleError:
                continue

        if not vehicle:
            raise VehicleError("Нет доступного перевозчика для маршрута")

        shipment = Shipment(cargo, route, vehicle)
        carrier.add_shipment(shipment)
        self._shipments[shipment.id] = shipment
        shipment.start()

    def track_cargo(self, shipment_id: str) -> str:
        """Вернуть текущий статус груза (по всем маршрутам)."""
        shipment: Shipment | None = self._shipments.get(shipment_id, None)
        if not shipment:
            raise NotFoundError(f"Перевозка с id {shipment_id} не найдена")
        return shipment.status
