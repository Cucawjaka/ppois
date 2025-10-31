from application.services.clients.CallCenterCervice import CallCenterService
from core.enums.TicketStatus import TicketStatus
from domain.support.SupportTicket import SupportTicket
from infrastructure.repositories.TicketsRepository import TicketsRepository


def test_create_ticket(call_center: CallCenterService, tickets_repo: TicketsRepository):
    ticket: SupportTicket = call_center.create_ticket(
        customer_id="test", message="Не работает банкомат"
    )
    assert isinstance(ticket, SupportTicket)
    assert ticket._message == "Не работает банкомат"
    assert ticket._status == TicketStatus.OPEN

    saved_ticket: SupportTicket = tickets_repo.read(ticket.id)
    assert saved_ticket == ticket


def test_register_operator(call_center: CallCenterService):
    call_center.register_operator("operator1")
    call_center.register_operator("operator2")
    assert "operator1" in call_center._operators
    assert len(call_center._operators) == 2


def test_assign_ticket(call_center: CallCenterService):
    ticket: SupportTicket = call_center.create_ticket("test", "Не работает банкомат")
    call_center.register_operator("operator1")

    call_center.assign_ticket(ticket.id)

    assert ticket._operator_id == "operator1"


def test_close_ticket(call_center: CallCenterService):
    ticket: SupportTicket = call_center.create_ticket("test", "Не работает банкомат")
    assert ticket._status == TicketStatus.OPEN

    call_center.close_ticket(ticket.id)
    assert ticket._status == TicketStatus.CLOSED
    assert ticket._resolved_at is not None


def test_ticket_reopen():
    ticker: SupportTicket = SupportTicket("1", "test", "Не работает банкомат")
    ticker.close()
    assert ticker._status == TicketStatus.CLOSED

    ticker.reopen()
    assert ticker._status == TicketStatus.OPEN
