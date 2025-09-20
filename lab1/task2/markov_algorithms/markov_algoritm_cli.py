from markov_algorithms.formula import Formula
from markov_algorithms.markov_algorithm import EMPTY_SYMBOL, MarkovAlgorithm


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
        result_tape = result_tape.replace(EMPTY_SYMBOL, '')
        print(f"{result_tape}, количество итерация {step_counter}")


    def output_scheme(self) -> None:
        scheme: list[Formula] = self.ma.get_scheme()
        print(scheme)


    def output_tape(self) -> None:
        tape: str = self.ma.get_tape()
        tape = tape.replace(EMPTY_SYMBOL, '')
        print(tape)


    def print_step(self) -> bool:
        done_ubstitution, is_final = self.ma.step()
        print(f"Выполнена операция {done_ubstitution}")
        return is_final