import numpy as np
import time


# solves graph coloring problem for grid graph L(2,1)
class GraphColoringSolver(object):
    DEFAULT_VALUE = -1

    def __init__(self, side, adjacency_matrix, calc_all_possible_results=False):
        self.side = side
        self.nodes_size = side * side
        self.nodes_values = np.zeros(shape=self.nodes_size, dtype=np.int8) + self.DEFAULT_VALUE
        self.adjacency_matrix = adjacency_matrix
        self.negated_adjacency_matrix = np.logical_not(adjacency_matrix)
        self.values_in_use_size = -1
        self.solving_time = -1
        self.nodes_values_results = []
        self.calc_all_possible_results = calc_all_possible_results

    def run(self):
        start = time.time()
        self.solve()
        end = time.time()
        self.solving_time = end - start

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

    def get_nodes_values_results(self):
        return self.nodes_values_results

    def get_solving_results(self):
        return np.asarray([self.side, self.solving_time, self.values_in_use_size])
