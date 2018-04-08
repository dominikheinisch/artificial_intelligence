import numpy as np

from csp.solvers.graph_coloring_solver import GraphColoringSolver


# solves graph coloring problem for grid graph L(2,1) using backtracking
class GraphForwardSolver(GraphColoringSolver):
    def __init__(self, *args):
        super(GraphForwardSolver, self).__init__(*args)
        self.min_distance = -1

    def solve(self):
        self.solve_backtracking()

    def solve_backtracking(self):
        while not self.nodes_values_results:
            nodes_values = np.zeros(shape=self.nodes_size, dtype=np.int8) + self.DEFAULT_VALUE
            self.values_in_use_size += 1
            if self.calc_all_possible_results:
                self.solve_all_backtracking_rec(0, np.copy(nodes_values))
            else:
                self.solve_backtracking_rec(0, np.copy(nodes_values))

    def solve_backtracking_rec(self):
        pass

    def adjacent_agreement(self, n, nodes_values):
        no_conflict = self.negated_adjacency_matrix[n] * (nodes_values[n] - self.DEFAULT_VALUE)
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
        self.values_in_use_size = 0
        self.double_adjacent_matrix = double_adjacent_matrix
        self.negate_double_adjacent_matrix = np.logical_not(double_adjacent_matrix)

    def check_conflicts(self, n, nodes_values):
        return self.adjacent_agreement(n, nodes_values) and self.double_adjacent_agreement(n, nodes_values)

    def double_adjacent_agreement(self, n, nodes_values):
        no_conflict = self.negate_double_adjacent_matrix[n] * (nodes_values[n] + 1)
        return np.min(np.absolute(np.multiply(self.double_adjacent_matrix[n], nodes_values)
                                  + no_conflict - nodes_values[n])) > 0

    def solve_backtracking_rec(self, node, nodes_values):
        if node == self.nodes_size:
            self.nodes_values = nodes_values
            self.nodes_values_results.append(list(nodes_values))
            return True
        for c in range(self.values_in_use_size):
            temp = nodes_values[node]
            nodes_values[node] = c
            if self.check_conflicts(node, nodes_values) and \
                    self.solve_backtracking_rec(node + 1, np.copy(nodes_values)):
                return True
            nodes_values[node] = temp
        return False

    def solve_all_backtracking_rec(self, node, nodes_values):
        if node == self.nodes_size:
            self.nodes_values = nodes_values
            self.nodes_values_results.append(list(nodes_values))
        for c in range(self.values_in_use_size):
            if node < self.nodes_size:
                nodes_values[node] = c
                if self.check_conflicts(node, nodes_values):
                    self.solve_all_backtracking_rec(node + 1, np.copy(nodes_values))
        return False