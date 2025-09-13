import pytest


from task2.main import (IS_FINAL, MarkovAlgorithm,
                        Scheme,
                        Tape,
                        Formula,
                        SIMPLE_SUBSTITUTION_SYMBOL,
                        FINAL_SUBSTITUTION_SYMBOL,
                        EMPTY_SYMBOL,
                        MAX_ITERATIONS)
from task2.tests.fixtures import scheme, tape, ma


@pytest.mark.parametrize(
        "formula, excepted_result, excepted_counter",
        [(("", "", True), "_aaa", 1),
         (None, "_aaa", 0)]
)
def test_run(formula: tuple | None, excepted_result: str, excepted_counter: int):
    ma: MarkovAlgorithm = MarkovAlgorithm()

    def mock_get_substituiting_value(tape: str) -> Formula | None:
        return Formula(*formula) if formula else None
    
    def mock_do_substitution(substitution: Formula | None) -> None:
        pass


    ma.tape.do_substitution = mock_do_substitution
    ma.scheme.get_substituiting_value = mock_get_substituiting_value

    ma.set_alphabet("a")
    ma.load_tape("aaa")

    result, counter = ma.run()

    assert result == excepted_result
    assert counter == excepted_counter
    assert ma.tape.tape == EMPTY_SYMBOL


def test_run_with_exception():
    ma: MarkovAlgorithm = MarkovAlgorithm()

    def mock_get_substituiting_value(tape: str) -> Formula | None:
        return Formula("", "", False)

    def mock_do_substitution(substitution: Formula | None) -> None:
        pass

    ma.tape.do_substitution = mock_do_substitution
    ma.scheme.get_substituiting_value = mock_get_substituiting_value

    with pytest.raises(RuntimeError):
        ma.run()
    assert ma.get_tape() == EMPTY_SYMBOL


@pytest.mark.parametrize(
        "formula, expected_value",
        [(("a", "b", False), not IS_FINAL),
         (("a", "b", True), IS_FINAL),
         (None, IS_FINAL)]
)
def test_step(formula: tuple | None, expected_value: bool, ma: MarkovAlgorithm):
    def mock_get_substituiting_value(tape: str) -> Formula | None:
        return Formula(*formula) if formula else None
    
    def mock_do_substitution(substitution: Formula | None) -> None:
        pass

    ma.tape.do_substitution = mock_do_substitution
    ma.scheme.get_substituiting_value = mock_get_substituiting_value

    old_counter = ma.step_counter
    _, is_final = ma.step()

    assert ma.step_counter == old_counter + 1
    assert is_final == expected_value


def test_step_with_exception(ma: MarkovAlgorithm):
    ma.step_counter = MAX_ITERATIONS + 1
    with pytest.raises(RuntimeError):
        ma.step()


def test_validate_alphabet():
    try:
        MarkovAlgorithm._validate_alphabet("abc")
    except ValueError:
        pytest.fail()


@pytest.mark.parametrize(
        "alphabet",
        ["",
         SIMPLE_SUBSTITUTION_SYMBOL,
         FINAL_SUBSTITUTION_SYMBOL,
         EMPTY_SYMBOL]
)
def test_validate_alphabet_with_exception(alphabet: str):
    with pytest.raises(ValueError):
        MarkovAlgorithm._validate_alphabet(alphabet)


@pytest.mark.parametrize(
        "alphabet, tape, expected_exception",
        [("", "", RuntimeError),
         ("a", "b", ValueError)]
)
def test_validate_tape(
    alphabet: str,
    tape: str,
    expected_exception: type[Exception]):
        ma: MarkovAlgorithm = MarkovAlgorithm()
        ma._alphabet = alphabet
        with pytest.raises(expected_exception):
            ma._validate_tape(tape)
