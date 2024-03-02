def is_vertex_cover(graph, cover):
    for edge in graph:
        if edge[0] not in cover and edge[1] not in cover:
            return False
    return True

def vertex_cover(graph, vertices, cover):
    if not vertices:
        if is_vertex_cover(graph, cover):
            return cover
        else:
            return None
    v = vertices[0]
    with_v = vertex_cover(graph, vertices[1:], cover + [v])
    if with_v:
        return with_v
    else:
        without_v = vertex_cover(graph, vertices[1:], cover)
        return without_v

def main():
    graph = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
    vertices = [0, 1, 2, 3, 4]
    cover = vertex_cover(graph, vertices, [])
    if cover:
        print("Vertex cover:", cover)
    else:
        print("No vertex cover found.")

if __name__ == "__main__":
    main()
