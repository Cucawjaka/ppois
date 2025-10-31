import pytest

from core.enums.Currency import Currency
from core.enums.TransactionType import TransactionType
from domain.accounts.CurrentAccount import CurrentAccount
from domain.exchanges.CurrencyConverter import CurrencyConverter
from domain.interfaces.BankAccount import BankAccount
from domain.transactions.Transaction import Transaction


@pytest.fixture
def converter() -> CurrencyConverter:
    return CurrencyConverter()


@pytest.fixture
def from_account() -> BankAccount:
    from_account: BankAccount = CurrentAccount("from", "from", Currency.DOLLAR)
    from_account.deposit(200)
    return from_account


@pytest.fixture
def to_account() -> BankAccount:
    return CurrentAccount("to", "to", Currency.DOLLAR)


@pytest.fixture
def transaction(
    from_account: BankAccount, to_account: BankAccount, converter: CurrencyConverter
) -> Transaction:
    return Transaction(100, from_account, to_account, converter, TransactionType.SALARY)
