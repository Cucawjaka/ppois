from enum import StrEnum, auto

from core.exceptions import ConverterError


class Currency(StrEnum):
    EURO = auto()
    DOLLAR = auto()
    BYN = auto()


class CurrencyConverter():
    def __init__(self) -> None:
        self._rates: dict[tuple[str, str], float] = {
            ("euro", "dollar"): 1.25,
            ("dollar", "euro"): 0.8,
            ("euro", "byn"): 3.46,
            ("byn", "euro"): 0.28,
            ("dollar", "byn"): 3.25,
            ("byn", "dollar"): 0.3
        }  


    def convert(self, amount: int, from_currency: Currency, to_currency: Currency) -> int:
        if from_currency == to_currency: return amount
        try:
            rate = self._rates[(from_currency, to_currency)]
            return int(amount*rate)
        except KeyError:
            raise ConverterError(f"Нет курса для {from_currency} -> {to_currency}")
    
