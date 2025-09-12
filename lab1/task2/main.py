from dataclasses import dataclass
from typing import Self


MAX_ITERATIONS = 10000
EMPTY_SYMBOL = '_'
SIMPLE_SUBSTITUTION_SYMBOL = '->'
FINAL_SUBSTITUTION_SYMBOL = '=>'
IS_FINAL = True


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
    

@dataclass
class Substitution:
    index: int
    formula: Formula

    @property
    def old_value(self) -> str:
        return self.formula.old_value
    
    @property
    def new_value(self)-> str:
        return self.formula.new_value
    
    @property
    def is_final(self) -> bool:
        return self.formula.is_final
    

    def __str__(self) -> str: 
        return str(self.formula)


class Scheme:
    def __init__(self) -> None:
        self._scheme: list[Formula] = list()


    def add_formula(self, formula: Formula) -> None:
        if formula in self._scheme:
            raise ValueError("Формула уже существует")
        self._scheme.append(formula)


    def delete_formula(self, formula_to_delete: Formula) -> None:
        self._scheme.remove(formula_to_delete)


    def clear_scheme(self) -> None:
        self._scheme = list()


    @property
    def scheme(self) -> list[Formula]:
        return self._scheme
    

    def get_substituiting_value(self, tape: str) -> Substitution | None:
        for formula in self._scheme:
            index = tape.find(formula.old_value)
            if index != -1:
                return Substitution(index, formula)
        return None


class Tape:
    def __init__(self) -> None:
        self._tape: str = EMPTY_SYMBOL


    def clear(self) -> None:
        self._tape = EMPTY_SYMBOL


    @property
    def tape(self) -> str:
        return self._tape


    def set_tape(self, tape: str) -> None:
        self._tape = EMPTY_SYMBOL + tape


    def do_substitution(self, substitution: Substitution | None) -> None:
        if not substitution: return
        self._tape = self._tape.replace(substitution.old_value, substitution.new_value, 1)


class MarkovAlgorithm:
    def __init__(
            self,
            tape: Tape | None = None,
            scheme: Scheme | None = None) -> None:
        self._alphabet: str = ""
        self.tape: Tape = tape if tape else Tape()
        self.scheme: Scheme = scheme if scheme else Scheme()
        self.step_counter: int = 0

    
    def _finish(self, result: str, iterations: int) -> tuple[str, int]:
        self.tape.clear()
        return result, iterations


    def run(self) -> tuple[str, int]:
        self.step_counter = 0

        while self.step_counter < MAX_ITERATIONS:
            self.step_counter += 1
            substitution = self.scheme.get_substituiting_value(self.tape.tape)
            
            self.tape.do_substitution(substitution)

            if not substitution:
                return self._finish(self.tape.tape, self.step_counter-1)
            if substitution.is_final:
                return self._finish(self.tape.tape, self.step_counter)

        self.tape.clear()
        raise RuntimeError("Превышен лимит операций")


    def step(self) -> tuple[Substitution | None, bool]:
        if self.step_counter > MAX_ITERATIONS:
            self.tape.clear()
            raise RuntimeError("Превышен лимит операций")

        self.step_counter += 1
        substitution: Substitution | None = self.scheme.get_substituiting_value(self.tape.tape)

        self.tape.do_substitution(substitution)

        if not substitution:
            return None, IS_FINAL
        if substitution.is_final:
            return substitution, IS_FINAL
        
        return substitution, not IS_FINAL




    def set_alphabet(self, alphabet: str) -> None:
        self._validate_alphabet(alphabet)
        self._alphabet = alphabet


    @staticmethod
    def _validate_alphabet(alphabet: str) -> None:
        if not alphabet:
            raise ValueError("Алфавит не может быть пустым")
        if SIMPLE_SUBSTITUTION_SYMBOL in alphabet:
            raise ValueError(f"Адфавит не может содержать символ простого перехода '{SIMPLE_SUBSTITUTION_SYMBOL}'")
        if FINAL_SUBSTITUTION_SYMBOL in alphabet:
            raise ValueError(f"Адфавит не может содержать символ финального перехода'{FINAL_SUBSTITUTION_SYMBOL}'")
        if EMPTY_SYMBOL in alphabet:
            raise ValueError(f"Адфавит не может содержать пустой символ '{EMPTY_SYMBOL}'")
        

    @property
    def alphabet(self) -> str:
        return self._alphabet
    

    def get_tape(self) -> str:
        return self.tape.tape
    

    def get_scheme(self) -> list[Formula]:
        return self.scheme.scheme


    def load_tape(self, tape: str) -> None: 
        self._validate_tape(tape)
        self.tape.set_tape(tape)


    def load_formula(self, formula: Formula) -> None:
        self.scheme.add_formula(formula)


    def _validate_tape(self, tape: str) -> None:
        if not self._alphabet:
            raise RuntimeError("Алфавит еще не установлен")
        for letter in tape:
            if letter not in self._alphabet:
                raise ValueError("Некорректное слово")


class MarkovAlgorithmCLI:
    def __init__(self, ma: MarkovAlgorithm) -> None:
        self.ma = ma

    def input_alphabet(self) -> None:
        alphabet = input("Введите алфавит: ")
        self.ma.set_alphabet(alphabet)

    def input_tape(self) -> None:
        word = input("Введитие ленту: ")
        self.ma.load_tape(word)


    def input_formula(self) -> None:
        input_value: str = input("Введите формулу: ")
        formula = Formula.from_string(input_value)

        self.ma.load_formula(formula)


    def output_result(self) -> None:
        result_tape, step_counter = self.ma.run()
        print(f"{result_tape}, количество итерация {step_counter}")


    def output_scheme(self) -> None:
        scheme: list[Formula] = self.ma.get_scheme()
        print(scheme)


    def output_tape(self) -> None:
        tape: str = self.ma.get_tape()
        tape = tape.replace('_', '')
        print(tape)


    def print_step(self) -> bool:
        done_ubstitution, is_final = self.ma.step()
        print(f"Выполнена операция {done_ubstitution}")
        return is_final