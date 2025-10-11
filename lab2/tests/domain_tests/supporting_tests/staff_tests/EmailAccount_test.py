import pytest
from core.exceptions import NotFoundError
from domain.processes.supporting.staff.EmailAccount import EmailAccount


def test_get_letter(email_account: EmailAccount) -> None:
    email_account.get_letter("some words")

    assert email_account._letters[0] == "some words"


def test_read_letter(email_account: EmailAccount) -> None:
    email_account.get_letter("some words")

    letter: str = email_account.read_letter()

    assert letter == "some words"


def test_read_letter_with_error(email_account: EmailAccount) -> None:
    with pytest.raises(NotFoundError):
        email_account.read_letter()


def test_send_letter(email_account: EmailAccount) -> None:
    recipient: EmailAccount = EmailAccount("friend@mail.ru")

    email_account.send_letter("Hi", recipient)

    assert recipient.read_letter() == "Hi"
