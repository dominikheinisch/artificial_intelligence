import numpy as np
import time

from constraint_satisfaction_problem.graph_coloring.solvers.solution_type import SolutionType


# solves graph coloring problem for grid graph L(2,1)
class GraphColoring(object):

    DEFAULT_COLOR = -2

    def __init__(self, side, adjacency_matrix, solution_type=SolutionType.BACKTRACKING):
        self.solution_type = solution_type
        self.side = side
        self.nodes_size = side * side
        self.nodes_colors = np.zeros(shape=self.nodes_size) + self.DEFAULT_COLOR
        self.adjacency_matrix = adjacency_matrix
        self.double_adjacent_matrix = np.zeros(shape=(self.nodes_size, self.nodes_size))
        self.calc_double_adjacent_matrix()
        self.min_colors_size = -1
        self.simulation_time = -1

    def calc_double_adjacent_matrix(self):
        for row in range(self.nodes_size):
            for col in range(self.nodes_size):
                if self.adjacency_matrix[row][col]:
                    self.double_adjacent_matrix[row] = np.logical_or(self.double_adjacent_matrix[row],
                                                                     self.adjacency_matrix[col])
        np.fill_diagonal(self.double_adjacent_matrix, 0)

    def solve(self):
        if self.solution_type == SolutionType.BACKTRACKING:
            self.solve_backtracking()
        elif self.solution_type == SolutionType.FORWARD_CHECKING:
            self.solve_forward_checking()

    def solve_backtracking(self):
        start = time.time()
        min_colors_size = 0
        while np.amin(self.nodes_colors) == -2:
            nodes_colors = np.zeros(shape=self.nodes_size) + self.DEFAULT_COLOR
            min_colors_size += 1
            self.solve_backtracking_rec(0, min_colors_size, np.copy(nodes_colors))
            print('min_colors_size:', min_colors_size)
        self.min_colors_size = min_colors_size
        end = time.time()
        self.simulation_time = end - start

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

    def solve_forward_checking(self):
        start = time.time()
        min_colors_size = 0
        while np.amin(self.nodes_colors) == -2:
            nodes_colors = np.zeros(shape=self.nodes_size) + self.DEFAULT_COLOR
            min_colors_size += 1
            self.solve_backtracking_rec(0, min_colors_size, np.copy(nodes_colors))
            print('min_colors_size:', min_colors_size)
        self.min_colors_size = min_colors_size
        end = time.time()
        self.simulation_time = end - start
