# Graph: An efficient graph.
# A graph implementation that uses an adjacency list to represent vertices
# and edges.
# Your implementation should pass the tests in test_graph.py.
# Erin O'Connell    

import functools

class Graph(object):

    def __init__(self):
        self.data = {}
        self.num_vertices = 0

        
    def neighbors(self,vertex):
        return []    

    def add_vertex(self,vertex):
        self.num_vertices += 1
        self.data[vertex] = self.neighbors(vertex)
        
    def remove_vertex(self, vertex):
        pass    

    def add_edge(self, pointA, pointB):
        pass

    def remove_edge(self, pointA, pointB):
        pass  

    def adjacent(self, pointA, pointB):
        return False