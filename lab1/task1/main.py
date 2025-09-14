from enum import StrEnum
from dataclasses import dataclass


MAX_ITERATIONS = 10000
EMPTY_SYMBOL = '_'
NO_WRITE_SYMBOL = '*'
IS_LAST = True


class Direction(StrEnum):
    LEFT = 'L'
    RIGHT = 'R'
    NONE = 'N'


@dataclass
class Transition:
    write: str
    move: Direction
    next_state: str
    stop: int = 0


class TapeHead:
    """Считывающая/записывающая головка"""
    def __init__(self) -> None:
        self._tape: list[str] = [EMPTY_SYMBOL]
        self._position: int = 0


    def move(self, direction: Direction) -> None:
        if direction == Direction.RIGHT:
            self._position += 1
            if self._position >= len(self._tape):
                self._tape.append(EMPTY_SYMBOL)
        elif direction == Direction.LEFT:
            self._position -= 1
            if self._position < 0:
                self._tape.insert(0, EMPTY_SYMBOL)
                self._position = 0


    def write(self, value: str) -> None:
        if value != NO_WRITE_SYMBOL:
            self._tape[self._position] = value


    def read(self) -> str:
        return self._tape[self._position]
    

    def set_word(self, word: str) -> None:
        if self._tape == [EMPTY_SYMBOL]:
            self._tape += list(word) + [EMPTY_SYMBOL]
            self._position = 1
        else:
            self._tape = self._tape[:-1] + list(word) + [EMPTY_SYMBOL]


    def clear(self) -> None:
        self._tape = [EMPTY_SYMBOL]
        self._position = 0


    @property
    def tape(self) -> str:
        return ''.join(self._tape[1:-1])
    

    @property
    def position(self) -> int:
        return self._position


class StateTransitionTable:
    """Устройство управления"""
    def __init__(self) -> None:
        self._table: dict[str, dict[str, Transition]] = {}
        self._current_state: str = ""
        

    def add_state(
            self,
            transition: Transition,
            letter: str,
            state_name: str
            ) -> None:
        if state_name not in self._table:
            self._table[state_name] = {}
        self._table[state_name][letter] = transition
        if self._current_state == "": 
            self._current_state = state_name
        

    def delete_state(self, state_name: str) -> None:
        if state_name not in self._table:
            raise ValueError("Состояния с именем {state_name} не найдено")
        self._table.pop(state_name, None)


    def set_state(self, state_name: str) -> None:
        if state_name not in self._table:
            raise ValueError("Состояния с именем {state_name} не найдено")
        self._current_state = state_name


    def clear_table(self) -> None:
        self._table = {}
        self._current_state = ""


    @property
    def table(self):
        return self._table
    

    def get_current_transition(self, letter: str) -> Transition:
        if self._current_state == "":
            raise RuntimeError("Состояние не установлено")
        try:
            return self._table[self._current_state][letter] 
        except KeyError:
            raise RuntimeError(f"Нет перехода для состояния {self._current_state} и символа {letter}")
        

class TuringMachine:
    """Машина"""
    def __init__(
            self,
            tape_head: TapeHead | None = None,
            state_table: StateTransitionTable | None = None,
            ) -> None:
        self._alphabet: str = ""
        self.tape_head = tape_head if tape_head else TapeHead()
        self.state_table = state_table if state_table else StateTransitionTable()
        self.step_counter = 0


    def _do_transition(self, transition: Transition):
        self.tape_head.write(transition.write)
        self.tape_head.move(transition.move)
        self.state_table.set_state(transition.next_state)


    def run(self) -> str:
        self.step_counter = 0

        while self.step_counter < MAX_ITERATIONS:
            self.step_counter += 1
            current_letter = self.tape_head.read()
            
            transition = self.state_table.get_current_transition(current_letter)

            if transition.stop:
                result = self.tape_head.tape
                self.tape_head.clear()
                return f"{result}, количество итераций: {self.step_counter}"

            self._do_transition(transition)

        self.tape_head.clear()
        raise RuntimeError("Превышен лимит операций")


    def step(self) -> tuple[str, bool]:
        if self.step_counter > MAX_ITERATIONS:
            self.tape_head.clear()
            raise RuntimeError("Превышен лимит операций")
        
        current_letter = self.tape_head.read()

        transition = self.state_table.get_current_transition(current_letter)

        direction_map = {
            Direction.LEFT: "сдвиг влево",
            Direction.RIGHT: "сдвиг вправо",
            Direction.NONE: "остаемся на месте"}
        
        message = f"<{current_letter}> -> <{transition.write}> ({direction_map[transition.move]})"

        if transition.stop:
            message += ", конец программы"
            self.tape_head.clear()
            return message, IS_LAST  
        
        self._do_transition(transition)

        return message, not IS_LAST

        
    def set_alphabet(self, alphabet: str) -> None:
        self._validate_alphabet(alphabet)
        alphabet = ''.join(dict.fromkeys(alphabet))
        self._alphabet = alphabet


    @staticmethod
    def _validate_alphabet(alphabet: str) -> None:
        if not alphabet:
            raise ValueError("Алфавит не может быть пустым")
        if NO_WRITE_SYMBOL in alphabet:
            raise ValueError(f"Адфавит не может содержать символ '{NO_WRITE_SYMBOL}'")
        if EMPTY_SYMBOL in alphabet:
            raise ValueError(f"Адфавит не может содержать пустой символ '{EMPTY_SYMBOL}'")


    @property
    def alphabet(self) -> str:
        return self._alphabet
    

    def get_tape(self) -> str:
        return self.tape_head.tape


    def load_word(self, word: str) -> None:
        self._validate_word(word)
        self.tape_head.set_word(word)


    def load_state(self, letter: str, state_name: str, transition: Transition) -> None:
        self.state_table.add_state(transition, letter, state_name)


    def _validate_word(self, word: str) -> None:
        if not self._alphabet:
            raise RuntimeError("Алфавит еще не установлен")
        for letter in word:
            if letter not in self._alphabet:
                raise ValueError("Некорректное слово")


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