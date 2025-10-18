import pytest


def test__next__and_prev(bi, test_class_1, test_class_2) -> None:
    assert bi.__next__() == test_class_1

    bi.__next__()

    assert bi.prev() == test_class_1


def test_prev_with_stop(bi) -> None:
    with pytest.raises(StopIteration):
        bi.prev()


def test__next__with_stop(bi) -> None:
    bi.__next__()
    bi.__next__()
    with pytest.raises(StopIteration):
        bi.__next__()
