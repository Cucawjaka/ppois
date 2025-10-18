import copy
from functools import total_ordering

from task2.errors.EdgeNotExistsError import EdgeNotExistsError
from task2.errors.VertexNotExistsError import VertexNotExistsError
from task2.iterators.BidirectionalIterator import BidirectionalIterator
from task2.IBidirectionalIterator import IBidirectionalIterator
from task2.iterators.ConstBidirectionalIterator import ConstBidirectionalIterator
from task2.iterators.ConstReverseBidirectionalIterator import (
    ConstReverseBidirectionalIterator,
)
from task2.iterators.ReverseBidirectionalIterator import ReverseBidirectionalIterator


adjacency_matrix = list[list[int]]


@total_ordering
class Graph[V]:
    def __init__(self) -> None:
        self._matrix: adjacency_matrix = list()
        self._vertexes: list[V] = list()
        self._edges: list[tuple[int, int]] = list()

    def _get_adjacent_vertexes(self, vertex: V) -> list[V]:
        if not self.is_vertex_exists(vertex):
            raise VertexNotExistsError("Вершины не существует")

        adjacent_vertexes: list[V] = list()
        vertex_index: int = self._vertexes.index(vertex)

        for i in range(len(self._matrix)):
            if self._matrix[vertex_index][i]:
                adjacent_vertexes.append(self._vertexes[i])

        return adjacent_vertexes

    def _get_incident_edges(self, vertex: V) -> list[tuple[V, V]]:
        if not self.is_vertex_exists(vertex):
            raise VertexNotExistsError("Вершины не существует")

        incident_edges: list[tuple[V, V]] = list()
        vertex_index: int = self._vertexes.index(vertex)

        for i in range(len(self._matrix)):
            if self._matrix[vertex_index][i]:
                if vertex_index <= i:
                    incident_edges.append(
                        (self._vertexes[vertex_index], self._vertexes[i])
                    )
                else:
                    incident_edges.append(
                        (self._vertexes[i], self._vertexes[vertex_index])
                    )

        return incident_edges

    def _get_edges(self) -> list[tuple[V, V]]:
        edges: list[tuple[V, V]] = list()

        for edge in self._edges:
            first_index: int = edge[0]
            second_index: int = edge[1]

            edges.append((self._vertexes[first_index], self._vertexes[second_index]))

        return edges

    def clear(self) -> None:
        self._matrix = list()
        self._vertexes = list()
        self._edges = list()

    def is_empty(self) -> bool:
        return not self._matrix

    def is_vertex_exists(self, vertex: V) -> bool:
        return vertex in self._vertexes

    def is_edge_exists(self, edge: tuple[V, V]) -> bool:
        first_index: int = self._vertexes.index(edge[0])
        second_index: int = self._vertexes.index(edge[1])

        found_edge: tuple[int, int] = (
            min(first_index, second_index),
            max(first_index, second_index),
        )

        return found_edge in self._edges

    def get_vertexes_quantity(self) -> int:
        return len(self._vertexes)

    def get_edges_quantity(self) -> int:
        return len(self._edges)

    def get_vertex_degree(self, vertex: V) -> int:
        if vertex in self._vertexes:
            index: int = self._vertexes.index(vertex)
            return sum(self._matrix[index])
        raise VertexNotExistsError("Вершины не существует")

    def get_edge_degree(self, edge: tuple[V, V]) -> int:
        if edge in self._get_edges():
            return 2
        raise EdgeNotExistsError("Ребра не существует")

    def add_vertex(self, vertex: V) -> None:
        self._vertexes.append(vertex)

        self._matrix.append([0] * len(self._matrix))

        for row in self._matrix:
            row.append(0)

    def add_edge(self, first_vertex: V, second_vertex: V) -> None:
        if not self.is_vertex_exists(first_vertex) or not self.is_vertex_exists(
            second_vertex
        ):
            raise VertexNotExistsError("Вершины не существует")

        first_index: int = self._vertexes.index(first_vertex)
        second_index: int = self._vertexes.index(second_vertex)

        self._matrix[first_index][second_index] = 1
        self._matrix[second_index][first_index] = 1

        self._edges.append(
            (min(first_index, second_index), max(first_index, second_index))
        )

    def remove_vertex(self, vertex: V) -> None:
        if not self.is_vertex_exists(vertex):
            raise VertexNotExistsError("Вершины не существует")

        vertex_index: int = self._vertexes.index(vertex)

        self._vertexes.pop(vertex_index)

        for row in self._matrix:
            row.pop(vertex_index)

        self._matrix.pop(vertex_index)

        self._edges.clear()
        for i in range(len(self._matrix)):
            for j in range(i + 1, len(self._matrix)):
                if self._matrix[i][j]:
                    self._edges.append((i, j))

    def remove_edge(self, first_vertex: V, second_vertex: V) -> None:
        if not self.is_edge_exists((first_vertex, second_vertex)):
            raise EdgeNotExistsError("Ребра не существует")

        first_index: int = self._vertexes.index(first_vertex)
        second_index: int = self._vertexes.index(second_vertex)

        self._edges.remove((first_index, second_index))

        self._matrix[first_index][second_index] = 0
        self._matrix[second_index][first_index] = 0

    def vertex_iter(self, position: int = -1) -> IBidirectionalIterator[V]:
        return BidirectionalIterator(self._vertexes, position)

    def edge_iter(self, position: int = -1) -> IBidirectionalIterator[tuple[V, V]]:
        edges: list[tuple[V, V]] = self._get_edges()
        return BidirectionalIterator[tuple[V, V]](edges, position)

    def incident_edges_iter(
        self, vertex: V, position: int = -1
    ) -> IBidirectionalIterator[tuple[V, V]]:
        incident_edges: list[tuple[V, V]] = self._get_incident_edges(vertex)
        return BidirectionalIterator[tuple[V, V]](incident_edges, position)

    def adjacent_vertexes_iter(
        self, vertex: V, position: int = -1
    ) -> IBidirectionalIterator[V]:
        adjacent_vertexes: list[V] = self._get_adjacent_vertexes(vertex)
        return BidirectionalIterator(adjacent_vertexes, position)

    def const_vertex_iter(self, position: int = -1) -> IBidirectionalIterator[V]:
        return ConstBidirectionalIterator(self._vertexes, position)

    def const_edge_iter(
        self, position: int = -1
    ) -> IBidirectionalIterator[tuple[V, V]]:
        edges: list[tuple[V, V]] = self._get_edges()
        return ConstBidirectionalIterator[tuple[V, V]](edges, position)

    def const_incident_edges_iter(
        self, vertex: V, position: int = -1
    ) -> IBidirectionalIterator[tuple[V, V]]:
        incident_edges: list[tuple[V, V]] = self._get_incident_edges(vertex)
        return ConstBidirectionalIterator[tuple[V, V]](incident_edges, position)

    def const_adjacent_vertexes_iter(
        self, vertex: V, position: int = -1
    ) -> IBidirectionalIterator[V]:
        adjacent_vertexes: list[V] = self._get_adjacent_vertexes(vertex)
        return ConstBidirectionalIterator(adjacent_vertexes, position)

    def reverse_vertex_iter(
        self, position: int | None = None
    ) -> IBidirectionalIterator[V]:
        return ReverseBidirectionalIterator(self._vertexes, position)

    def reverse_edge_iter(
        self, position: int | None = None
    ) -> IBidirectionalIterator[tuple[V, V]]:
        edges: list[tuple[V, V]] = self._get_edges()
        return ReverseBidirectionalIterator[tuple[V, V]](edges, position)

    def reverse_incident_edges_iter(
        self, vertex: V, position: int | None = None
    ) -> IBidirectionalIterator[tuple[V, V]]:
        incident_edges: list[tuple[V, V]] = self._get_incident_edges(vertex)
        return ReverseBidirectionalIterator[tuple[V, V]](incident_edges, position)

    def reverse_adjacent_vertexes_iter(
        self, vertex: V, position: int | None = None
    ) -> IBidirectionalIterator[V]:
        adjacent_vertexes: list[V] = self._get_adjacent_vertexes(vertex)
        return ReverseBidirectionalIterator(adjacent_vertexes, position)

    def const_reverse_vertex_iter(
        self, position: int | None = None
    ) -> IBidirectionalIterator[V]:
        return ConstReverseBidirectionalIterator(self._vertexes, position)

    def const_reverse_edge_iter(
        self, position: int | None = None
    ) -> IBidirectionalIterator[tuple[V, V]]:
        edges: list[tuple[V, V]] = self._get_edges()
        return ConstReverseBidirectionalIterator[tuple[V, V]](edges, position)

    def const_reverse_incident_edges_iter(
        self, vertex: V, position: int | None = None
    ) -> IBidirectionalIterator[tuple[V, V]]:
        incident_edges: list[tuple[V, V]] = self._get_incident_edges(vertex)
        return ConstReverseBidirectionalIterator[tuple[V, V]](incident_edges, position)

    def const_reverse_adjacent_vertexes_iter(
        self, vertex: V, position: int | None = None
    ) -> IBidirectionalIterator[V]:
        adjacent_vertexes: list[V] = self._get_adjacent_vertexes(vertex)
        return ConstReverseBidirectionalIterator(adjacent_vertexes, position)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return False

        if set(self._vertexes) != set(other._vertexes):
            return False

        self_edges: list[tuple[V, V]] = self._get_edges()
        other_edges: list[tuple[V, V]] = other._get_edges()

        return set(self_edges) == set(other_edges)

    def __lt__(self, other: "Graph") -> bool:
        self_sum: int = sum(sum(row) for row in self._matrix)
        other_sum: int = sum(sum(row) for row in self._matrix)

        return self_sum == other_sum

    def __deepcopy__(self, memo: None = None) -> "Graph[V]":
        new_graph = Graph[V]()
        new_graph._vertexes = copy.deepcopy(self._vertexes, memo)
        new_graph._matrix = copy.deepcopy(self._matrix, memo)
        new_graph._edges = copy.deepcopy(self._edges, memo)
        return new_graph

    def __str__(self) -> str:
        vertexes_str = ", ".join(str(v) for v in self._vertexes)
        edges_str = ", ".join(
            f"({self._vertexes[a]}, {self._vertexes[b]})" for a, b in self._edges
        )
        return f"Graph(\nvertexes=[{vertexes_str}],\nedges=[{edges_str}]\n)"
