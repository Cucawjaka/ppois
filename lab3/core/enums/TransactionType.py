from enum import StrEnum, auto


class TransactionType(StrEnum):
    TRANSFER = auto()
    TAX = auto()
    SALARY = auto()
    PAYMENT = auto()
    RETURN = auto()
