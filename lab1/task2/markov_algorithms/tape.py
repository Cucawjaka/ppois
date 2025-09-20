from markov_algorithms.formula import Formula


EMPTY_SYMBOL = '_'


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


    def do_substitution(self, substitution: Formula | None) -> None:
        if not substitution: return
        self._tape = self._tape.replace(substitution.old_value, substitution.new_value, 1)
