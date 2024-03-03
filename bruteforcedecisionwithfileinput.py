def is_vertex_cover(graph, cover):
    for edge in graph:
        if edge[0] not in cover and edge[1] not in cover:
            return False
    return True

def vertex_cover_decision(graph, vertices, cover_size, cover):
    if cover_size < 0:
        return False
    if not vertices:
        return len(cover) == cover_size
    v = vertices[0]
    with_v = vertex_cover_decision(graph, vertices[1:], cover_size - 1, cover + [v])
    if with_v:
        return True
    else:
        return vertex_cover_decision(graph, vertices[1:], cover_size, cover)

def read_graph_from_file(file_path):
    graph = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('p'):
                continue
            elif line.startswith('c'):
                continue
            else:
                parts = line.split()
                graph.append((int(parts[0]), int(parts[1])))
    return graph

def main():
    file_path = "./pace2019-vc-exact-public-v2/public/vc-exact_005.gr"
    graph = read_graph_from_file(file_path)
    vertices = list(set([v for edge in graph for v in edge]))
    k = 200  # Desired cover size (k - 1)
    if vertex_cover_decision(graph, vertices, k - 1, []):
        print(f"There exists a vertex cover with size {k - 1}.")
    else:
        print(f"There is no vertex cover with size {k - 1}.")

if __name__ == "__main__":
    main()
