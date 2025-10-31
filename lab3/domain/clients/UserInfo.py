from dataclasses import dataclass


@dataclass
class UserInfo:
    _phone_number: int
    _email: str
    _pasport_number: str
    _age: int

    def update_email(self, new_email: str) -> None:
        self._email = new_email

    def update_phone_number(self, new_number: int) -> None:
        self._phone_number = new_number
