from application.interfaces.BaseFactory import BaseFactory
from core.enums.AccountType import AccountType
from core.enums.Currency import Currency
from core.utils.IDGenerator import IDGenerator
from domain.clients.Customer import Customer
from application.interfaces.IRepository import IRepository
from domain.interfaces.BankAccount import BankAccount
from exceptions.application_errors import BankAccountClosingError


class BankAccountService:
    def __init__(self, account_factory: BaseFactory, account_repo: IRepository) -> None:
        self._account_repo: IRepository[BankAccount] = account_repo
        self._account_factory: BaseFactory = account_factory

    def create_account(
        self, account_type: AccountType, customer: Customer, currency: Currency
    ) -> BankAccount:
        new_account: BankAccount = self._account_factory.create(
            owner_id=customer.id,
            key=account_type,
            account_number=IDGenerator.create_uuid(),
            currency=currency,
        )

        self._account_repo.create(new_account)
        customer.add_account(new_account)
        return new_account

    def close_account(self, account: BankAccount, customer: Customer) -> None:
        if account.balance != 0:
            raise BankAccountClosingError(
                "Невозможно закрыть счет с ненулевым балансом"
            )

        self._account_repo.delete(account.account_number)
        customer.remove_account(account)
