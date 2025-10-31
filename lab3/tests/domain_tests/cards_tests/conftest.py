import pytest
from datetime import datetime

from core.enums.Currency import Currency
from core.enums.CardType import CardType
from core.enums.Denomination import Denomination
from domain.accounts.CurrentAccount import CurrentAccount
from domain.cards.ATM import ATM
from domain.cards.ExpireDate import ExpireDate
from domain.cards.Card import Card
from domain.cards.Terminal import Terminal
from domain.interfaces.BankAccount import BankAccount
from infrastructure.repositories.AccountRepository import AccountRepository
from infrastructure.repositories.CardRepository import CardRepository


@pytest.fixture
def account() -> BankAccount:
    account: BankAccount = CurrentAccount(
        owner_id="test1", account_number="test1", currency=Currency.BYN
    )
    account.deposit(10000)
    return account


@pytest.fixture
def second_account() -> BankAccount:
    account: BankAccount = CurrentAccount(
        owner_id="test2", account_number="test2", currency=Currency.BYN
    )
    account.deposit(5000)
    return account


@pytest.fixture
def expire_date() -> ExpireDate:
    return ExpireDate(datetime.now().month, datetime.now().year + 3)


@pytest.fixture
def card(expire_date, account) -> Card:
    card = Card(
        expiry=expire_date,
        pin=1234,
        owner_id=account.owner_id,
        account_number=account.account_number,
        type_=CardType.DEBIT,
    )
    card.activate()
    return card


@pytest.fixture
def cargs_repo(card: Card) -> CardRepository:
    cards_repo: CardRepository = CardRepository()
    cards_repo.create(card)

    return cards_repo


@pytest.fixture
def accounts_repo(account: BankAccount) -> AccountRepository:
    account_repo: AccountRepository = AccountRepository()
    account_repo.create(account)

    return account_repo


@pytest.fixture
def atm(cargs_repo: CardRepository, accounts_repo: AccountRepository) -> ATM:
    atm = ATM(
        location="test",
        cards_repo=cargs_repo,
        accounts_repo=accounts_repo,
        withdrow_limit=50000,
    )

    atm._cash[Denomination.FIFTY] = 10
    atm._cash[Denomination.HUNDRED] = 20
    return atm


@pytest.fixture
def terminal(second_account: BankAccount) -> Terminal:
    return Terminal(owner_account=second_account)
