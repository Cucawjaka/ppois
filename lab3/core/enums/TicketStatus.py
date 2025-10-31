from enum import StrEnum, auto


class TicketStatus(StrEnum):
    CLOSED = auto()
    OPEN = auto()
