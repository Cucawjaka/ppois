import pytest
from core.enums.CardStatus import CardStatus
from domain.cards.Card import Card
from domain.cards.Terminal import Terminal
from domain.interfaces.BankAccount import BankAccount
from exceptions.domain_errors import (
    WrongPasswordError,
    FrozenAccountError,
    TerminalError,
)
from core.enums.TransactionType import TransactionType
from domain.transactions.Transaction import Transaction


def test_terminal_insert_card_success(terminal: Terminal, card: Card):
    terminal.insert_card(card, pin=1234)
    assert terminal._current_card == card


def test_terminal_insert_card_wrong_pin(terminal: Terminal, card: Card):
    with pytest.raises(WrongPasswordError):
        terminal.insert_card(card, pin=9999)


def test_terminal_insert_card_frozen(terminal: Terminal, card: Card):
    card._status = CardStatus.FROZEN
    with pytest.raises(FrozenAccountError):
        terminal.insert_card(card, pin=1234)


def test_terminal_make_payment(terminal: Terminal, card: Card, account: BankAccount):
    terminal.insert_card(card, 1234)
    transaction: Transaction = terminal.make_payment(account, 500)
    assert isinstance(transaction, Transaction)
    assert transaction._amount == 500
    assert transaction._type == TransactionType.PAYMENT


def test_terminal_remove_card(terminal, card):
    terminal.insert_card(card, 1234)
    terminal.remove_card()
    assert terminal._current_card is None


def test_terminal_without_card_error(terminal, account):
    with pytest.raises(TerminalError):
        terminal.make_payment(account, 100)
