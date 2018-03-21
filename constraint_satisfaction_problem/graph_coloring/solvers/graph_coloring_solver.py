import numpy as np
import time


# solves graph coloring problem for grid graph L(2,1)
class GraphColoringSolver(object):

    DEFAULT_COLOR = -2

    def __init__(self, side, adjacency_matrix):
        self.side = side
        self.nodes_size = side * side
        self.nodes_colors = np.zeros(shape=self.nodes_size) + self.DEFAULT_COLOR
        self.adjacency_matrix = adjacency_matrix
        self.double_adjacent_matrix = np.zeros(shape=(self.nodes_size, self.nodes_size))
        self.calc_double_adjacent_matrix()
        self.min_colors_size = -1
        self.simulation_time = -1

    def run(self):
        start = time.time()
        self.solve()
        end = time.time()
        self.simulation_time = end - start

    def solve(self):
        pass

    def calc_double_adjacent_matrix(self):
        for row in range(self.nodes_size):
            for col in range(self.nodes_size):
                if self.adjacency_matrix[row][col]:
                    self.double_adjacent_matrix[row] = np.logical_or(self.double_adjacent_matrix[row],
                                                                     self.adjacency_matrix[col])
        np.fill_diagonal(self.double_adjacent_matrix, 0)

    def check_conflicts(self, n, nodes_colors):
        return self.adjacent_agreement(n, nodes_colors) and self.double_adjacent_agreement(n, nodes_colors)

    def adjacent_agreement(self, n, nodes_colors):
        no_conflict = np.logical_not(self.adjacency_matrix[n]) * (nodes_colors[n] + 2)
        return np.min(np.absolute(np.multiply(self.adjacency_matrix[n], nodes_colors)
                                  + no_conflict - nodes_colors[n])) > 1

    def double_adjacent_agreement(self, n, nodes_colors):
        no_conflict = np.logical_not(self.double_adjacent_matrix[n]) * (nodes_colors[n] + 2)
        return np.min(np.absolute(np.multiply(self.double_adjacent_matrix[n], nodes_colors)
                                  + no_conflict - nodes_colors[n])) > 1

    def check_given_colors(self, given_colors):
        res = True
        i = 0
        while res and i < self.nodes_size:
            res = self.check_conflicts(i, given_colors)
            i += 1
        return res

