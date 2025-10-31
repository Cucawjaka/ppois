import pytest
from application.services.accounts.OperationService import OperationService
from core.enums.Currency import Currency
from core.enums.TransactionType import TransactionType
from domain.exchanges.ExchangeRequest import ExchangeRequest
from domain.interfaces.BankAccount import BankAccount
from domain.transactions.Money import Money
from domain.transactions.Transaction import Transaction
from exceptions.application_errors import OperationError


def test_create_inowner_transfer(operation_service: OperationService):
    transaction: Transaction = operation_service.create_inowner_transfer(
        from_number="1",
        to_number="2",
        money=Money(100, Currency.DOLLAR),
    )
    assert transaction._amount == 100
    assert transaction._from_account.account_number == "1"
    assert transaction._to_account.account_number == "2"
    assert transaction._status == "pending"


def test_create_inowner_transfer_different_currency(
    operation_service: OperationService, to_current: BankAccount
):
    to_current._currency = Currency.EURO
    with pytest.raises(OperationError):
        operation_service.create_inowner_transfer("1", "2", Money(100, Currency.DOLLAR))


def test_create_inowner_transfer_different_owner(operation_service: OperationService):
    with pytest.raises(OperationError):
        operation_service.create_inowner_transfer("1", "4", Money(100, Currency.DOLLAR))


def test_convert_currency(
    operation_service: OperationService, exchange_request: ExchangeRequest
):
    transaction: Transaction = operation_service.convert_currency(
        "1", "2", Money(50, Currency.DOLLAR), exchange_request
    )
    assert transaction._from_account.account_number == "1"
    assert transaction._to_account.account_number == "2"
    assert transaction._status == "pending"


def test_internal_transfer_success(operation_service: OperationService):
    transaction: Transaction = operation_service.create_internal_transfer(
        "1", "2", TransactionType.SALARY, Money(200, Currency.DOLLAR)
    )
    assert transaction._type == TransactionType.SALARY
    assert transaction._amount == 200


def test_internal_transfer_wrong_accounts(
    operation_service: OperationService,
):
    with pytest.raises(OperationError):
        operation_service.create_internal_transfer(
            "1", "4", TransactionType.SALARY, Money(100, Currency.EURO)
        )


def test_create_transfer_success(operation_service: OperationService):
    transaction: Transaction = operation_service.create_transfer(
        "3", "4", TransactionType.TRANSFER, Money(100, Currency.EURO)
    )
    assert transaction._amount == 100
    assert transaction._from_account.account_number == "3"
    assert transaction._to_account.account_number == "4"
    assert transaction._status == "pending"


def test_create_transfer_invalid_accounts(operation_service: OperationService):
    with pytest.raises(OperationError):
        operation_service.create_transfer(
            "1", "2", TransactionType.TRANSFER, Money(100, Currency.DOLLAR)
        )


def test_execute_operation(operation_service: OperationService):
    transaction: Transaction = operation_service.create_inowner_transfer(
        "1", "2", Money(100, Currency.DOLLAR)
    )
    receipt = operation_service.execute_operation(transaction)

    assert receipt.amount == 100
    assert receipt.from_account.account_number == "1"
    assert receipt.to_account.account_number == "2"
    assert transaction._status == "complited"
