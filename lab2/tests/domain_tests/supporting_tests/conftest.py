import pytest

from domain.processes.supporting.finance.budget import Budget


@pytest.fixture
def budget() -> Budget:
    return Budget(1000)
