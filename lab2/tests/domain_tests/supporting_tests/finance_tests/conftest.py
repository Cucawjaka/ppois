import pytest

from core.enums.currency import Currency
from domain.processes.supporting.finance.accounting_department import (
    AccountingDepartment,
)
from domain.processes.supporting.finance.bank_account import BankAccount
from domain.processes.supporting.finance.currency_converter import CurrencyConverter
from domain.processes.supporting.finance.transaction import Transaction


@pytest.fixture(scope="function")
def accounting_department() -> AccountingDepartment:
    return AccountingDepartment("test")


@pytest.fixture
def converter() -> CurrencyConverter:
    return CurrencyConverter()


@pytest.fixture
def from_account() -> BankAccount:
    from_account: BankAccount = BankAccount("from", Currency.DOLLAR)
    from_account.deposit(200)
    return from_account


@pytest.fixture
def to_account() -> BankAccount:
    return BankAccount("to", Currency.DOLLAR)


@pytest.fixture
def transaction(
    from_account: BankAccount, to_account: BankAccount, converter: CurrencyConverter
) -> Transaction:
    return Transaction(100, from_account, to_account, converter, "salary")
