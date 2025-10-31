from abc import ABC, abstractmethod

from core.enums.Currency import Currency
from domain.accounts.AccountInfo import AccountInfo


class BankAccount(ABC):
    def __init__(self, owner_id: str, account_number: str, currency: Currency) -> None:
        self._owner_id: str = owner_id
        self._account_number: str = account_number
        self._balance: int = 0
        self._currency: Currency = currency
        self._is_freeze: bool = False

    def get_account_info(self) -> AccountInfo:
        return AccountInfo(
            self._account_number, self._balance, self._currency, self._is_freeze
        )

    @property
    def balance(self) -> int:
        return self._balance

    @property
    def currency(self) -> Currency:
        return self._currency

    @property
    def account_number(self) -> str:
        return self._account_number

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @abstractmethod
    def deposit(self, money_amount: int) -> None: ...

    @abstractmethod
    def withdraw(self, money_amount: int) -> None: ...

    def freeze(self) -> None:
        self._is_freeze = True
