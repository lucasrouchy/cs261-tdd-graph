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
