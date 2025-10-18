import pytest

from task2.ConstContainer import ConstContainer


def test__next__and_prev(crbi) -> None:
    assert isinstance(crbi.__next__(), ConstContainer)

    crbi.__next__()

    assert isinstance(crbi.prev(), ConstContainer)


def test_prev_with_stop(crbi) -> None:
    with pytest.raises(StopIteration):
        crbi.prev()


def test__next__with_stop(crbi) -> None:
    crbi.__next__()
    crbi.__next__()
    with pytest.raises(StopIteration):
        crbi.__next__()
