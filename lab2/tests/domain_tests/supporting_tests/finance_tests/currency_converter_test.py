from core.enums.currency import Currency
from domain.processes.supporting.finance.currency_converter import CurrencyConverter


def test_conevert(converter: CurrencyConverter) -> None:
    new_amount: int = converter.convert(100, Currency.EURO, Currency.DOLLAR)

    assert new_amount == 125
