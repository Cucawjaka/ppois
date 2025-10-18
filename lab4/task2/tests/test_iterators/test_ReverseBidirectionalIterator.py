import pytest


def test__next__and_prev(rbi, test_class_2) -> None:
    assert rbi.__next__() == test_class_2

    rbi.__next__()

    assert rbi.prev() == test_class_2


def test_prev_with_stop(rbi) -> None:
    with pytest.raises(StopIteration):
        rbi.prev()


def test__next__with_stop(rbi) -> None:
    rbi.__next__()
    rbi.__next__()
    with pytest.raises(StopIteration):
        rbi.__next__()
