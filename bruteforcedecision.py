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

def main():
    graph = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
    vertices = [0, 1, 2, 3, 4]
    k = 3  # Desired cover size (k - 1)
    if vertex_cover_decision(graph, vertices, k - 1, []):
        print(f"There exists a vertex cover with size {k - 1}.")
    else:
        print(f"There is no vertex cover with size {k - 1}.")

if __name__ == "__main__":
    main()
