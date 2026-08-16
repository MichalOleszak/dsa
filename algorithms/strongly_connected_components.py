# Kosaraju's two-pass algorithm for finding strongly connected components in a directed graph

from collections import Counter, defaultdict
from tqdm import tqdm


def _load_data(file_path: str) -> tuple[dict[int, list[int]], dict[int, list[int]]]:
    graph = defaultdict(list)
    graph_rev = defaultdict(list)
    with open(file_path, "r") as f:
        for line in f:
            u, v = map(lambda i: int(i), line.split(" ")[:-1])
            graph[u].append(v)
            graph_rev[v].append(u)
    return graph, graph_rev


def _dfs_pass_1(edges: dict[int, list[int]], vertex: int, t: int, finishing_times: dict, explored_nodes: set) -> int:
    stack = [(vertex, "enter")]
    while stack:
        current_vertex, state = stack.pop()
        if state == "enter":
            if current_vertex in explored_nodes:
                continue
            explored_nodes.add(current_vertex)
            stack.append((current_vertex, "finish"))
            for neighbor in edges[current_vertex]:
                if neighbor not in explored_nodes:
                    stack.append((neighbor, "enter"))
        elif state == "finish":
            finishing_times[current_vertex] = t
            t += 1
    return t


def _dfs_pass_2(edges: dict[int, list[int]], vertex: int, current_leader: int, leaders: dict, explored_nodes: set) -> None:
    stack = [vertex]
    explored_nodes.add(vertex)
    while stack:
        current_vertex = stack.pop()
        leaders[current_vertex] = current_leader
        for neighbor in edges[current_vertex]:
            if neighbor not in explored_nodes:
                explored_nodes.add(neighbor)
                stack.append(neighbor)


def get_strongly_connected_components(graph_adj_list: dict[int, list[int]], graph_rev_adj_list: dict[int, list[int]]):
    t = 0
    explored_nodes = set()
    finishing_times = dict()

    max_node_label = max(graph_adj_list.keys() | graph_rev_adj_list.keys())

    for i in tqdm(range(max_node_label, 0, -1), "DFS pass 1"):
        if i not in explored_nodes:
            t = _dfs_pass_1(graph_rev_adj_list, i, t, finishing_times, explored_nodes)

    finishing_times_sorted = sorted(finishing_times.items(), key=lambda x: x[1], reverse=True)

    explored_nodes = set()
    leaders = dict()

    for i, _ in tqdm(finishing_times_sorted, "DFS pass 2"):
        if i not in explored_nodes:
            current_leader = i
            _ = _dfs_pass_2(graph_adj_list, i, current_leader, leaders, explored_nodes)

    return leaders


def format_result(leaders: dict[int, int]):
    """
    Output Format: You should output the sizes of the 5 largest SCCs in the given graph,
    in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm
    computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your
    answer should be "500,400,300,200,100" (without the quotes). If your algorithm finds less
    than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only
    3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0"
    (without the quotes).  (Note also that your answer should not have any spaces in it.)
    """
    scc_sizes = list(Counter(leaders.values()).values())
    scc_sizes_decraesing = sorted(scc_sizes, reverse=True)[:5]
    while len(scc_sizes_decraesing) < 5:
        scc_sizes_decraesing.append(0)
    return ",".join(list(map(str, scc_sizes_decraesing)))


def run(file_path: str):
    graph, graph_rev = _load_data(file_path)
    sccs = get_strongly_connected_components(graph, graph_rev)
    formated_result = format_result(sccs)
    return formated_result