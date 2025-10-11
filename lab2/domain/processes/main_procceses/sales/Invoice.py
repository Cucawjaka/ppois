from datetime import datetime
from core.utils.IDGenerator import IDGenerator
from domain.processes.main_procceses.sales.Order import Order


class Invoice:
    def __init__(self, order: Order) -> None:
        self._id: str = IDGenerator.create_uuid()
        self._order: Order = order
        self._amount: int = order.calculate_total()
        self._paid_date: datetime | None = None
        self._paid: bool = False

    def pay(self) -> None:
        self._paid = True
        self._paid_date = datetime.now()
        self._order.status = "paid"

    @property
    def is_paid(self) -> bool:
        return self._paid

    @property
    def id(self) -> str:
        return self._id
