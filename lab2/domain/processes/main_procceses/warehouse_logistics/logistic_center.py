from collections import defaultdict
from core.enums.country import Country
from core.enums.material import Material
from core.enums.product import Product
from core.exceptions import NotEnoughItemError
from core.utils.id_generator import IDGenerator

from domain.processes.main_procceses.warehouse_logistics.cargo import Cargo
from domain.processes.main_procceses.warehouse_logistics.cargo_sorting_plan import (
    CargoSortingPlan,
)
from domain.processes.main_procceses.warehouse_logistics.warehouse import WareHouse


class LogisticsCenter:
    def __init__(self, country: Country) -> None:
        self._id: str = IDGenerator.create_uuid()
        self._country: Country = country
        self._warehauses: list[WareHouse] = list()
        self._cargos: list[Cargo] = list()

    @property
    def country(self) -> Country:
        return self._country

    def register_warehouse(self, warehouse: WareHouse) -> None:
        self._warehauses.append(warehouse)

    def _pass_cargo_through_custmoms(self, cargo: Cargo) -> None:
        """пройти таможенный досмотр"""
        cargo.customs_status = "import_cleared"

    def _clear_cargo_through_customs(self, cargo: Cargo) -> None:
        cargo.customs_status = "export_cleared"

    def receive_cargo(self, cargo: Cargo, cargo_sorting_plan: CargoSortingPlan) -> None:
        if cargo.customs_status == "custom_required":
            self._pass_cargo_through_custmoms(cargo)

        destination_map: dict[WareHouse, dict[Material | Product, int]] = (
            cargo_sorting_plan.distribution_map
        )

        for wh, items in destination_map.items():
            new_cargo: Cargo = Cargo(items, self._id, wh._id, "domestic")
            self._cargos.append(new_cargo)

    def send_cargo(
        self, cargo_sorting_plan: CargoSortingPlan, destination: str
    ) -> Cargo:
        destination_map: dict[WareHouse, dict[Material | Product, int]] = (
            cargo_sorting_plan.distribution_map
        )
        cargo_items: dict[Material | Product, int] = defaultdict(int)

        for wh, items in destination_map.items():
            for item, quantity in items.items():
                if not wh.check_availability(item, quantity):
                    raise NotEnoughItemError("Недостаточное количество на складе")

                wh.consume_item(item, quantity)

                cargo_items[item] += quantity

        new_cargo: Cargo = Cargo(cargo_items, self._id, destination, "custom_required")
        self._clear_cargo_through_customs(new_cargo)

        return new_cargo
