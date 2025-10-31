from application.interfaces.IRepository import IRepository
from core.utils.IDGenerator import IDGenerator
from domain.clients.Customer import Customer
from domain.clients.UserInfo import UserInfo


class RegistrationService:
    def __init__(self, customer_repo: IRepository) -> None:
        self._customer_repo: IRepository = customer_repo

    def registrate(
        self, phone_number: int, email: str, pasport_number: str, age: int
    ) -> Customer:
        user_info = UserInfo(phone_number, email, pasport_number, age)
        new_customer = Customer(IDGenerator.create_uuid(), user_info)
        self._customer_repo.create(new_customer)

        return new_customer
