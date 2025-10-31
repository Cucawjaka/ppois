class InfrastructureException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg: str = msg


class RepositoryError(InfrastructureException): ...
