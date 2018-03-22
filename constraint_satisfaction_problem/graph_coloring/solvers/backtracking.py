import numpy as np

from constraint_satisfaction_problem.graph_coloring.solvers.graph_coloring_solver import GraphColoringSolver


class GraphBacktrackingSolver(GraphColoringSolver):
    def __init__(self, *args):
        super(GraphBacktrackingSolver, self).__init__(*args)
        self.min_distance = -1

    def solve(self):
        self.solve_backtracking()

    def solve_backtracking(self):
        while np.amin(self.nodes_values) == self.DEFAULT_VALUE:
            nodes_values = np.zeros(shape=self.nodes_size, dtype=np.int8) + self.DEFAULT_VALUE
            self.colors_in_use_size += 1
            self.solve_backtracking_rec(0, np.copy(nodes_values))
            print('colors_in_use_size:', self.colors_in_use_size)

    def solve_backtracking_rec(self):
        pass

    def adjacent_agreement(self, n, nodes_values):
        no_conflict = np.logical_not(self.adjacency_matrix[n]) * (nodes_values[n] - self.DEFAULT_VALUE)
        return np.min(np.absolute(np.multiply(self.adjacency_matrix[n], nodes_values)
                                  + no_conflict - nodes_values[n])) > self.min_distance


# solves graph coloring problem for grid graph L(2,1) using backtracking
class GraphColoringBacktracking(GraphBacktrackingSolver):
    # default value == -2, to ensure correct calculations for L(2,1) graph coloring
    DEFAULT_COLOR = -2

    def __init__(self, double_adjacent_matrix, *args):
        self.DEFAULT_VALUE = self.DEFAULT_COLOR
        super(GraphColoringBacktracking, self).__init__(*args)
        self.min_distance = 1
        self.colors_in_use_size = 0
        self.double_adjacent_matrix = double_adjacent_matrix

    def check_conflicts(self, n, nodes_values):
        return self.adjacent_agreement(n, nodes_values) and self.double_adjacent_agreement(n, nodes_values)

    def double_adjacent_agreement(self, n, nodes_values):
        no_conflict = np.logical_not(self.double_adjacent_matrix[n]) * (nodes_values[n] + 1)
        return np.min(np.absolute(np.multiply(self.double_adjacent_matrix[n], nodes_values)
                                  + no_conflict - nodes_values[n])) > 0

    # def solve_backtracking_rec(self, node, nodes_values):
    #     if node == self.nodes_size:
    #         self.nodes_values = nodes_values
    #         self.nodes_values_results.append(list(nodes_values))
    #         return True
    #     for c in range(self.colors_in_use_size):
    #         temp = nodes_values[node]
    #         nodes_values[node] = c
    #         if self.check_conflicts(node, nodes_values) and self.solve_backtracking_rec(node + 1, np.copy(nodes_values)):
    #             return True
    #         nodes_values[node] = temp
    #     return False

    def solve_backtracking_rec(self, node, nodes_values):
        if node == self.nodes_size:
            self.nodes_values = nodes_values
            self.nodes_values_results.append(list(nodes_values))
        for c in range(self.colors_in_use_size):
            if node < self.nodes_size:
                nodes_values[node] = c
                if self.check_conflicts(node, nodes_values):
                    self.solve_backtracking_rec(node + 1, np.copy(nodes_values))
        return False


class LatinSquareBacktracking(GraphBacktrackingSolver):
    def __init__(self, *args):
        super(LatinSquareBacktracking, self).__init__(*args)
        self.min_distance = 0
        self.colors_in_use_size = self.side - 1

    def check_conflicts(self, n, nodes_values):
        return self.adjacent_agreement(n, nodes_values)

    def solve_backtracking_rec(self, node, nodes_values):
        if node == self.nodes_size:
            self.nodes_values = nodes_values
            self.nodes_values_results.append(list(nodes_values))
        for c in range(self.colors_in_use_size):
            if node < self.nodes_size:
                nodes_values[node] = c
                if self.check_conflicts(node, nodes_values):
                    self.solve_backtracking_rec(node + 1, np.copy(nodes_values))
        return False
