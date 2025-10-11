from core.enums.VehicleType import VehicleType
from core.exceptions import TransportError
from domain.processes.main_procceses.transport_logistics.WeightMap import WeightMap
from domain.processes.main_procceses.warehouse_logistics.Cargo import Cargo


class Vehicle:
    def __init__(self, vehicle_number: str, capacity: int) -> None:
        self._vehicle_number: str = vehicle_number
        self._type: VehicleType
        self._capacity: int = capacity
        self._is_busy: bool = False

    @property
    def vehicle_number(self) -> str:
        return self._vehicle_number

    @property
    def is_busy(self) -> bool:
        return self._is_busy

    def can_carry(self, cargo: Cargo) -> bool:
        total: float = 0

        for item, quantity in cargo.items.items():
            total += quantity * WeightMap.get_weight(item)
        return total <= self._capacity

    def assign(self) -> None:
        if self._is_busy:
            raise TransportError(f"Транспорт {self._vehicle_number} уже занят")
        self._is_busy = True

    def release(self) -> None:
        self._is_busy = False
