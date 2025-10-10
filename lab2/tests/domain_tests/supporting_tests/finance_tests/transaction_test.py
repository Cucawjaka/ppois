import pytest
from core.enums.currency import Currency
from core.exceptions import TransactionError
from domain.processes.supporting.finance.bank_account import BankAccount
from domain.processes.supporting.finance.receipt import Receipt
from domain.processes.supporting.finance.transaction import Transaction


def test_from_account(transaction: Transaction, from_account: BankAccount) -> None:
    assert transaction.from_account == from_account


def test_to_account(transaction: Transaction, to_account: BankAccount) -> None:
    assert transaction.to_account == to_account


def test_set_failed(transaction: Transaction) -> None:
    transaction.set_failed()

    assert transaction._status == "failed"


def test_get_receipt(transaction: Transaction) -> None:
    transaction.execute()

    receipt: Receipt = transaction.get_receipt()

    assert receipt.amount == 100
    assert receipt.currency == Currency.DOLLAR
    assert receipt.type == "salary"


def test_get_receipt_with_error(transaction: Transaction) -> None:
    with pytest.raises(TransactionError):
        transaction.get_receipt()


def test_reverce(
    transaction: Transaction, from_account: BankAccount, to_account: BankAccount
) -> None:
    transaction.execute()
    transaction.reverce()

    assert from_account.balance == 200
    assert to_account.balance == 0
    assert transaction._status == "wrong"


def test_execute(
    transaction: Transaction, from_account: BankAccount, to_account: BankAccount
) -> None:
    transaction.execute()

    assert from_account.balance == 100
    assert to_account.balance == 100
    assert transaction._status == "complited"


def test_execute_with_error(
    transaction: Transaction, from_account: BankAccount
) -> None:
    from_account.withdraw(180)
    with pytest.raises(TransactionError):
        transaction.execute()

    assert transaction._status == "failed"
