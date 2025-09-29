from typing import Literal

from core.exceptions import BudgetLimitExceededError


class Budget:
    def __init__(self,
                 amount_allocated: int) -> None:
        self._amount_allocated: int = amount_allocated
        self._amount_spend: int = 0
        self._status: Literal["active", "closed", "over_limit"] = "active"


    def allocate(self, money_amount: int) -> None:
        self._amount_allocated += money_amount


    def spend(self, money_amount: int) -> None:
        self._amount_spend += money_amount
        if self._is_over_limit:
            self._status = "over_limit"
            raise BudgetLimitExceededError("Превышен лимит бюджета!")


    def close(self) -> None:
        self._status = "closed"


    @property
    def status(self) -> Literal["active", "closed", "over_limit"]:
        return self.status


    def _is_over_limit(self) -> bool:
        return self._amount_spend > self._amount_allocated


    def get_report(self) -> str:
        rest: int = self._amount_allocated - self._amount_spend
        return (f"Отчет:\n Выделено: {self._amount_allocated}\n" 
                f"Потрачено: {self._amount_spend}\n Остаток: {rest}\n"
        )
