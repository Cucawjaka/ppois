import pytest

from task1.main import Direction, StateTransitionTable, TapeHead, Transition, TuringMachine


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