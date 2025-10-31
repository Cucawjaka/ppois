from core.enums.CardStatus import CardStatus
from core.enums.TransactionType import TransactionType
from domain.cards.Card import Card
from domain.exchanges.CurrencyConverter import CurrencyConverter
from domain.interfaces.BankAccount import BankAccount
from domain.transactions.Transaction import Transaction
from exceptions.domain_errors import (
    FrozenAccountError,
    TerminalError,
    WrongPasswordError,
)
from core.utils.IDGenerator import IDGenerator


class Terminal:
    def __init__(self, owner_account: BankAccount):
        self._owner_account: BankAccount = owner_account
        self._id: str = IDGenerator.create_uuid()
        self._transactions: list[Transaction] = []
        self._current_card: Card | None = None

    def insert_card(self, card: Card, pin: int) -> None:
        if not card.verify_pin(pin):
            raise WrongPasswordError("Неверный PIN-код")

        if card._status != CardStatus.ACTIVE:
            raise FrozenAccountError("Карта неактивна или заморожена")

        self._current_card = card

    def remove_card(self) -> None:
        self._current_card = None

    def make_payment(self, from_account: BankAccount, amount: int) -> Transaction:
        self._check_card()

        transaction = Transaction(
            amount=amount,
            from_account=from_account,
            to_account=self._owner_account,
            currency_converter=CurrencyConverter(),
            type_=TransactionType.PAYMENT,
        )

        self._transactions.append(transaction)
        return transaction

    def get_transaction_history(self) -> list[Transaction]:
        return self._transactions

    def _check_card(self) -> None:
        if self._current_card is None:
            raise TerminalError("Карта не вставлена")

    @property
    def id(self) -> str:
        return self._id
