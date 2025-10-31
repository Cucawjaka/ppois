from datetime import datetime, timedelta

from domain.finance.CreditPayment import CreditPayment
from domain.interfaces.BankAccount import BankAccount


class CreditSchedule:
    @staticmethod
    def generate(
        total_amount: int,
        rate: int,
        months: int,
        start_date: datetime,
        payment_account: BankAccount,
    ):
        monthly_rate: int = int(rate / 12 / 100)
        payment = total_amount * monthly_rate / (1 - (1 + monthly_rate) ** -months)
        payments: list[CreditPayment] = []

        for i in range(months):
            payment_date: datetime = start_date + timedelta(days=30 * (i + 1))
            interest_part = total_amount * monthly_rate
            payments.append(
                CreditPayment(payment_date, payment, interest_part, payment_account)
            )
            total_amount -= total_amount - interest_part

        return payments
