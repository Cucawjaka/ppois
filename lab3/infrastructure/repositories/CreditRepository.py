from domain.finance.Credit import Credit
from exceptions.infrastructure_errors import RepositoryError


class CreditRepository:
    credits: dict[str, Credit] = {}

    def create(self, item: Credit) -> None:
        self.credits[item.id] = item

    def read(self, key: str) -> Credit:
        if credit := self.credits.get(key, None):
            return credit
        raise RepositoryError("Кредит не найден")

    def delete(self, key: str) -> None:
        del self.credits[key]
