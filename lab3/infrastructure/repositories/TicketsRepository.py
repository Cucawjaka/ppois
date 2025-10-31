from domain.support.SupportTicket import SupportTicket
from exceptions.infrastructure_errors import RepositoryError


class TicketsRepository:
    tickets: dict[str, SupportTicket] = {}

    def create(self, item: SupportTicket) -> None:
        self.tickets[item.id] = item

    def read(self, key: str) -> SupportTicket:
        if account := self.tickets.get(key, None):
            return account
        raise RepositoryError("Тикет не найден")

    def delete(self, key: str) -> None:
        del self.tickets[key]
