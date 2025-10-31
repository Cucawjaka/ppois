from datetime import datetime

from application.interfaces.IRepository import IRepository
from core.enums.CardType import CardType
from core.utils.IDGenerator import IDGenerator
from domain.cards.Card import Card
from domain.cards.ExpireDate import ExpireDate
from domain.cards.CardOrder import CardOrder
from domain.clients.Customer import Customer


class CardOrderService:
    def __init__(
        self,
        order_repository: IRepository[Card],
        generator: IDGenerator,
        customer_repo: IRepository[Customer],
    ):
        self._cards_repo: IRepository[Card] = order_repository
        self._customer_repo: IRepository[Customer] = customer_repo
        self._generator: IDGenerator = generator

    def create_order(
        self,
        owner_id: str,
        account_number: str,
        pin: int,
        card_type: CardType,
        expiry: ExpireDate | None = None,
    ) -> CardOrder:
        if expiry is None:
            expiry = ExpireDate.create_default()

        new_card = Card(
            expiry=expiry,
            pin=pin,
            owner_id=owner_id,
            account_number=account_number,
            type_=card_type,
        )

        new_order = CardOrder(
            id=self._generator.create_int_id(),
            owner_id=owner_id,
            card=new_card,
            created_at=datetime.now(),
        )

        customer: Customer = self._customer_repo.read(owner_id)
        customer.add_card(new_card)

        self._cards_repo.create(new_card)
        return new_order

    def activate_card(self, card_order: CardOrder) -> None:
        card_order.card.activate()
