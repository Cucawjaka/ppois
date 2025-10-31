from domain.interfaces.BankAccount import BankAccount
from domain.clients.UserInfo import UserInfo
from domain.cards.Card import Card
from exceptions.domain_errors import NotFoundError


class Customer:
    def __init__(self, id: str, info: UserInfo) -> None:
        self._id: str = id
        self._info: UserInfo = info
        self._cards: list[Card] = []
        self._accounts: list[BankAccount] = []

    @property
    def info(self) -> UserInfo:
        return self._info

    @property
    def id(self) -> str:
        return self._id

    def add_account(self, bank_account: BankAccount) -> None:
        self._accounts.append(bank_account)

    def remove_account(self, bank_account: BankAccount) -> None:
        try:
            self._accounts.remove(bank_account)
        except ValueError:
            raise NotFoundError("Аккаунт не найден.")

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def remove_card(self, card: Card) -> None:
        try:
            self._cards.remove(card)
        except ValueError:
            raise NotFoundError("Карта не найден.")
