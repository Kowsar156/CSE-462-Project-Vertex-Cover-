import time

def read_graph(filename):

  graph = {}
  with open(filename, 'r') as f:
    # Read the number of vertices and edges from the first line
    num_vertices, _ = map(int, f.readline().strip().split())

    # Read edges and build the adjacency list
    for line in f:
      node1, node2 = map(int, line.strip().split())
      # Use sets to avoid duplicate neighbors and efficiently check for connections
      graph.setdefault(node1, set()).add(node2)
      graph.setdefault(node2, set()).add(node1)
  return graph







def greedy_vertex_cover(graph):

    C = set()  # Initialize empty set for vertex cover
    E = set()  # Get all edges as tuples (u, v)
    for u in graph:
        for v in graph[u]:
            E.add((u, v))

    while E:
        # Find an vertex with maximum degree 
        max_degree_vertex = max(E, key=lambda edge: len(graph[edge[0]]))

        # Add the vertices of the max degree edge to the cover
        C.add(max_degree_vertex[0])
        # C.add(max_degree_vertex[1])

        # Remove all edges incident to the selected vertices
        incident_edges = [(max_degree_vertex[0], neighbor) for neighbor in graph[max_degree_vertex[0]]] + \
                         [(neighbor, max_degree_vertex[0]) for neighbor in graph[max_degree_vertex[0]]] 

        E.difference_update(incident_edges)

    return C

if __name__ == "__main__":
  filename = "graph.gr"
  graph = read_graph(filename)
 
  start_time = time.perf_counter() 
  vertex_cover = greedy_vertex_cover(graph)
  end_time = time.perf_counter()

  print("Heuristic vertex cover:", vertex_cover)
  print("  ")
  print("Number of vertices in the graph:", len(graph))
  print("Number of vertices in the heuristic vertex cover:", len(vertex_cover))
  print("  ")
  print("Time taken:", (end_time - start_time)*1000, "milliseconds")
  print("  ")
