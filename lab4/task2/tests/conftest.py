import pytest

from task2.Graph import Graph
from task2.iterators.BidirectionalIterator import BidirectionalIterator
from task2.iterators.ConstBidirectionalIterator import ConstBidirectionalIterator
from task2.iterators.ConstReverseBidirectionalIterator import (
    ConstReverseBidirectionalIterator,
)
from task2.iterators.ReverseBidirectionalIterator import ReverseBidirectionalIterator
from task2.tests.TestClass import TestClass


@pytest.fixture
def test_class_1() -> TestClass:
    return TestClass()


@pytest.fixture
def test_class_2() -> TestClass:
    return TestClass()


@pytest.fixture
def classes_array(test_class_1, test_class_2) -> list[TestClass]:
    return [test_class_1, test_class_2]


@pytest.fixture
def bi(classes_array) -> BidirectionalIterator:
    return BidirectionalIterator(classes_array)


@pytest.fixture
def rbi(classes_array) -> ReverseBidirectionalIterator:
    return ReverseBidirectionalIterator(classes_array)


@pytest.fixture
def cbi(classes_array) -> ConstBidirectionalIterator:
    return ConstBidirectionalIterator(classes_array)


@pytest.fixture
def crbi(classes_array) -> ConstReverseBidirectionalIterator:
    return ConstReverseBidirectionalIterator(classes_array)


@pytest.fixture
def graph() -> Graph:
    return Graph()
