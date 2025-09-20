import sys, json

from markov_algorithms.formula import Formula
from markov_algorithms.markov_algorithm import MarkovAlgorithm
from markov_algorithms.markov_algoritm_cli import MarkovAlgorithmCLI


def load_from_file(path: str) -> MarkovAlgorithm:
    with open(path, "r", encoding="utf-8") as file:
        data: dict = json.load(file)

    ma = MarkovAlgorithm()
    ma.set_alphabet(data["alphabet"])
    ma.load_tape(data["tape"])

    for string_formula in data["formulas"]:
        formula: Formula = Formula.from_string(string_formula)
        ma.load_formula(formula)

    return ma


if __name__ == "__main__": #pragma: no cover
    if len(sys.argv) < 2:
        print("Использование: python3 -m script <path> [-log]")
        sys.exit(1)

    path = sys.argv[1]
    log = "-log" in sys.argv
    ma = load_from_file(path)
    cli = MarkovAlgorithmCLI(ma)

    if log:
        print("Нажмите 'n' для следующего шага, 'q' - для выхода\n\n")
        while True:
            done: bool = False
            user_input: str = input()
            if user_input == 'n':
                done = cli.print_step()
                cli.output_tape()
        
            if done:
                print("Программа завершена")
                ma.tape.clear()
            if user_input == 'q':
                print("Завершение программы")
                break

    else:
        cli.output_result()