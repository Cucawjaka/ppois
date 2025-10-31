from dataclasses import dataclass
from datetime import datetime

from domain.cards.Card import Card


@dataclass
class CardOrder:
    id: int
    owner_id: str
    card: Card
    created_at: datetime
