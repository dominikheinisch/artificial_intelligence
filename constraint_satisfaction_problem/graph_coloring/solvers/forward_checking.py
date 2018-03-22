import numpy as np
import time

from constraint_satisfaction_problem.graph_coloring.solvers.graph_coloring_solver import GraphColoringSolver


# solves graph coloring problem for grid graph L(2,1) using backtracking
class GraphBacktrackingSolver(GraphColoringSolver):
    def __init__(self, *args):
        super(GraphBacktrackingSolver, self).__init__(*args)
        self.nodes_values_two_dim = None

    def solve(self):
        self.solve_forward_checking()

    def solve_forward_checking(self):
        colors_in_use_size = 0
        while np.amin(self.nodes_values) == -2:
            nodes_values = np.zeros(shape=self.nodes_size) + self.DEFAULT_VALUE
            colors_in_use_size += 1
            self.nodes_values_two_dim = np.zeros(shape=(self.nodes_size, colors_in_use_size))
            self.solve_forward_checking_rec(0, colors_in_use_size, np.copy(nodes_values))
            print('colors_in_use_size:', colors_in_use_size)
        self.colors_in_use_size = colors_in_use_size

    def solve_forward_checking_rec(self, node, colors_in_use_size, nodes_values):
        if node == self.nodes_size:
            self.nodes_values = nodes_values
            return True
        for c in range(colors_in_use_size):
            temp = nodes_values[node]
            nodes_values[node] = c
            if self.check_conflicts(node, nodes_values):
                if self.solve_forward_checking_rec(node + 1, colors_in_use_size, nodes_values):
                    return True
            nodes_values[node] = temp
        return False
