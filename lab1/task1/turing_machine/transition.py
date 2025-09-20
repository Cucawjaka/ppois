from dataclasses import dataclass
from turing_machine.direction import Direction


@dataclass
class Transition:
    write: str
    move: Direction
    next_state: str
    stop: int = 0