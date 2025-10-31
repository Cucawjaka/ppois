from collections import defaultdict
from application.interfaces.IRepository import IRepository
from core.enums.Denomination import Denomination
from core.utils.IDGenerator import IDGenerator
from domain.cards.Card import Card
from domain.interfaces.BankAccount import BankAccount
from exceptions.domain_errors import ATMError


class ATM:
    def __init__(
        self,
        location: str,
        cards_repo: IRepository[Card],
        accounts_repo: IRepository[BankAccount],
        withdrow_limit: int,
    ) -> None:
        self._id = IDGenerator.create_uuid()
        self._location: str = location
        self._cash: dict[Denomination, int] = defaultdict(int)
        self._cards_repo: IRepository[Card] = cards_repo
        self._accounts_repo: IRepository[BankAccount] = accounts_repo
        self._withdrow_limit: int = withdrow_limit

    def withdraw(self, card_number: str, amount: int) -> dict[Denomination, int]:
        account = self._authenticate(card_number)

        cash: dict[Denomination, int] = self._split_into_denominations(amount)

        account.deposit(amount)

        for k, v in cash.items():
            self._cash[k] -= v

        return cash

    def deposit(self, card_number: str, cash: dict[Denomination, int]) -> None:
        account = self._authenticate(card_number)

        total_amount: int = 0
        for k, v in cash.items():
            total_amount += k.value * v
            self._cash[k] += v

        account.deposit(total_amount)

    def _authenticate(self, card_number: str) -> BankAccount:
        card: Card = self._cards_repo.read(card_number)
        account: BankAccount = self._accounts_repo.read(card.account_number)

        return account

    def _split_into_denominations(self, amount: int) -> dict[Denomination, int]:
        result: dict[Denomination, int] = {}

        for denomination in sorted(Denomination, key=lambda d: d.value, reverse=True):
            count = amount // denomination.value
            if count > 0:
                result[denomination] = count
                amount -= denomination.value * count

        if amount != 0:
            raise ATMError("Сумма не может быть выдана существующими номиналами")

        return result
