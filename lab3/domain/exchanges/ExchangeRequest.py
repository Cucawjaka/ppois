from dataclasses import dataclass, field
from datetime import datetime

from core.enums.Currency import Currency


@dataclass(frozen=True)
class ExchangeRequest:
    offer_id: str
    owner_id: str
    from_currency: Currency
    to_currency: Currency
    from_amount: int
    rate: float
    created_at: datetime = field(default_factory=datetime.now)
