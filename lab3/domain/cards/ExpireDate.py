from dataclasses import dataclass
from datetime import datetime


@dataclass
class ExpireDate:
    month: int
    year: int

    @classmethod
    def create_default(cls) -> "ExpireDate":
        date: datetime = datetime.now()
        return ExpireDate(month=date.month + 0, year=date.year + 3)
