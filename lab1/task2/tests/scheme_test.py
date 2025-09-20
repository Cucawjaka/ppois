import pytest


from markov_algorithms.formula import Formula
from markov_algorithms.scheme import Scheme
from task2.tests.fixtures import scheme


def test_add_formula(scheme: Scheme):
    formula: Formula = Formula("a", "b", True)
    scheme.add_formula(formula)
    assert formula in scheme._scheme


def test_add_formula_with_exсeption(scheme: Scheme):
    formula: Formula = Formula("a", "b", False)
    with pytest.raises(ValueError):
        scheme.add_formula(formula)


def test_delete_formula(scheme: Scheme):
    formula: Formula = Formula("a", "b", False)
    scheme.delete_formula(formula)
    assert formula not in scheme._scheme


def test_clear_scheme(scheme: Scheme):
    scheme.clear_scheme()
    assert not scheme._scheme 


def test_scheme(scheme: Scheme):
    formulas: list[Formula] = [
        Formula("a", "b", False),
        Formula("_", "a", False)
        ]
    assert scheme.scheme == formulas


@pytest.mark.parametrize(
        "tape, formula",
        [("_abbc", ("a", "b", False)),
         ("_bb", ("_", "a", False)),
         ("ccc", None)]
)
def test_get_substituting_value(tape: str, formula: tuple, scheme: Scheme):
    expected_formula = Formula(*formula) if formula else None
    substitution: Formula | None = scheme.get_substituiting_value(tape)
    assert substitution == expected_formula