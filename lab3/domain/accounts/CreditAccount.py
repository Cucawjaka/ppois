from core.enums.Currency import Currency
from domain.interfaces.BankAccount import BankAccount
from domain.transactions.Transaction import Transaction
from exceptions.domain_errors import FrozenAccountError, NotEnoughMoneyError


class CreditAccount(BankAccount):
    def __init__(
        self,
        account_number: str,
        currency: Currency,
        credit_limit: int,
        interest_rate: int,
        owner_id: str,
    ):
        super().__init__(owner_id, account_number, currency)
        self._credit_limit: int = credit_limit
        self._interest_rate: int = interest_rate

    def deposit(self, money_amount: int) -> None:
        if self._is_freeze:
            raise FrozenAccountError("Аккаунт заморожен")
        self._balance += money_amount

    def refund(self) -> Transaction:
        raise NotImplementedError

    def withdraw(self, money_amount: int) -> None:
        if self._is_freeze:
            raise FrozenAccountError("Аккаунт заморожен")
        if self._balance - money_amount < -self._credit_limit:
            raise NotEnoughMoneyError("Превышен кредитный лимит")
        self._balance -= money_amount

    def apply_interest(self) -> None:
        """Начислить проценты на задолженность"""
        if self._balance > 0:
            return
        debt: int = abs(self._balance)
        interest: int = int(debt * self._interest_rate / 100)
        self._balance -= interest
