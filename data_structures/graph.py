"""
Vertices connected by (possibly weighted) edges.

- Bidirectional: edges are two-way
- Direcional: edges are one-way
- A tree (and therefore also a linkned list) are forms of graphs

Graph representations:
    Adjacency matrix:
    - Row: a vertex
    - Columnns: vertices it has an edge with
    - All zeros on the diagonal (no self-loops)
    - Undirected graph: matrix is symmetric
    - Weighted graph: matrix contains weights instead of 1s and 0s
    Adjacency list:
    - Dict key: a vertex
    - Dict value: list of vertices it has an edge with

Space complexity:
- Adjacency matrix: O(V^2) - store all zeros and ones
- Adjacency list: O(V + E) - store only existing edges

Time complexity:
- Adding a vertex (not connected)
    - Adjacency matrix: O(V^2) - adding new row anc column
    - Adjacency list: O(1) - appending key-value pair to dict
- Addinge an edge:
    - Adjacency matrix: O(1) - updating matrix values
    - Adjacency list: O(1) - appending to list
- Removing an edge:
    - Adjacency matrix: O(1) - updating matrix values
    - Adjacency list: O(E) - searching for vertex in list of edges
- Removing a vertex:
    - Adjacency matrix: O(V^2) - removing one row and one column
    - Adjacency list: O(V + E) - removing vertex from dict and all lists
"""


class Graph:
    def __init__(self):
        self.adj_list = {}

    def print(self):
        for vertex in self.adj_list:
            print(vertex, " : ", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        else:
            return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for vtx in self.adj_list[vertex]:
                self.adj_list[vtx].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
