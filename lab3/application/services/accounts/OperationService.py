from application.interfaces.IRepository import IRepository
from core.enums.TransactionType import TransactionType
from domain.accounts.CurrentAccount import CurrentAccount
from domain.accounts.ForeignCurrencyAccount import ForeignCurrencyAccount
from domain.clients.Customer import Customer
from domain.exchanges.CurrencyConverter import CurrencyConverter
from domain.exchanges.ExchangeRequest import ExchangeRequest
from domain.interfaces.BankAccount import BankAccount
from domain.transactions.Money import Money
from domain.transactions.Receipt import Receipt
from domain.transactions.Transaction import Transaction
from exceptions.application_errors import OperationError


class OperationService:
    def __init__(
        self,
        transaction_repo: IRepository,
        customer_repo: IRepository,
        account_repo: IRepository,
        converter: CurrencyConverter,
    ) -> None:
        self._transaction_repo: IRepository[Transaction] = transaction_repo
        self._customer_repo: IRepository[Customer] = customer_repo
        self._account_repo: IRepository[BankAccount] = account_repo
        self._currency_converter: CurrencyConverter = converter

    def create_inowner_transfer(
        self, from_number: str, to_number: str, money: Money
    ) -> Transaction:
        from_account, to_account = self._get_accounts(from_number, to_number)

        self._validate_equal_owner(from_account, to_account)
        if from_account.currency != to_account.currency:
            raise OperationError("Данный тип платежа запрещает конвертацию")

        new_transaction: Transaction = Transaction(
            amount=money.amount,
            from_account=from_account,
            to_account=to_account,
            currency_converter=CurrencyConverter(),
            type_=TransactionType.TRANSFER,
        )

        self._transaction_repo.create(new_transaction)
        return new_transaction

    def convert_currency(
        self,
        from_number: str,
        to_number: str,
        money: Money,
        exchange_request: ExchangeRequest | None,
    ) -> Transaction:
        from_account, to_account = self._get_accounts(from_number, to_number)

        self._validate_equal_owner(from_account, to_account)

        converter: CurrencyConverter = CurrencyConverter()
        if exchange_request:
            converter.set_customer_rate(exchange_request)

        new_transaction: Transaction = Transaction(
            amount=money.amount,
            from_account=from_account,
            to_account=to_account,
            currency_converter=converter,
            type_=TransactionType.TRANSFER,
        )

        self._transaction_repo.create(new_transaction)
        return new_transaction

    def create_internal_transfer(
        self, from_number: str, to_number: str, type_: TransactionType, money: Money
    ) -> Transaction:
        from_account, to_account = self._get_accounts(from_number, to_number)

        if not (
            isinstance(from_account, CurrentAccount)
            and isinstance(to_account, CurrentAccount)
        ):
            raise OperationError("Данный тип перевода запрещен")

        new_transaction: Transaction = Transaction(
            amount=money.amount,
            from_account=from_account,
            to_account=to_account,
            currency_converter=CurrencyConverter(),
            type_=type_,
        )

        self._transaction_repo.create(new_transaction)
        return new_transaction

    def create_transfer(
        self, from_number: str, to_number: str, type_: TransactionType, money: Money
    ) -> Transaction:
        from_account, to_account = self._get_accounts(from_number, to_number)

        if not (
            isinstance(from_account, ForeignCurrencyAccount)
            and isinstance(to_account, ForeignCurrencyAccount)
            and money.currency == from_account.currency
        ):
            raise OperationError("Данный тип перевода запрещен")

        new_transaction: Transaction = Transaction(
            amount=money.amount,
            from_account=from_account,
            to_account=to_account,
            currency_converter=CurrencyConverter(),
            type_=type_,
        )

        self._transaction_repo.create(new_transaction)
        return new_transaction

    def _get_accounts(
        self, from_number: str, to_number: str
    ) -> tuple[BankAccount, BankAccount]:
        from_account: BankAccount = self._account_repo.read(from_number)
        to_account: BankAccount = self._account_repo.read(to_number)

        return from_account, to_account

    def execute_operation(self, transaction: Transaction) -> Receipt:
        transaction.execute()

        return transaction.get_receipt()

    def _validate_equal_owner(
        self, from_account: BankAccount, to_account: BankAccount
    ) -> None:
        if from_account.owner_id != to_account.owner_id:
            raise OperationError("Владельцы аккаунтов не совпадают")
