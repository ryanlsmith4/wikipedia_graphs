from graph import Graph, Vertex
import sys

def read_file():
  # if len(sys.argv[2]) == 0 or len(sys.argv[3] == 0):
  #   raise ValueError('Need to pass in a vertex')
  # from_vert = int(sys.argv[2])
  # to_vert = int(sys.argv[3])
  # print(from_vert)
  # print(to_vert)
  vertex_list = []
  edges = []
  counter = 0
  with open(sys.argv[1], 'r') as f:
      for line in f:
          x = line.strip('()\n').split(',')
          # counter at 1 indicates the input list or the vert list
          if counter == 1:
              vertex_list = x
          counter += 1
          # counter > 2 indicates the edges
          if counter > 2:
              edges.append(x)
          
  g = Graph()
  for vertex in vertex_list:
      g.add_vertex(vertex)

  for edge in edges:
      g.add_edge(edge[0], edge[1])
      

  return g