from application.interfaces.BaseFactory import BaseFactory
from core.enums.AccountType import AccountType
from domain.interfaces.BankAccount import BankAccount
from domain.accounts.CreditAccount import CreditAccount
from domain.accounts.CurrentAccount import CurrentAccount
from domain.accounts.DepositAccount import DepositAccount
from domain.accounts.ForeignCurrencyAccount import ForeignCurrencyAccount


class AccountFactory(BaseFactory):
    """Класс-фабрика для создания команд."""

    def __init__(self) -> None:
        self._registry: dict[AccountType, type[BankAccount]] = {
            AccountType.CREDIT: CreditAccount,
            AccountType.CURRENT: CurrentAccount,
            AccountType.DEPOSIT: DepositAccount,
            AccountType.FOREIGN_CURRENCY: ForeignCurrencyAccount,
        }

        self._error_msg: str = "Неизвестный тип аккаунта"
