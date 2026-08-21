def _load_data(file_path: str) -> dict[int, list[tuple]]:
    graph = dict()
    with open(file_path, "r") as f:
        for line in f:
            items = line.split("\t")
            graph[int(items[0])] = [
                tuple(map(int, edge.split(",")))
                for edge in items[1:-1]
            ]
    return graph


def _get_total_vertices(graph):
    vertices = set()
    for v, edges in graph.items():
        vertices.add(v)
        for w, _ in edges:
            vertices.add(w)
    return len(vertices)


def _run_dijkstra(graph, source):
    processed_vertices = [source]
    shortest_path_distances = {source: 0}

    total_vertices = _get_total_vertices(graph)

    while len(processed_vertices) < total_vertices:
        current_min_value = 1_000_000
        current_min_vertex = None
        for v in processed_vertices:
            for w, dist in graph[v]:
                if w not in processed_vertices:
                    candidate = shortest_path_distances[v] + dist
                    if candidate < current_min_value:
                        current_min_value = candidate
                        current_min_vertex = w
        shortest_path_distances[current_min_vertex] = current_min_value
        processed_vertices.append(current_min_vertex)

    return shortest_path_distances



def _format_result(dijkstra_result):
    VERTICES_TO_REPORT = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    results = [dijkstra_result[vertex] for vertex in VERTICES_TO_REPORT]
    return ",".join(list(map(str, results)))



def main():
    graph = _load_data("data/dijkstra.txt")
    dijkstra_result = _run_dijkstra(graph, 1)
    output = _format_result(dijkstra_result)
    return output
