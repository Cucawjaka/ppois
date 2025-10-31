from dataclasses import dataclass

from core.enums.Currency import Currency


@dataclass(frozen=True)
class Money:
    amount: int
    currency: Currency
