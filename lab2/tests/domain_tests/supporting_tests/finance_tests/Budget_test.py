import pytest
from core.exceptions import BudgetLimitExceededError
from domain.processes.supporting.finance.Budget import Budget


def test_allocate(budget: Budget) -> None:
    budget.allocate(100)

    assert budget.amount_allocated == 1100


def test_spend(budget: Budget) -> None:
    budget.spend(100)

    assert budget._amount_spend == 100


def test_spend_with_error(budget: Budget) -> None:
    with pytest.raises(BudgetLimitExceededError):
        budget.spend(1100)


def test_close(budget: Budget) -> None:
    budget.close()

    assert budget.status == "closed"


def test_amount_allocated(budget: Budget) -> None:
    assert budget.amount_allocated == 1000


def test_status(budget: Budget) -> None:
    assert budget.status == "active"


def test_get_report(budget: Budget) -> None:
    budget.spend(100)

    assert (
        budget.get_report()
        == "Отчет:\n Выделено: 1000\nПотрачено: 100\n Остаток: 900\n"
    )


def test_allocate_subbudget(budget: Budget) -> None:
    subbudget: Budget = budget.allocate_subbudget(100)

    assert subbudget.amount_allocated == 100
    assert budget._amount_spend == 100
