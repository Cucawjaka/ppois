from datetime import datetime

from core.enums.TicketStatus import TicketStatus


class SupportTicket:
    def __init__(self, ticket_id: str, customer_id: str, message: str):
        self._id: str = ticket_id
        self._customer_id: str = customer_id
        self._message: str = message
        self._status: TicketStatus = TicketStatus.OPEN
        self._created_at: datetime = datetime.now()
        self._resolved_at: datetime | None = None

    def close(self):
        self._status = TicketStatus.CLOSED
        self._resolved_at = datetime.now()

    def reopen(self):
        self._status = TicketStatus.OPEN

    def assign_operator(self, operator_id: str):
        self._operator_id: str = operator_id

    @property
    def id(self) -> str:
        return self._id
