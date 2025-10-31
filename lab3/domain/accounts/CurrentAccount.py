from domain.interfaces.BankAccount import BankAccount
from exceptions.domain_errors import FrozenAccountError, NotEnoughMoneyError


class CurrentAccount(BankAccount):
    def deposit(self, money_amount: int) -> None:
        if self._is_freeze:
            raise FrozenAccountError("Аккаунт заморожен")
        self._balance += money_amount

    def withdraw(self, money_amount: int) -> None:
        if self._is_freeze:
            raise FrozenAccountError("Аккаунт заморожен")
        if self._balance - money_amount < 0:
            raise NotEnoughMoneyError(
                f"Недостаточно денег для снятия суммы: {money_amount}"
            )
        self._balance -= money_amount
