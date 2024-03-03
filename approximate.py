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



def approx_vertex_cover(graph):
  C = set()  # Initialize empty set for vertex cover
  E = set()  # Get all vertices as edges
  for u in graph:
    for v in graph[u]:
     E.add((u, v))
 
  while E:
    # Choose an arbitrary edge
    edge = E.pop()
    u, v = edge
 
    # Add vertices of chosen edge to vertex cover
    C.add(u)
    C.add(v)
 
    # Remove all incident edges from both vertices
    for neighbor in graph[u]:
      if neighbor != v and (u, neighbor) in E:
        E.remove((u, neighbor))
      if neighbor != v and (neighbor, u) in E:
        E.remove((neighbor, u))

    for neighbor in graph[v]:
      if neighbor != u and (v, neighbor) in E:
        E.remove((v, neighbor))
      if neighbor != u and (neighbor, v) in E:
        E.remove((neighbor, v))
 
  return C
 
if __name__ == "__main__":

  filename = "vc-exact_111.gr"
  graph = read_graph(filename)
  
  start_time = time.perf_counter()
  vertex_cover = approx_vertex_cover(graph)
  end_time = time.perf_counter()

  print("Approximate vertex cover:", vertex_cover)
  print("  ")
  print("Number of vertices in the graph:", len(graph))
  print("Number of vertices in the approximate vertex cover:", len(vertex_cover))
  print("  ")
  #print("Time taken:", end_time - start_time, "seconds")
  print("Time taken:", (end_time - start_time)*1000, "milliseconds")
  print("  ")