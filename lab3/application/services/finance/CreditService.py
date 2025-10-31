from datetime import datetime
from application.services.clients.NotificationService import NotificationService
from core.enums.CreditType import CreditType
from domain.finance.Credit import Credit
from domain.finance.CreditSchedule import CreditSchedule
from domain.interfaces.BankAccount import BankAccount
from domain.transactions.Transaction import Transaction
from infrastructure.repositories.CreditRepository import CreditRepository


class CreditService:
    def __init__(
        self, notification_service: NotificationService, credits_repo: CreditRepository
    ):
        self._credits_repo = credits_repo
        self._notification_service = notification_service

    def open_credit(
        self,
        customer_id: str,
        total_amount: int,
        annual_rate: int,
        months_length: int,
        start_date: datetime,
        payment_account: BankAccount,
        type_: CreditType,
    ) -> Credit:
        credit = Credit(
            customer_id,
            total_amount,
            annual_rate,
            months_length,
            start_date,
            type_,
        )

        schedule = CreditSchedule.generate(
            total_amount,
            annual_rate,
            months_length,
            start_date,
            payment_account,
        )

        credit.set_payments(schedule)
        self._credits_repo.create(credit)

        self._notification_service.send_email(
            customer_id,
            f"Кредит оформлен на сумму {total_amount} под {annual_rate}% сроком на {months_length} мес.",
        )

        return credit

    def pay_credit_payment(
        self, credit_id: str, payment_number: int, from_account: BankAccount
    ) -> Transaction:
        credit = self._credits_repo.read(credit_id)

        payment = credit._payments[payment_number]

        transaction = payment.create_pay_transaction(from_account)
        payment.set_paid()

        return transaction

    def close_credit(self, credit_id: str):
        credit = self._credits_repo.read(credit_id)
        credit.mark_as_closed()
        self._notification_service.send_email(
            credit._customer_id, "Кредит успешно закрыт"
        )
