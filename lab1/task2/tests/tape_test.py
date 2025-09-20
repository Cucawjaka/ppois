import pytest



from markov_algorithms.formula import Formula
from markov_algorithms.tape import Tape
from task2.tests.fixtures import tape
    

def test_clear(tape: Tape):
    tape.clear()
    assert tape.tape == "_"


def test_tape(tape: Tape):
    assert tape.tape == "_abc"


def test_set_tape(tape: Tape):
    tape.set_tape("aabbcc")
    assert tape.tape == "_aabbcc"


@pytest.mark.parametrize(
        "formula, checked_value",
        [(("a", "b", False), "_bbc"),
         (("_", "a", False), "aabc"),
         (None, "_abc")]
)
def test_do_substitution(formula: tuple, checked_value: str, tape: Tape):
    class_formula = Formula(*formula) if formula else None
    tape.do_substitution(class_formula)
    assert tape.tape == checked_value