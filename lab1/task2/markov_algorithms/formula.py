from dataclasses import dataclass
from typing import Self


FINAL_SUBSTITUTION_SYMBOL = '=>'


@dataclass
class Formula:
    old_value: str
    new_value: str
    is_final: bool

    @classmethod
    def from_string(cls, data: str) -> Self:
        list_data: list = data.split()
        
        return cls(
            old_value = list_data[0],
            new_value = list_data[2],
            is_final = list_data[1] == FINAL_SUBSTITUTION_SYMBOL
        )


    def __eq__(self, value: Self) -> bool:
        return (self.old_value, self.new_value, self.is_final) == \
            (value.old_value, value.new_value, value.is_final)
    

    def __str__(self) -> str:
        pointer: str = "=>" if self.is_final else "->"
        return f"{self.old_value} {pointer} {self.new_value}" 