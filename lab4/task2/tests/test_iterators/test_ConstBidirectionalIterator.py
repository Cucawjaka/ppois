import pytest

from task2.ConstContainer import ConstContainer


def test__next__and_prev(cbi) -> None:
    assert isinstance(cbi.__next__(), ConstContainer)

    cbi.__next__()

    assert isinstance(cbi.prev(), ConstContainer)


def test_prev_with_stop(cbi) -> None:
    with pytest.raises(StopIteration):
        cbi.prev()


def test__next__with_stop(cbi) -> None:
    cbi.__next__()
    cbi.__next__()
    with pytest.raises(StopIteration):
        cbi.__next__()
