import random
from application.interfaces.IRepository import IRepository
from core.utils.IDGenerator import IDGenerator
from domain.support.SupportTicket import SupportTicket


class CallCenterService:
    def __init__(self, tickets_repo: IRepository):
        self._tickets_repo: IRepository[SupportTicket] = tickets_repo
        self._operators: list[str] = []

    def register_operator(self, operator_id: str):
        self._operators.append(operator_id)

    def create_ticket(self, customer_id: str, message: str) -> SupportTicket:
        ticket = SupportTicket(IDGenerator.create_uuid(), customer_id, message)
        self._tickets_repo.create(ticket)
        return ticket

    def assign_ticket(self, ticket_id: str):
        operator: str = random.choice(self._operators)
        ticket: SupportTicket = self._tickets_repo.read(ticket_id)
        ticket.assign_operator(operator)

    def close_ticket(self, ticket_id: str):
        ticket: SupportTicket = self._tickets_repo.read(ticket_id)
        ticket.close()
