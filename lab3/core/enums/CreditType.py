from enum import StrEnum, auto


class CreditType(StrEnum):
    MORTGAGE = auto()
    CONSUMER = auto()
    INSTALLMENT_PLAN = auto()
    LEASING = auto()
