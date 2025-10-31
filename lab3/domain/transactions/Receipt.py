from dataclasses import dataclass
import datetime

from core.enums.Currency import Currency
from core.enums.TransactionType import TransactionType
from domain.interfaces.BankAccount import BankAccount


@dataclass(frozen=True)
class Receipt:
    amount: int
    currency: Currency
    from_account: BankAccount
    to_account: BankAccount
    data: datetime.datetime
    type: TransactionType
    descrpition: str

    def __str__(self) -> str:
        return (
            f"Сумма {self.amount}{self.currency}\n"
            f"Отправитель {self.from_account.account_number}, получатель {self.to_account.account_number}\n"
            f"Тип транзакции {self.type}\n"
            f"Дополнительные сведения {self.descrpition}\n"
            f"Дата {self.data}"
        )
