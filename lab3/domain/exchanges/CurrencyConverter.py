from core.enums.Currency import Currency
from domain.exchanges.ExchangeRequest import ExchangeRequest
from exceptions.utils_errors import ConverterError


class CurrencyConverter:
    def __init__(self) -> None:
        self._rates: dict[tuple[Currency, Currency], float] = {
            (Currency.EURO, Currency.DOLLAR): 1.25,
            (Currency.DOLLAR, Currency.EURO): 0.8,
            (Currency.EURO, Currency.BYN): 3.46,
            (Currency.BYN, Currency.EURO): 0.28,
            (Currency.DOLLAR, Currency.BYN): 3.25,
            (Currency.BYN, Currency.DOLLAR): 0.3,
        }

    def convert(
        self, amount: int, from_currency: Currency, to_currency: Currency
    ) -> int:
        if from_currency == to_currency:
            return amount
        try:
            rate = self._rates[(from_currency, to_currency)]
            return int(amount * rate)
        except KeyError:
            raise ConverterError(f"Нет курса для {from_currency} -> {to_currency}")

    def set_customer_rate(self, offer: ExchangeRequest) -> None:
        self._rates[(offer.from_currency, offer.to_currency)] = offer.rate
