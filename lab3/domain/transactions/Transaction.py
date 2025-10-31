import datetime
from typing import Literal

from core.enums.Currency import Currency
from core.enums.TransactionType import TransactionType
from core.utils.IDGenerator import IDGenerator
from domain.exchanges.CurrencyConverter import CurrencyConverter
from domain.interfaces.BankAccount import BankAccount
from domain.transactions.Receipt import Receipt
from exceptions.domain_errors import TransactionError
from exceptions.utils_errors import ConverterError


class Transaction:
    def __init__(
        self,
        amount: int,
        from_account: BankAccount,
        to_account: BankAccount,
        currency_converter: CurrencyConverter,
        type_: TransactionType,
        description: str = "",
    ) -> None:
        self._validate_amount(amount)

        self._id: str = IDGenerator.create_uuid()
        self._amount: int = amount
        self._currency: Currency = from_account.currency
        self._from_account: BankAccount = from_account
        self._to_account: BankAccount = to_account
        self._data: datetime.datetime
        self._type: TransactionType = type_
        self._description: str = description
        self._status: Literal["complited", "pending", "failed", "wrong"] = "pending"
        self._currency_converter = currency_converter

    @property
    def from_account(self) -> BankAccount:
        return self._from_account

    @property
    def id(self) -> str:
        return self._id

    @property
    def to_account(self) -> BankAccount:
        return self._to_account

    def set_failed(self) -> None:
        self._status = "failed"

    def get_receipt(self) -> Receipt:
        if self._status != "complited":
            raise TransactionError("Транзакция еще не выполнена")
        return Receipt(
            self._amount,
            self._currency,
            self._from_account,
            self._to_account,
            self._data,
            self._type,
            self._description,
        )

    def reverce(self) -> None:
        reversed_transaction: "Transaction" = Transaction(
            amount=self._amount,
            from_account=self._to_account,
            to_account=self._from_account,
            currency_converter=self._currency_converter,
            type_=TransactionType.RETURN,
            description="",
        )
        reversed_transaction.execute()
        self._status = "wrong"

    @staticmethod
    def _validate_amount(amount: int) -> None:
        if amount < 0:
            raise TransactionError(f"Неверная сумма транзакции: {amount}")

    def execute(self) -> None:
        self._data = datetime.datetime.now()
        if self._from_account.balance < self._amount:
            self._status = "failed"
            raise TransactionError("Недостаточно средств")

        try:
            converted_amount: int = self._convert_to_currency()
            self._from_account.withdraw(self._amount)
            self._to_account.deposit(converted_amount)
            self._status = "complited"
        except ConverterError:
            raise TransactionError("Не удалось сконвертировать валюту")

    def _convert_to_currency(self) -> int:
        return self._currency_converter.convert(
            amount=self._amount,
            from_currency=self._from_account.currency,
            to_currency=self._to_account.currency,
        )
