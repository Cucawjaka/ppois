import pytest
from application.services.clients.CallCenterCervice import CallCenterService
from infrastructure.repositories.TicketsRepository import TicketsRepository


@pytest.fixture
def tickets_repo() -> TicketsRepository:
    return TicketsRepository()


@pytest.fixture
def call_center(tickets_repo: TicketsRepository):
    return CallCenterService(tickets_repo=tickets_repo)
