from dataclasses import dataclass

from core.enums.Currency import Currency


@dataclass(frozen=True)
class AccountInfo:
    account_number: str
    balance: int
    currency: Currency
    is_freeze: bool
