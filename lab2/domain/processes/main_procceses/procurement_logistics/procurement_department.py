from core.enums.material import Material
from core.enums.product import Product
from core.exceptions import NotFoundError
from domain.processes.main_procceses.procurement_logistics.contract import Contract
from domain.processes.main_procceses.procurement_logistics.purchase_order import (
    PurchaseOrder,
)
from domain.processes.main_procceses.procurement_logistics.supplier import Supplier


class ProcurementDepartment:
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._suppliers: list[Supplier] = list()
        self._contracts: list[Contract] = list()
        self._orders: list[PurchaseOrder] = list()

    def register_supplier(self, supplier: Supplier) -> None:
        self._suppliers.append(supplier)

    def create_contract(
        self, supplier: Supplier, items: dict[Material | Product, int]
    ) -> Contract:
        contract = Contract(supplier, self._name, items)
        self._contracts.append(contract)
        return contract

    def place_order(self, contract: Contract) -> PurchaseOrder:
        order = PurchaseOrder(self._name, contract.items)
        order.approve()
        self._orders.append(order)
        return order

    def track_order(self, order_id: str) -> str:
        for order in self._orders:
            if order.id == order_id:
                return order._status
        raise NotFoundError("Заказ не найден")
