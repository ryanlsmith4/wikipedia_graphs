#!python

import sys
import random


""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""
from collections import deque

class Vertex(object):

    def __init__(self, vertex):
        """initialize a vertex and its neighbors
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        
        """
        self.id = vertex
        self.neighbors = {}

    def __str__(self):
        """output the list of neighbors of this vertex"""
        # return(str(self.id))
        return str(self.id) + " adjancent to " + str([x.id for x in self.neighbors])

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.neighbors.keys())

    def add_neighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        # check if vertex is already a neighbor
        if vertex in self.neighbors:
            raise ValueError('Vertex already a neighbor')
        # if not, add vertex to neighbors and assign weight.
        else:
            self.neighbors[vertex] = weight

    def get_neighbors(self):
        """return the neighbors of this vertex"""
        # return the neighbors
        # if len(self.neighbors.keys()) != 0:
        #     # print('\n')
        return self.neighbors.keys()
        # else:
        #     # print(self.id)
        #     raise ValueError('No neighbors')
        # return  self.neighbors.keys()

    def get_id(self):
        """return the id of this vertex"""
        return self.id

    def get_edge_weight(self, vertex):
        """return the weight of this edge"""
        # return the weight of the edge from this
        # vertext to the given vertex.
        if vertex in self.neighbors:
            return self.neighbors[vertex]
        else:
            raise ValueError('Vertex not in Graph')
    
    def is_neighbor(self, vert):

        if vert in self.neighbors:
            return True
        else:
            return False


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""


class Graph:
    def __init__(self):
        """ initializes a graph object with an empty dictionary.
        """
        self.vert_dict = {}
        # self.vert_dict = []
        self.num_vertices = 0

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_dict.values())


    def __str__(self):
            return str(self.vert_dict)
            
    def add_vertex(self, key):
        """add a new vertex object to the graph with
        the given key and return the vertex
        """
        # increment the number of vertices
        self.num_vertices += 1
        # create a new vertex
        vertex = Vertex(key)
        # add the new vertex to the vertex dictionary with a list as the value
        # self.vert_dict[vertex] = []
        # add the new vertex to the vertex list
        self.vert_dict[key] = vertex
        # print(vertex)
        # return the new vertex
        return vertex

    def get_vertex(self, vertex):
        """return the vertex if it exists"""
        # return the vertex if it is in the graph
        if vertex in self.vert_dict:
            # print(self.vert_dict[vertex])
            return self.vert_dict[vertex]
        else:
            raise ValueError('Vertex not in graph')

    def add_edge(self, from_vert, to_vert, cost=0):
        """add an edge from vertex f to vertex t with a cost
        """
        # if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        if from_vert not in self.vert_dict or to_vert not in self.vert_dict:
            raise ValueError('vertexes not in graph')
        # if both vertices in the graph, add the
        # edge by making t a neighbor of f
        else:
           self.vert_dict[from_vert].add_neighbor(self.vert_dict[to_vert], cost)
           self.vert_dict[to_vert].add_neighbor(self.vert_dict[from_vert], cost)


    def get_vertices(self):
        """return all the vertices in the graph"""
        return str(self.vert_dict.keys())

    def bfs(self, vertex, n=0):
        """Perform breadth first search to get the single shortest path
        Between 2 nodes"""
        # Make sure the input node is actually in the graph
        # print(self.vert_dict.keys())
        # print(vertex)
        if vertex not in self.vert_dict:
            raise KeyError("Vert not in Graph!")
        visited = []
        first = self.get_vertex(vertex)
        queue = deque()
        queue.appendleft(first)
        counter = 0

        while queue:
            vert = queue.pop()

            if vert not in visited:
                 visited.append(vert.id)
                 edges = vert.get_neighbors()
                #  print(edges)

                 for edge in edges:
                    #  print('right')
                    #  print(edge)
                     queue.appendleft(edge)
            counter += 1
            if counter == n and n > 0:
                return visited
        # print('here')
        return visited


    def find_shortest_path(self, from_vert, to_vert):
        """Perform breadth first search to get the single shortest path
        Between 2 nodes"""
        # dictionary for path key: vector.id | value: parent
        visited = {}
        # store the shortest path in a list
        shortest_path = []
        num_edges = len(shortest_path) -1
        # Use a queue for it's FIFO properties 
        queue = deque()
        # Make sure the input node is actually in the graph
        if from_vert not in self.vert_dict or to_vert not in self.vert_dict:
            raise KeyError("One of the verticies is not inside of the graph!")

        # BASE CASE!! If they are the same vertex, the path is itself and the # of edges
        # is 0!
        if from_vert == to_vert:
            return("Vertices in shortest path: {}\n Number of edges in shortest path: {} ".format(shortest_path, num_edges))
        else:
            # Enter the queue before while to set end point
            queue.appendleft(from_vert)
            # inital value set to 0 for start point
            visited[from_vert] = 0

            while queue:
                # get the top of the queue
                vert_id = queue.pop()
                current_vert = self.get_vertex(vert_id)
                # iterate through the neighbors of the current vert
                for neighbor in current_vert.get_neighbors():
                    # if they have been visited continue; else do the things
                    if neighbor in visited:
                        continue
                    queue.appendleft(neighbor)
                    visited[neighbor] = current_vert.id
                    # ensure we don't have duplicates
                    if current_vert.id not in shortest_path:
                        shortest_path.append(current_vert.id)
            # since we've reached the target add it to the list
            shortest_path.append(to_vert)
            # return(shortest_path)
            return("Vertices in shortest path: {}\n Number of edges in shortest path: {} ".format(",".join(shortest_path), num_edges ))

    def clique(self):
        # create needed structures and variables
        key_list = list(self.vert_dict.values())
        rand_choice = random.choice(key_list)
        clique = []
        clique.append(rand_choice)
        # vert_neighbors = []
        for vert in self.vert_dict.values():
            for vert1 in clique:
                print(vert)
                if vert1.is_neighbor(vert):
                    print('here')
                    print(vert1)
                    clique.append(vert1)
                
        return clique 



if __name__ == "__main__":
    g = Graph()

    vertices = [1,2,3,4,5]
    # print(vertices)
    
    for vert in vertices:
        # print(elem.id)
        g.add_vertex(vert)


    one =  g.get_vertex(1)
    two =  g.get_vertex(2)
    three =  g.get_vertex(3)
    four =  g.get_vertex(4)
    five =  g.get_vertex(5)
    # print("here: {}".format(one.id))

    g.add_edge(one.id, two.id)
    g.add_edge(one.id, four.id)
    g.add_edge(two.id, three.id)
    g.add_edge(two.id, four.id)
    g.add_edge(two.id, five.id)
    g.add_edge(three.id, five.id)

    # print(g)


    print(g.clique())