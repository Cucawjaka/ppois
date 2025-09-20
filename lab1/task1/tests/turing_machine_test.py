import pytest


from turing_machine.direction import Direction
from turing_machine.tape_head import EMPTY_SYMBOL, NO_WRITE_SYMBOL
from turing_machine.transition import Transition
from turing_machine.turing_machine import MAX_ITERATIONS, TuringMachine
from tests.fixtures import tm


def test_run(tm: TuringMachine):
    def mock_get_current_transition(letter: str) -> Transition:
        mock_transition = Transition("b", Direction.LEFT, "", 1)
        return mock_transition
    
    tm.state_table.get_current_transition = mock_get_current_transition
    tm.set_alphabet("ab")
    tm.load_word("aba")

    result = tm.run()

    assert result == "aba, количество итераций: 1"


def test_run_with_exception(tm: TuringMachine):
    with pytest.raises(RuntimeError):
        tm.run()
    assert tm.get_tape() == ''


@pytest.mark.parametrize(
        "direction, stop, excepted_tuple",
        [(Direction.RIGHT, 0, ("<a> -> <b> (сдвиг вправо)", False)),
         (Direction.LEFT, 0, ("<a> -> <b> (сдвиг влево)", False)),
         (Direction.NONE, 0, ("<a> -> <b> (остаемся на месте)", False)),
         (Direction.RIGHT, 1, ("<a> -> <b> (сдвиг вправо), конец программы", True))]
)
def test_step(direction: Direction,
              stop: int,
              excepted_tuple: tuple[str, bool],
              tm: TuringMachine):
    def mock_get_current_transition(letter: str) -> Transition:
        mock_transition = Transition("b", direction, "", stop)
        return mock_transition
    
    tm.state_table.get_current_transition = mock_get_current_transition

    message, is_last = tm.step()

    assert (message, is_last) == excepted_tuple


def test_step_with_exception(tm: TuringMachine):
    tm.step_counter = MAX_ITERATIONS + 1

    with pytest.raises(RuntimeError):
        tm.step()


@pytest.mark.parametrize(
        "alphabet, excepted_value",
        [("ab", "ab"), ("aaab", "ab")]
)
def test_set_alphabet(alphabet: str, excepted_value: str, tm: TuringMachine):
    tm.set_alphabet(alphabet)

    assert tm.alphabet == excepted_value


def test_validate_alphabet(tm: TuringMachine):
    try:
        tm._validate_alphabet("aaaa")
    except Exception as e:
        pytest.fail(f"Функция вернула непредвиденное исключение: {e}")


@pytest.mark.parametrize(
        "alphabet",
        ["", NO_WRITE_SYMBOL, EMPTY_SYMBOL]
)
def test_validate_alphabet_with_exceptions(alphabet: str, tm: TuringMachine):
    with pytest.raises(ValueError):
        tm._validate_alphabet(alphabet)
    

def test_validate_word(tm: TuringMachine):
    tm._alphabet = "a"
    try: 
        tm._validate_word("aaa")
    except Exception as e:
        pytest.fail(f"Функция вернула непредвиденное исключение: {e}")


def test_validate_word_with_empty_alphabet(tm: TuringMachine):
    with pytest.raises(RuntimeError):
        tm._validate_word("a")


def test_validate_word_with_wrong_letter(tm: TuringMachine):
    tm._alphabet = "a"
    with pytest.raises(ValueError):
        tm._validate_word("b")