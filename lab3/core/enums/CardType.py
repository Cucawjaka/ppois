from enum import StrEnum, auto


class CardType(StrEnum):
    DEBIT = auto()
    CREDIT = auto()
    VIRTUAL = auto()
