import numpy as np
import time

from constraint_satisfaction_problem.graph_coloring.solvers.graph_coloring_solver import GraphColoringSolver


# solves graph coloring problem for grid graph L(2,1) using backtracking
class GraphColoringBacktracking(GraphColoringSolver):

    def __init__(self, *args):
        super(GraphColoringBacktracking, self).__init__(*args)

    def solve(self):
        self.solve_backtracking()

    def solve_backtracking(self):
        min_colors_size = 0
        while np.amin(self.nodes_colors) == -2:
            nodes_colors = np.zeros(shape=self.nodes_size) + self.DEFAULT_COLOR
            min_colors_size += 1
            self.solve_backtracking_rec(0, min_colors_size, np.copy(nodes_colors))
            print('min_colors_size:', min_colors_size)
        self.min_colors_size = min_colors_size

    def solve_backtracking_rec(self, node, min_colors_size, nodes_colors):
        if node == self.nodes_size:
            self.nodes_colors = nodes_colors
            return True
        for c in range(min_colors_size):
            temp = nodes_colors[node]
            nodes_colors[node] = c
            if self.check_conflicts(node, nodes_colors):
                if self.solve_backtracking_rec(node + 1, min_colors_size, nodes_colors):
                    return True
            nodes_colors[node] = temp
        return False
