from datetime import datetime
from core.enums.CreditType import CreditType
from core.utils.IDGenerator import IDGenerator
from domain.finance.CreditPayment import CreditPayment


class Credit:
    def __init__(
        self,
        customer_id: str,
        total_amount: int,
        annual_rate: int,
        months_length: int,
        start_date: datetime,
        type_: CreditType,
    ):
        self._id: str = IDGenerator.create_uuid()
        self._customer_id: str = customer_id
        self._total_amount: int = total_amount
        self._annual_rate: int = annual_rate
        self._months_length: int = months_length
        self._start_date: datetime = start_date
        self._payments: list[CreditPayment] = []
        self._closed: bool = False
        self._type: CreditType = type_

    @property
    def id(self) -> str:
        return self._id

    def set_payments(self, payments: list[CreditPayment]) -> None:
        self._payments = payments

    def get_payment(self, payment_number: int) -> CreditPayment:
        return self._payments[payment_number]

    def total_debt(self) -> float:
        return sum(p.amount for p in self._payments if not p.is_paid)

    def mark_as_closed(self):
        if self.total_debt() <= 0:
            self._closed = True
