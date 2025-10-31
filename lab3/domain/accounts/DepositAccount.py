from datetime import date
from core.enums.Currency import Currency
from domain.interfaces.BankAccount import BankAccount
from exceptions.domain_errors import DepositException, NotEnoughMoneyError


class DepositAccount(BankAccount):
    def __init__(
        self,
        owner_id: str,
        account_number: str,
        currency: Currency,
    ):
        super().__init__(owner_id, account_number, currency)
        self._interest_rate: int = 0
        self._end_date: date | None = None

    def deposit(self, money_amount: int, interest_rate: int) -> None:
        if self._end_date:
            raise DepositException("Депозит нельзя пополнить в данный момент")
        self._interest_rate: int = interest_rate
        self._end_date: date | None = None
        self._balance += money_amount

    def withdraw(self, money_amount: int) -> None:
        if self._end_date:
            today: date = date.today()
            if today < self._end_date:
                raise DepositException(
                    "Нельзя снять деньги до окончания срока депозита"
                )
        if money_amount > self._balance:
            raise NotEnoughMoneyError(
                f"Недостаточно денег для снятия суммы: {money_amount}"
            )
        self._balance -= money_amount

    def apply_interest(self) -> None:
        """Начисление процентов по вкладу"""
        interest: int = int(self._balance * self._interest_rate / 100)
        self._balance += interest
