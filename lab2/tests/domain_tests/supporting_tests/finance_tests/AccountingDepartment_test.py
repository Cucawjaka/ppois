import pytest
from core.enums.Currency import Currency
from core.exceptions import AccountClosingError, NotFoundError
from domain.processes.supporting.finance.AccountingDepartment import (
    AccountingDepartment,
)
from domain.processes.supporting.finance.BankAccount import BankAccount
from domain.processes.supporting.finance.CurrencyConverter import CurrencyConverter
from domain.processes.supporting.finance.Transaction import Transaction


def test_open_account(accounting_department: AccountingDepartment) -> None:
    _: BankAccount = accounting_department.open_account("number", Currency.BYN)

    assert accounting_department._accounts[0].account_number == "number"


def test_close_account(accounting_department: AccountingDepartment) -> None:
    _: BankAccount = accounting_department.open_account("number", Currency.BYN)

    accounting_department.close_account("number")

    assert len(accounting_department._accounts) == 0


def test_close_account_with_not_found_error(
    accounting_department: AccountingDepartment,
) -> None:
    with pytest.raises(NotFoundError):
        accounting_department.close_account("test")


def test_close_account_with_error(accounting_department: AccountingDepartment) -> None:
    account: BankAccount = accounting_department.open_account("number", Currency.BYN)
    account.deposit(100)

    with pytest.raises(AccountClosingError):
        accounting_department.close_account("number")


def test_get_account_history(
    accounting_department: AccountingDepartment, converter: CurrencyConverter
) -> None:
    account: BankAccount = accounting_department.open_account("number", Currency.BYN)
    account.deposit(100)
    new_account: BankAccount = BankAccount("number2", Currency.BYN)

    transaction: Transaction = Transaction(
        1, account, new_account, converter, "payment"
    )

    accounting_department.process_transaction(transaction)

    assert transaction in accounting_department.get_account_history("number")


def test_get_account_history_with_error(
    accounting_department: AccountingDepartment,
) -> None:
    with pytest.raises(NotFoundError):
        accounting_department.get_account_history("number")


def test_calculate_total_balance(accounting_department: AccountingDepartment) -> None:
    account: BankAccount = accounting_department.open_account("number", Currency.BYN)
    account.deposit(100)

    assert accounting_department.calculate_total_balance(Currency.BYN) == 100
