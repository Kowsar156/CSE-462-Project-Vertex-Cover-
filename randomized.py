import random
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




def random_approx_vertex_cover(graph):
  C = set()  # Initialize empty set for vertex cover
  E = set()  # Get all vertices as edges
  for u in graph:
    for v in graph[u]:
     E.add((u, v))

  while E:
    #print("Current vertex cover:", C)
    #print("Current edges:", E)
    #print("====================================")
    # Choose an arbitrary edge
    edge = E.pop()
    u, v = edge

    # Randomly choose one vertex from the edge
    vertex = random.choice([u, v])

    # Add the chosen vertex to vertex cover
    C.add(vertex)

    # Remove all incident edges of the chosen vertex
    for neighbor in graph[vertex]:
        if (vertex, neighbor) in E:
            E.remove((vertex, neighbor))
        if (neighbor, vertex) in E:
            E.remove((neighbor, vertex))

  return C

if __name__ == "__main__":

  filename = "vc-exact_111.gr"
  graph = read_graph(filename)

  start_time = time.perf_counter()
  vertex_cover = random_approx_vertex_cover(graph)
  end_time = time.perf_counter()

  print("Randomized approximate vertex cover:", vertex_cover)
  print("  ")
  print("Number of vertices in the graph:", len(graph))
  print("Number of vertices in the randomized vertex cover:", len(vertex_cover))
  print("  ")
  #print("Time taken:", end_time - start_time, "seconds")
  print("Time taken:", (end_time - start_time)*1000, "milliseconds")
  print("  ")