from domain.transactions.Transaction import Transaction
from exceptions.infrastructure_errors import RepositoryError


class TransactionRepository:
    transactions: dict[str, Transaction] = {}

    def create(self, item: Transaction) -> None:
        self.transactions[item.id] = item

    def read(self, key: str) -> Transaction:
        if transaction := self.transactions.get(key, None):
            return transaction
        raise RepositoryError("Транзакция не найдена")

    def delete(self, key: str) -> None:
        del self.transactions[key]
