from enum import StrEnum, auto


class CardStatus(StrEnum):
    ACTIVE = auto()
    BLOCKED = auto()
    FROZEN = auto()
    EXPIRED = auto()
    DELIVERING = auto()
