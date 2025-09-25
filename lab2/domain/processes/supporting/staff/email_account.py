from core.exceptions import NotFoundEmailError


class EmailAccount:
    def __init__(self, email_addres: str) -> None:
        self._letters: list[str] = list()
        self._addres: str = email_addres


    def read_letter(self) -> str:
        if self._letters:
            letter = self._letters.pop(0)
            return letter
        else: raise NotFoundEmailError("Непрочитанных писем нету")


    def send_letter(self, letter: str, recipient: "EmailAccount") -> None:
        recipient.get_letter(letter)


    def get_letter(self, letter: str) -> None:
        self._letters.append(letter)

