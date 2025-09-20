import pytest

from markov_algorithms.formula import Formula
from markov_algorithms.markov_algorithm import MarkovAlgorithm
from markov_algorithms.scheme import Scheme
from markov_algorithms.tape import Tape


@pytest.fixture(scope="function")
def ma(scheme: Scheme, tape: Tape) -> MarkovAlgorithm:
    ma: MarkovAlgorithm = MarkovAlgorithm(tape, scheme)
    return ma


@pytest.fixture(scope="function")
def scheme() -> Scheme:
    formulas: list[Formula] = [
        Formula("a", "b", False),
        Formula("_", "a", False)
        ]
    new_scheme: Scheme = Scheme()
    new_scheme._scheme = formulas
    return new_scheme


@pytest.fixture(scope="function")
def tape() -> Tape:
    new_tape: Tape = Tape()
    new_tape._tape = "_abc"
    return new_tape