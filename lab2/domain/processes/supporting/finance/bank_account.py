from core.exceptions import FrozenAccountError, NotEnoughMoneyError
from domain.processes.supporting.finance.currency import Currency


class BankAccount:
    def __init__(self,
                 account_number: str,
                 currency: Currency) -> None:
        self._account_number: str = account_number
        self._balance: int = 0
        self._currency: Currency = currency
        self._is_freeze: bool = False


    @property
    def balance(self) -> int:
        return self._balance
    

    @property
    def currency(self) -> Currency:
        return self._currency
    

    @property
    def account_number(self) -> str:
        return self._account_number
    

    def deposit(self, money_amount: int):
        if self._is_freeze:
            raise FrozenAccountError("Аккаунт заморожен")
        self._balance += money_amount
        ...


    def withdraw(self, money_amount: int) -> None:
        if self._is_freeze:
            raise FrozenAccountError("Аккаунт заморожен")
        if self._balance - money_amount < 0:
            raise NotEnoughMoneyError(f"Недостаточно денег для снятия суммы: {money_amount}")
        self._balance -= money_amount
        ...


    def freeze(self) -> None:
        self._is_freeze = True
