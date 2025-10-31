import pytest
from application.services.accounts.BankAccountService import BankAccountService
from core.enums.AccountType import AccountType
from core.enums.Currency import Currency
from domain.accounts.CurrentAccount import CurrentAccount
from domain.clients.Customer import Customer
from domain.interfaces.BankAccount import BankAccount
from exceptions.application_errors import BankAccountClosingError


def test_create_account(bank_account_service: BankAccountService, customer: Customer):
    new_account: BankAccount = bank_account_service.create_account(
        AccountType.CURRENT, customer, Currency.DOLLAR
    )

    assert isinstance(new_account, CurrentAccount)
    assert new_account == bank_account_service._account_repo.read(
        new_account.account_number
    )


def test_close_account_with_error(
    bank_account_service: BankAccountService, customer: Customer
):
    new_account: BankAccount = bank_account_service.create_account(
        AccountType.CURRENT, customer, Currency.DOLLAR
    )
    new_account.deposit(100)

    with pytest.raises(BankAccountClosingError):
        bank_account_service.close_account(new_account, customer)


def test_close_account(bank_account_service: BankAccountService, customer: Customer):
    new_account: BankAccount = bank_account_service.create_account(
        AccountType.CURRENT, customer, Currency.DOLLAR
    )

    bank_account_service.close_account(new_account, customer)

    assert len(customer._accounts) == 0
