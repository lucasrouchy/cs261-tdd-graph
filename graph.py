# Graph: An efficient graph.
# A graph implementation that uses an adjacency list to represent vertices
# and edges.
# Your implementation should pass the tests in test_graph.py.
# YOUR NAME

import functools

class Graph:
    def __init__(self):
        self.data = dict()
   
    def adjacent(self, A, B):
        if len(self.data) <=1:
            return False
        if B in self.data[A]:
            return True

        
    def neighbors(self, vertex):
        if vertex in self.data:
            return self.data[vertex]
        return []
    def add_vertex(self, vertex):
        if vertex in self.data:
            return
        self.data[vertex]=[]
        try:
            test = self.data[vertex]
        except KeyError:
            self.data[vertex] = []

    def remove_vertex(self,vertex):
        if vertex in self.data:
            self._remove_vertex(vertex)
            self.data.pop(vertex)
    def add_edge(self, A, B):
        pass
    def remove_edge(self, A, B):
        pass
    def _remove_vertex(self, vertex):
        for neighbor in self.neighbors(vertex):
            if vertex in self.neighbors(neighbor):
                self.neighbors(neighbor).remove(vertex)
    def _vertices(self, A, B):
        return A in self.data and B in self.data
    def _neighbor(self, A, B):
        return A in self.data[B] and B in self.data
        

