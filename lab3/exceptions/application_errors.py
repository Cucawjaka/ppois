class ApplicationException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg: str = msg


class FactoryError(ApplicationException): ...


class BankAccountClosingError(ApplicationException): ...


class OperationError(ApplicationException): ...
