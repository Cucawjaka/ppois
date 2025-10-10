import pytest
from core.exceptions import FrozenAccountError, NotEnoughMoneyError
from domain.processes.supporting.finance.bank_account import BankAccount


def test_withdrow_with_money_error(from_account: BankAccount) -> None:
    with pytest.raises(NotEnoughMoneyError):
        from_account.withdraw(300)


def test_operation_with_freeze_error(from_account: BankAccount) -> None:
    from_account.freeze()

    assert from_account._is_freeze

    with pytest.raises(FrozenAccountError):
        from_account.withdraw(100)

    with pytest.raises(FrozenAccountError):
        from_account.deposit(100)
