from markov_algorithms.formula import FINAL_SUBSTITUTION_SYMBOL, Formula
from markov_algorithms.scheme import Scheme
from markov_algorithms.tape import Tape


MAX_ITERATIONS = 10000
EMPTY_SYMBOL = '_'
SIMPLE_SUBSTITUTION_SYMBOL = '->'
IS_FINAL = True


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


    def step(self) -> tuple[Formula | None, bool]:
        if self.step_counter > MAX_ITERATIONS:
            self.tape.clear()
            raise RuntimeError("Превышен лимит операций")

        self.step_counter += 1
        substitution: Formula | None = self.scheme.get_substituiting_value(self.tape.tape)

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