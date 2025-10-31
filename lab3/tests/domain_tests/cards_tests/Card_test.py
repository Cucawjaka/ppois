import pytest
from core.enums.CardStatus import CardStatus
from exceptions.domain_errors import WrongPasswordError


def test_card_pin_verification(card):
    assert card.verify_pin(1234)
    assert not card.verify_pin(9999)


def test_card_change_pin(card):
    card.change_pin(1234, 4321)
    assert card.verify_pin(4321)
    assert not card.verify_pin(1234)


def test_card_change_pin_wrong(card):
    with pytest.raises(WrongPasswordError):
        card.change_pin(1111, 2222)


def test_card_activation_and_status(card):
    card.block()
    card.freeze()
    card.activate()
    assert card._status == CardStatus.ACTIVE
