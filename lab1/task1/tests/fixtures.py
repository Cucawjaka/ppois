import pytest

from turing_machine.direction import Direction
from turing_machine.state_transition_table import StateTransitionTable
from turing_machine.tape_head import TapeHead
from turing_machine.transition import Transition
from turing_machine.turing_machine import TuringMachine


@pytest.fixture(scope="function")
def state_table() -> StateTransitionTable:
    state = StateTransitionTable()
    return state


@pytest.fixture
def transition() -> Transition:
    transition = Transition(
        write="a",
        move=Direction.LEFT,
        next_state="q0")
    return transition


@pytest.fixture(scope="function")
def state_table_with_transition(state_table: StateTransitionTable, transition: Transition):
    state_table.add_state(transition, "b", "q0")
    return state_table


@pytest.fixture(scope="function")
def tape_head() -> TapeHead:
    new_tape = TapeHead()
    return TapeHead()


def mock_wirte(value: str) -> None:
    pass

def mock_move(direction: Direction) -> None:
    pass

def mock_set_state(state_name: str) -> None:
    pass

def mock_read() -> str:
    return "a"


@pytest.fixture(scope="function")
def tm() -> TuringMachine:
    tm = TuringMachine()

    tm.tape_head.write = mock_wirte
    tm.tape_head.move = mock_move
    tm.state_table.set_state = mock_set_state
    tm.tape_head.read = mock_read

    return tm