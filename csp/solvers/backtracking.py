import numpy as np

from csp.solvers.graph_coloring_solver import GraphColoringSolver


class GraphBacktrackingSolver(GraphColoringSolver):
    def __init__(self, *args):
        super(GraphBacktrackingSolver, self).__init__(*args)
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
        self.double_min_distance = 0
        self.values_in_use_size = 0
        self.double_adjacent_matrix = double_adjacent_matrix
        self.negate_double_adjacent_matrix = np.logical_not(double_adjacent_matrix)

    def check_conflicts(self, n, nodes_values):
        return self.adjacent_agreement(n, nodes_values) and self.double_adjacent_agreement(n, nodes_values)

    def double_adjacent_agreement(self, n, nodes_values):
        no_conflict = self.negate_double_adjacent_matrix[n] * (nodes_values[n] + 1)
        return np.min(np.absolute(np.multiply(self.double_adjacent_matrix[n], nodes_values)
                                  + no_conflict - nodes_values[n])) > self.double_min_distance

    def solve_backtracking_rec(self, node, nodes_values):
        if node == self.nodes_size:
            self.nodes_values = nodes_values
            self.nodes_values_results.append(list(nodes_values))
            return True
        for c in range(self.values_in_use_size):
            temp = nodes_values[node]
            nodes_values[node] = c
            if self.check_conflicts(node, nodes_values) and \
                    self.solve_backtracking_rec(node + 1, nodes_values):
                return True
            nodes_values[node] = temp
        return False

    def solve_all_backtracking_rec(self, node, nodes_values):
        if node == self.nodes_size:
            self.nodes_values = nodes_values
            self.nodes_values_results.append(list(nodes_values))
            return
        for c in range(self.values_in_use_size):
            if node < self.nodes_size:
                temp = nodes_values[node]
                nodes_values[node] = c
                if self.check_conflicts(node, nodes_values):
                    self.solve_all_backtracking_rec(node + 1, nodes_values)
            nodes_values[node] = temp
        return


# solves latin square completing problem
class LatinSquareBacktracking(GraphBacktrackingSolver):
    def __init__(self, *args):
        super(LatinSquareBacktracking, self).__init__(*args)
        self.min_distance = 0
        self.values_in_use_size = self.side - 1

    def check_conflicts(self, n, nodes_values):
        return self.adjacent_agreement(n, nodes_values)

    def solve_backtracking_rec(self, i):
        if i == self.nodes_size:
            self.nodes_values = self.nodes_values
            self.nodes_values_results.append(list(self.nodes_values))
            return True
        for c in range(self.values_in_use_size):
            self.nodes_values[i] = c
            if self.check_conflicts(i, self.nodes_values) and self.solve_backtracking_rec(i + 1):
                return True
            self.nodes_values[i] = self.DEFAULT_VALUE
        return False

    def solve_all_backtracking_rec(self, i):
        if i == self.nodes_size:
            # self.nodes_values = self.nodes_values
            self.nodes_values_results.append(list(self.nodes_values))
            return
        for c in range(self.values_in_use_size):
            self.nodes_values[i] = c
            if self.check_conflicts(i, self.nodes_values):
                self.solve_all_backtracking_rec(i + 1)
            self.nodes_values[i] = self.DEFAULT_VALUE
        return

    def solve_backtracking(self):
        nodes_values = np.zeros(shape=self.nodes_size, dtype=np.int8) + self.DEFAULT_VALUE
        self.values_in_use_size = self.side
        if self.calc_all_possible_results:
            # self.solve_all_backtracking_rec(0, np.copy(nodes_values))
            self.solve_all_backtracking_rec(0)
        else:
            self.solve_backtracking_rec(0)
