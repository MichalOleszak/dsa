# Karger's algorithm 
#
# Min cut = cut with fewest crossing edges
#
# Input file structure: multiple-space separated integers, first is node ID starting from 1,
# follower by its edges:
#
# 1	37	79	164	155	...
# 2	123	134	10	141	...
# 3	48	123	134	1   ...
# ...


from copy import deepcopy
import random
import math


def load_data(file_path: str) -> dict[int, list[int]]:
    with open(file_path, "r") as f:
        lines = f.readlines()
        graph = [
            list(map(lambda i: int(i), l.split("\t")[1:-1]))
            for l in lines
        ]
    return {node: edges for node, edges in enumerate(graph, start=1)}


def pick_random_edge(graph: dict[int, list[int]]) -> tuple[int, int]:
    u = random.choice(list(graph.keys()))
    v = random.choice(graph[u])
    return u, v


def contract_edge(graph: dict[int, list[int]], edge: tuple[int, int]) -> dict[int, list[int]]:
    u, v = edge
    graph[u] = graph[u] + graph[v]
    del graph[v]
    for i in graph.keys():
        graph[i] = [j if j != v else u for j in graph[i]]
    return graph



def remove_self_loops(graph: dict[int, list[int]]) -> dict[int, list[int]]:
    for node, edges in graph.items():
        while node in edges:
            edges.remove(node)
    return graph


def get_num_crossing_edges(graph: dict[int, list[int]]) -> dict[int, list[int]]:
    ce = 0
    for edges in graph.values():
        ce += len(edges)
    return ce / 2


def run_once(graph: dict[int, list[int]]) -> int:
    while len(graph) > 2:
        edge = pick_random_edge(graph)
        graph = contract_edge(graph, edge)
        graph = remove_self_loops(graph)
    num_crossing_edges = get_num_crossing_edges(graph)
    return num_crossing_edges


def get_min_cut_crossing_edges(file_path: str, num_runs: int = 10_000) -> int:
    graph = load_data(file_path)
    min_cut = math.inf
    for _ in range(num_runs):
        seed = random.randint(0, 999_999)
        random.seed(seed)
        num_crossing_edges = run_once(deepcopy(graph))
        if num_crossing_edges < min_cut:
            min_cut = num_crossing_edges
            print(f"min cut: {min_cut}")
    return min_cut

