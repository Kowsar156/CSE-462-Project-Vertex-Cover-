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

# Example usage
filename = "graph.gr"
graph = read_graph(filename)

# Print the graph dictionary (uncomment to see the structure)
print(graph)