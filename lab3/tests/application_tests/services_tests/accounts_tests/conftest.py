import pytest
from application.factories.AccountFactory import AccountFactory
from application.services.accounts.BankAccountService import BankAccountService
from application.services.accounts.OperationService import OperationService
from core.enums.Currency import Currency
from domain.accounts.CurrentAccount import CurrentAccount
from domain.accounts.ForeignCurrencyAccount import ForeignCurrencyAccount
from domain.clients.Customer import Customer
from domain.clients.UserInfo import UserInfo
from domain.exchanges.CurrencyConverter import CurrencyConverter
from domain.exchanges.ExchangeRequest import ExchangeRequest
from domain.interfaces.BankAccount import BankAccount
from infrastructure.repositories.AccountRepository import AccountRepository
from infrastructure.repositories.CustomerRepository import CustomerRepository
from infrastructure.repositories.TransactionRepository import TransactionRepository


@pytest.fixture
def converter() -> CurrencyConverter:
    return CurrencyConverter()


@pytest.fixture
def customer() -> Customer:
    user_info: UserInfo = UserInfo(123, "exapmle@mail.ru", "123", 123)
    return Customer("test", user_info)


@pytest.fixture
def from_current(customer: Customer) -> BankAccount:
    from_account: BankAccount = CurrentAccount(customer.id, "1", Currency.DOLLAR)
    from_account.deposit(200)
    return from_account


@pytest.fixture
def to_current(customer: Customer) -> BankAccount:
    return CurrentAccount(customer.id, "2", Currency.DOLLAR)


@pytest.fixture
def from_foreign(customer: Customer) -> BankAccount:
    from_account: ForeignCurrencyAccount = ForeignCurrencyAccount(
        customer.id, "3", Currency.EURO
    )
    from_account.deposit(800)
    return from_account


@pytest.fixture
def to_foreign(customer: Customer) -> BankAccount:
    return ForeignCurrencyAccount(customer.id, "4", Currency.EURO)


@pytest.fixture
def account_repo(
    from_current: BankAccount,
    to_current: BankAccount,
    from_foreign: BankAccount,
    to_foreign: BankAccount,
) -> AccountRepository:
    account_repo: AccountRepository = AccountRepository()

    account_repo.create(from_current)
    account_repo.create(to_current)
    account_repo.create(from_foreign)
    account_repo.create(to_foreign)

    return account_repo


@pytest.fixture
def customer_repo(customer: Customer) -> CustomerRepository:
    customer_repo: CustomerRepository = CustomerRepository()

    customer_repo.create(customer)

    return customer_repo


@pytest.fixture
def transaction_repo() -> TransactionRepository:
    return TransactionRepository()


@pytest.fixture
def operation_service(
    transaction_repo: TransactionRepository,
    customer_repo: CustomerRepository,
    account_repo: AccountRepository,
    converter: CurrencyConverter,
) -> OperationService:
    return OperationService(
        transaction_repo=transaction_repo,
        customer_repo=customer_repo,
        account_repo=account_repo,
        converter=converter,
    )


@pytest.fixture
def exchange_request() -> ExchangeRequest:
    return ExchangeRequest("1", "2", Currency.DOLLAR, Currency.DOLLAR, 1, 2)


@pytest.fixture
def bank_account_service(account_repo: AccountRepository) -> BankAccountService:
    factory: AccountFactory = AccountFactory()
    return BankAccountService(factory, account_repo)
