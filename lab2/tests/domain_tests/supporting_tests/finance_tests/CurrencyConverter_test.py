from core.enums.Currency import Currency
from domain.processes.supporting.finance.CurrencyConverter import CurrencyConverter


def test_conevert(converter: CurrencyConverter) -> None:
    new_amount: int = converter.convert(100, Currency.EURO, Currency.DOLLAR)

    assert new_amount == 125
