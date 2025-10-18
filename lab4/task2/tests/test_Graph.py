from task2.ConstContainer import ConstContainer
from task2.iterators.BidirectionalIterator import BidirectionalIterator
from task2.iterators.ConstBidirectionalIterator import ConstBidirectionalIterator
from task2.iterators.ConstReverseBidirectionalIterator import (
    ConstReverseBidirectionalIterator,
)
from task2.iterators.ReverseBidirectionalIterator import ReverseBidirectionalIterator


def test_clear(graph, test_class_1, test_class_2) -> None:
    graph._vertexes = [test_class_1, test_class_2]
    graph._edges = [(0, 1)]

    graph.clear()

    assert not graph._vertexes
    assert not graph._edges
    assert not graph._matrix


def test_is_empty(graph) -> None:
    assert graph.is_empty()


def test_is_vertex_exists(graph, test_class_1) -> None:
    graph._vertexes = [test_class_1]

    assert graph.is_vertex_exists(test_class_1)


def test_is_edge_exists(graph, test_class_1, test_class_2) -> None:
    graph._vertexes = [test_class_1, test_class_2]
    graph._edges = [(0, 1)]

    assert graph.is_edge_exists((test_class_2, test_class_1))


def test_get_vertexes_quantity(graph, test_class_1, test_class_2) -> None:
    graph._vertexes = [test_class_1, test_class_2]

    assert graph.get_vertexes_quantity() == 2


def test_get_edges_quantity(graph) -> None:
    graph._edges = [(0, 1)]

    assert graph.get_edges_quantity() == 1


def test_get_vertex_degree(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    assert graph.get_vertex_degree(test_class_1) == 1


def test_get_edge_degree(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    assert graph.get_edge_degree((test_class_1, test_class_2)) == 2


def test_add_vertex(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)

    assert graph._vertexes[0] == test_class_1
    assert graph._matrix == [[0, 0], [0, 0]]


def test_add_edge(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    assert graph._edges[0] == (0, 1)
    assert graph._matrix == [[0, 1], [1, 0]]


def test_remove_vertex(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    graph.remove_vertex(test_class_1)

    assert not graph._edges
    assert graph._matrix == [[0]]
    assert graph._vertexes[0] == test_class_2


def test_remove_edge(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    graph.remove_edge(test_class_1, test_class_2)

    assert not graph._edges
    assert graph._matrix == [[0, 0], [0, 0]]


def test_vertex_iter(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)

    iter = graph.vertex_iter()

    assert iter._elements == [test_class_1, test_class_2]
    assert isinstance(iter, BidirectionalIterator)


def test_edge_iter(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    iter = graph.edge_iter()

    assert iter._elements == [(test_class_1, test_class_2)]
    assert isinstance(iter, BidirectionalIterator)


def test_incident_edges_iter(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    iter = graph.incident_edges_iter(test_class_1)

    assert iter._elements == [(test_class_1, test_class_2)]
    assert isinstance(iter, BidirectionalIterator)


def test_adjacent_vertexes_iter(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    iter = graph.adjacent_vertexes_iter(test_class_1)

    assert iter._elements == [test_class_2]
    assert isinstance(iter, BidirectionalIterator)


def test_const_vertex_iter(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    iter = graph.const_vertex_iter()

    assert iter._elements == [test_class_1, test_class_2]
    assert isinstance(iter, ConstBidirectionalIterator)
    assert isinstance(iter.__next__(), ConstContainer)


def test_const_edge_iter(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    iter = graph.const_edge_iter()

    assert iter._elements == [(test_class_1, test_class_2)]
    assert isinstance(iter, ConstBidirectionalIterator)
    assert isinstance(iter.__next__(), tuple)


def test_const_incident_edges_iter(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    iter = graph.const_incident_edges_iter(test_class_1)

    assert iter._elements == [(test_class_1, test_class_2)]
    assert isinstance(iter, ConstBidirectionalIterator)
    assert isinstance(iter.__next__(), tuple)


def test_const_adjacent_vertexes_iter(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    iter = graph.const_adjacent_vertexes_iter(test_class_1)

    assert iter._elements == [test_class_2]
    assert isinstance(iter, ConstBidirectionalIterator)
    assert isinstance(iter.__next__(), ConstContainer)


def test_reverse_vertex_iter(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    iter = graph.reverse_vertex_iter()

    assert iter._elements == [test_class_1, test_class_2]
    assert isinstance(iter, ReverseBidirectionalIterator)


def test_reverse_edge_iter(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    iter = graph.reverse_edge_iter()

    assert iter._elements == [(test_class_1, test_class_2)]
    assert isinstance(iter, ReverseBidirectionalIterator)


def test_reverse_incident_edges_iter(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    iter = graph.reverse_incident_edges_iter(test_class_1)

    assert iter._elements == [(test_class_1, test_class_2)]
    assert isinstance(iter, ReverseBidirectionalIterator)


def test_reverse_adjacent_vertexes_iter(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    iter = graph.reverse_adjacent_vertexes_iter(test_class_1)

    assert iter._elements == [test_class_2]
    assert isinstance(iter, ReverseBidirectionalIterator)


def test_const_reverse_vertex_iter(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    iter = graph.const_reverse_vertex_iter()

    assert iter._elements == [test_class_1, test_class_2]
    assert isinstance(iter, ConstReverseBidirectionalIterator)
    assert isinstance(iter.__next__(), ConstContainer)


def test_const_reverse_edge_iter(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    iter = graph.const_reverse_edge_iter()

    assert iter._elements == [(test_class_1, test_class_2)]
    assert isinstance(iter, ConstReverseBidirectionalIterator)
    assert isinstance(iter.__next__(), tuple)


def test_const_reverse_incident_edges_iter(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    iter = graph.const_reverse_incident_edges_iter(test_class_1)

    assert iter._elements == [(test_class_1, test_class_2)]
    assert isinstance(iter, ConstReverseBidirectionalIterator)
    assert isinstance(iter.__next__(), tuple)


def test_const_reverse_adjacent_vertexes_iter(
    graph, test_class_1, test_class_2
) -> None:
    graph.add_vertex(test_class_1)
    graph.add_vertex(test_class_2)
    graph.add_edge(test_class_1, test_class_2)

    iter = graph.const_reverse_adjacent_vertexes_iter(test_class_1)

    assert iter._elements == [test_class_2]
    assert isinstance(iter, ConstReverseBidirectionalIterator)
    assert isinstance(iter.__next__(), ConstContainer)


def test_copy(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)

    new_graph = graph.__deepcopy__()

    new_graph.add_vertex(test_class_2)

    assert len(new_graph._vertexes) == 2
    assert len(graph._vertexes) == 1


def test_eq(graph, test_class_1) -> None:
    graph.add_vertex(test_class_1)
    new_graph = graph.__deepcopy__()

    assert graph != new_graph


def test_lt(graph, test_class_1, test_class_2) -> None:
    graph.add_vertex(test_class_1)
    new_graph = graph.__deepcopy__()
    new_graph.add_vertex(test_class_2)
    new_graph.add_edge(new_graph._vertexes[0], test_class_2)

    assert graph < new_graph
