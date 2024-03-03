def read_graph(filename):
  """
  Reads a graph from a file with the specified format and creates a dictionary.

  Args:
      filename: The name of the file containing the graph.

  Returns:
      A dictionary representing the graph, where keys are vertex numbers and values are sets of adjacent vertices.
  """
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


def write_vertex_cover_to_file(vertex_cover, num_vertices, filename="vertex_cover.vc"):
 """
 Writes a vertex cover to a file in the specified format.

 Args:
     vertex_cover: A set containing the vertex numbers in the cover.
     num_vertices: The total number of vertices in the graph.
     filename: The name of the file to write to (default is "output.vc").
 """

 with open(filename, 'w') as f:
   # Write the first line with header information
   f.write(f"s vc {num_vertices} {len(vertex_cover)}\n")

   # Write each vertex number from the cover in separate lines
   for vertex in vertex_cover:
     f.write(f"{vertex}\n")





def approx_vertex_cover(graph):
    """
    This function implements an approximation algorithm for the minimum vertex cover problem
    using the maximum degree node solution first.

    Args:
        graph: A dictionary representing the graph. Keys are vertices, and values are sets of adjacent vertices.

    Returns:
        A set representing the approximate vertex cover.
    """
    C = set()  # Initialize empty set for vertex cover
    E = set()  # Get all edges as tuples (u, v)
    for u in graph:
        for v in graph[u]:
            E.add((u, v))

    while E:
        # Find an edge with maximum degree vertices
        max_degree_edge = max(E, key=lambda edge: len(graph[edge[0]]))

        # Add the vertices of the max degree edge to the cover
        C.add(max_degree_edge[0])
        # C.add(max_degree_edge[1])

        # Remove all edges incident to the selected vertices
        incident_edges = [(max_degree_edge[0], neighbor) for neighbor in graph[max_degree_edge[0]]] + \
                         [(neighbor, max_degree_edge[0]) for neighbor in graph[max_degree_edge[0]]] 

        E.difference_update(incident_edges)

    return C

 
# Example usage
filename = "graph.gr"
graph = read_graph(filename)
 
vertex_cover = approx_vertex_cover(graph)
print("Approximate vertex cover:", vertex_cover)
print("  ")
print("Number of vertices in the graph:", len(graph))
print("Number of vertices in the approximate vertex cover:", len(vertex_cover))
print("  ")
write_vertex_cover_to_file(vertex_cover, len(graph))