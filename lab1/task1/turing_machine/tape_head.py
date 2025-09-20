from turing_machine.direction import Direction


EMPTY_SYMBOL = '_'
NO_WRITE_SYMBOL = '*'


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