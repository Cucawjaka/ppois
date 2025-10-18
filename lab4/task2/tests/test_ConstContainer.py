import pytest

from task2.ConstContainer import ConstContainer
from task2.errors.ConstContainerError import ConstContainerError


def test__getattribute__(test_class_1) -> None:
    container = ConstContainer(test_class_1)

    assert container.x == 1


def test__getattribute___with_error(test_class_1) -> None:
    container = ConstContainer(test_class_1)
    with pytest.raises(ConstContainerError):
        container._containered


def test__setattr__(test_class_1) -> None:
    container = ConstContainer(test_class_1)
    with pytest.raises(ConstContainerError):
        container.x = 2
