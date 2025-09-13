import pytest


from task2.main import Formula


@pytest.mark.parametrize(
        "data, formula",
        [("a -> b", ("a", "b", False)),
         ("a => b", ("a", "b", True))]
)
def test_from_string(data: str, formula: tuple):
    expected_result: Formula = Formula(*formula)
    assert expected_result == Formula.from_string(data)


@pytest.mark.parametrize(
    "compared, comparing, result",
    [(("a", "b", False), ("b", "a", False), False),
     (("a", "b", False), ("a", "b", False), True)]
)
def test__eq__(compared: tuple, comparing: tuple, result: bool):
    assert (Formula(*compared) == Formula(*comparing)) == result


@pytest.mark.parametrize(
        "formula, expected_str",
        [(("a", "b", False), "a -> b"),
         (("a", "b", True), "a => b")]
)
def test__str__(formula: tuple, expected_str: str):
    class_formula = Formula(*formula)
    assert str(class_formula) == expected_str