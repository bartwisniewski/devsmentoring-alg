from __future__ import annotations
from typing import Dict, List
from dfs import DFS
from bfs import BFS


class Vertex:
    def __init__(self, id, order, value):
        self.__id = id
        self.__order = order
        self.value = value

    @property
    def id(self) -> int:
        return self.__id

    @property
    def order(self) -> int:
        return self.__order


class Graph:
    def __init__(self):
        self.vertices: Dict[int, Vertex] = {}
        self.edges: List[List[int]] = []
        self.__ids: List[int] = []

    def add_vertex(self, new_id, value) -> None:
        if new_id in self.vertices.keys():
            return
        next_order = len(self.vertices)
        self.vertices.update({new_id: Vertex(new_id, next_order, value)})
        no = len(self.vertices)
        for edge in self.edges:
            edge.append(0)
        self.edges.append([0]*no)
        self.__ids.append(new_id)

    def edit_vertex(self, id, value):
        vertex = self.vertices.get(id)
        if vertex:
            vertex.value = value

    def get_vertex(self, id) -> Vertex:
        return self.vertices.get(id, None)

    def set_edge(self, first_id: int, second_id: int, weight: int) -> None:
        keys = self.vertices.keys()
        if first_id not in keys or second_id not in keys:
            return
        order1 = self.vertices.get(first_id).order
        order2 = self.vertices.get(second_id).order
        self.edges[order1][order2] = weight

    def get_neighbours(self, id):
        vertex = self.vertices.get(id)
        if not vertex:
            return []
        order = vertex.order
        neighbours = []
        order2 = 0
        for weight in self.edges[order]:
            if weight > 0:
                neighbours.append(self.__ids[order2])
            order2 += 1
        return neighbours

    def show_vertex(self, id):
        vertex = self.vertices.get(id)
        if not vertex:
            return
        order = vertex.order
        edges = []
        order2 = 0
        for weight in self.edges[order]:
            if weight > 0:
                edges.append(f'{self.__ids[order2]} ({weight})')
            order2 += 1

        print(f"{vertex.id}: {vertex.value} -> {', '.join(edges)}")

    def print_graph(self):
        for vertex in self.vertices:
            self.show_vertex(vertex)


def create_example_graph():
    graph = Graph()
    graph.add_vertex(10, 52)
    graph.add_vertex(20, 104)
    graph.add_vertex(30, 208)
    graph.add_vertex(40, 408)
    graph.add_vertex(50, 608)
    graph.add_vertex(60, 808)
    graph.add_vertex(70, 908)
    graph.add_vertex(80, 1008)
    graph.set_edge(10, 20, 1)
    graph.set_edge(10, 30, 1)
    graph.set_edge(20, 40, 1)
    graph.set_edge(20, 50, 1)
    graph.set_edge(20, 60, 1)
    graph.set_edge(30, 70, 1)
    graph.set_edge(30, 80, 1)
    graph.set_edge(60, 10, 10)
    graph.set_edge(80, 20, 10)
    return graph


if __name__ == "__main__":
    graph = create_example_graph()
    graph.print_graph()
    print("print with DFS:")
    dfs = DFS(graph, 10, graph.show_vertex)
    dfs.run()
    print("print with BFS:")
    bfs = BFS(graph, 10, graph.show_vertex)
    bfs.run()
