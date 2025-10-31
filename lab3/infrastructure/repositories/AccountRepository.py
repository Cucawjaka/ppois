from domain.interfaces.BankAccount import BankAccount
from exceptions.infrastructure_errors import RepositoryError


class AccountRepository:
    accounts: dict[str, BankAccount] = {}

    def create(self, item: BankAccount) -> None:
        self.accounts[item.account_number] = item

    def read(self, key: str) -> BankAccount:
        if account := self.accounts.get(key, None):
            return account
        raise RepositoryError("Счет не найден")

    def delete(self, key: str) -> None:
        del self.accounts[key]
