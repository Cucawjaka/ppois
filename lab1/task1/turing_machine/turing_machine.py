from turing_machine.direction import Direction
from turing_machine.state_transition_table import StateTransitionTable
from turing_machine.tape_head import EMPTY_SYMBOL, NO_WRITE_SYMBOL, TapeHead
from turing_machine.transition import Transition


MAX_ITERATIONS = 10000
IS_LAST = True


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