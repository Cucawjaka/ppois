class DomainException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg: str = msg


class NotFoundError(DomainException): ...


class FrozenAccountError(DomainException): ...


class NotEnoughMoneyError(DomainException): ...


class DepositException(DomainException): ...


class TransactionError(DomainException): ...


class WrongPasswordError(DomainException): ...


class ATMError(DomainException): ...


class TerminalError(DomainException): ...
