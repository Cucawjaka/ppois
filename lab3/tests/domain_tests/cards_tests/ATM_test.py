from core.enums.Denomination import Denomination
from domain.cards.ATM import ATM
from domain.cards.Card import Card
from domain.interfaces.BankAccount import BankAccount


def test_atm_deposit_and_withdraw(atm: ATM, card: Card):
    deposit_cash = {Denomination.FIFTY: 2, Denomination.HUNDRED: 1}
    atm.deposit(card_number=card.id, cash=deposit_cash)

    account: BankAccount = atm._authenticate(card.id)
    assert account.balance == 10200

    result: dict[Denomination, int] = atm.withdraw(card_number=card.id, amount=1500)
    assert isinstance(result, dict)
    assert sum(k.value * v for k, v in result.items()) == 1500
