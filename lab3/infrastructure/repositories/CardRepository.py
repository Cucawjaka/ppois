from domain.cards.Card import Card
from exceptions.infrastructure_errors import RepositoryError


class CardRepository:
    cards: dict[str, Card] = {}

    def create(self, item: Card) -> None:
        self.cards[item.id] = item

    def read(self, key: str) -> Card:
        if customer := self.cards.get(key, None):
            return customer
        raise RepositoryError("Клиент не найден")

    def delete(self, key: str) -> None:
        del self.cards[key]
