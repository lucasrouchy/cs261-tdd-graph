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
        
    def neighbors(self, vertex):
        if vertex in self.data:
            return self.data[vertex]
        return []
    def add_vertex(self, vertex):
        if vertex in self.data:
            return
        self.data[vertex]=[]
    def remove_vertex(self,vertex):
        pass
    def add_edge(self, A, B):
        pass
    def remove_edge(self, A, B):
        pass
    
        
