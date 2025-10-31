from domain.clients.Customer import Customer
from exceptions.infrastructure_errors import RepositoryError


class CustomerRepository:
    customers: dict[str, Customer] = {}

    def create(self, item: Customer) -> None:
        self.customers[item.id] = item

    def read(self, key: str) -> Customer:
        if customer := self.customers.get(key, None):
            return customer
        raise RepositoryError("Клиент не найден")

    def delete(self, key: str) -> None:
        del self.customers[key]
