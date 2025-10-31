import random

from core.enums.CardStatus import CardStatus
from core.enums.CardType import CardType
from core.utils.Cryptography import Cryptography
from core.utils.IDGenerator import IDGenerator
from domain.cards.ExpireDate import ExpireDate
from exceptions.domain_errors import WrongPasswordError


class Card:
    def __init__(
        self,
        expiry: ExpireDate,
        pin: int,
        owner_id: str,
        account_number: str,
        type_: CardType,
    ) -> None:
        self._owner_id: str = owner_id
        self._id: str = IDGenerator.create_uuid()
        self._account_number: str = account_number
        self._number: str = str(random.randint(10**16, 10**17 - 1))
        self._expiry: ExpireDate = expiry
        self._pin: int = Cryptography.encode_int(pin)
        self._type: CardType = type_
        self._cvv: int
        self._status: CardStatus = CardStatus.DELIVERING

    def get_number_mask(self) -> str:
        return self._account_number[-4:]

    def change_pin(self, old_pin: int, new_pin: int) -> None:
        if not Cryptography.verify_int(old_pin, self._pin):
            raise WrongPasswordError("Неверный пин код")

        self._pin = Cryptography.encode_int(new_pin)

    def verify_pin(self, pin: int) -> bool:
        return Cryptography.verify_int(pin, self._pin)

    def activate(self) -> None:
        self._status = CardStatus.ACTIVE

    def block(self) -> None:
        self._status = CardStatus.BLOCKED

    def freeze(self) -> None:
        self._status = CardStatus.FROZEN

    @property
    def owner_id(self) -> str:
        return self._owner_id

    @property
    def id(self) -> str:
        return self._id

    @property
    def account_number(self) -> str:
        return self._account_number
