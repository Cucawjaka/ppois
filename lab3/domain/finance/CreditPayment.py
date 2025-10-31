from datetime import datetime

from core.enums.TransactionType import TransactionType
from domain.exchanges.CurrencyConverter import CurrencyConverter
from domain.interfaces.BankAccount import BankAccount
from domain.transactions.Transaction import Transaction


class CreditPayment:
    def __init__(
        self,
        payment_date: datetime,
        amount: int,
        interest: int,
        payment_account: BankAccount,
    ) -> None:
        self._payment_date: datetime = payment_date
        self._amount: int = amount
        self._interest: int = interest
        self._is_paid: bool = False
        self._paid_at: datetime | None = None
        self._account_for_payment: BankAccount = payment_account

    def create_pay_transaction(self, from_account: BankAccount) -> Transaction:
        return Transaction(
            amount=self._amount,
            from_account=from_account,
            to_account=self._account_for_payment,
            currency_converter=CurrencyConverter(),
            type_=TransactionType.PAYMENT,
        )

    def set_paid(self) -> None:
        self._is_paid = True

    @property
    def amount(self) -> int:
        return self._amount

    def is_paid(self) -> bool:
        return not self._is_paid
