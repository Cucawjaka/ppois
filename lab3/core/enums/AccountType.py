from enum import StrEnum, auto


class AccountType(StrEnum):
    CREDIT = auto()
    CURRENT = auto()
    DEPOSIT = auto()
    FOREIGN_CURRENCY = auto()
