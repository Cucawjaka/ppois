from datetime import datetime
from typing import Literal
from core.utils.IDGenerator import IDGenerator
from domain.processes.main_procceses.transport_logistics.Route import Route
from domain.processes.main_procceses.transport_logistics.Vehicle import Vehicle
from domain.processes.main_procceses.warehouse_logistics.Cargo import Cargo


class Shipment:
    def __init__(self, cargo: Cargo, route: Route, vehicle: Vehicle) -> None:
        self._id: str = IDGenerator.create_uuid()
        self._cargo: Cargo = cargo
        self._route: Route = route
        self._vehicle: Vehicle = vehicle
        self._status: Literal["planned", "in_transit", "delivered"] = "planned"
        self._start_time: datetime
        self._end_time: datetime

    @property
    def status(self) -> str:
        return self._status

    @property
    def id(self) -> str:
        return self._id

    def start(self) -> None:
        self._vehicle.assign()
        self._start_time = datetime.now()
        self._status = "in_transit"

    def complete(self) -> None:
        self._vehicle.release()
        self._end_time = datetime.now()
        self._status = "delivered"
