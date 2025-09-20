from turing_machine.direction import Direction
from turing_machine.transition import Transition
from turing_machine.turing_machine import TuringMachine


class TuringMachineCLI:
    def __init__(self, machine: TuringMachine) -> None:
        self.machine = machine
        

    def input_word(self) -> None:
        word = input("Введитие слово: ")
        self.machine.load_word(word)


    def input_alphabet(self) -> None:
        alphabet = input("Введите алфавит: ")
        self.machine.set_alphabet(alphabet)
    

    def input_state(self) -> None: 
        state_name = input("Введите название состояния: ")
        for letter in self.machine.alphabet:
            raw = input(f"Введите переход (символ, L/R/N, след. состояние, stop=1/0) \
                        для состояния {state_name} и символа {letter}: ")
            parts = raw.split()
            if len(parts) < 4:
                raise ValueError("Неверный формат перехода")
            write, move, next_state, stop_flag = parts
            transition = Transition(write=write, move=Direction(move), next_state=next_state, stop=int(stop_flag))
            self.machine.load_state(state_name, letter, transition)


    def output_result(self) -> None:
        print(self.machine.run())


    def output_state_table(self):
        print(self.machine.state_table.table)


    def print_step(self) -> bool:
        message, done = self.machine.step()
        print(message)
        return done
    

    def output_tape(self) -> None:
        tape = self.machine.get_tape()
        print(tape)