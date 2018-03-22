import numpy as np
import time


# solves graph coloring problem for grid graph L(2,1)
class GraphColoringSolver(object):
    DEFAULT_VALUE = -1

    def __init__(self, side, adjacency_matrix):
        self.side = side
        self.nodes_size = side * side
        self.nodes_values = np.zeros(shape=self.nodes_size, dtype=np.int8) + self.DEFAULT_VALUE
        self.adjacency_matrix = adjacency_matrix
        self.colors_in_use_size = -1
        self.simulation_time = -1
        self.nodes_values_results = []

    def run(self):
        start = time.time()
        self.solve()
        end = time.time()
        self.simulation_time = end - start

    def solve(self):
        pass

    def check_conflicts(self, n, nodes_values):
        pass

    def check_given_colors(self, given_colors):
        res = True
        i = 0
        while res and i < self.nodes_size:
            res = self.check_conflicts(i, given_colors)
            i += 1
        return res
