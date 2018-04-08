import numpy as np

from csp.solvers.graph_coloring_solver import GraphColoringSolver


# solves graph coloring problem for grid graph L(2,1) using backtracking
class GraphForwardSolver(GraphColoringSolver):

    DEFAULT_VALUE = 0
    BANNED_VALUE = -1
    INSERTED_VALUE = 1

    def __init__(self, *args):
        super(GraphForwardSolver, self).__init__(*args)
        self.min_distance = -1
        self.values_in_use_size = 1
        self.forward_matrix = None

    def solve(self):
        self.solve_forward_checking()

    def solve_forward_checking(self):
        while not self.nodes_values_results:
            self.forward_matrix = np.zeros(shape=(self.nodes_size, self.values_in_use_size), dtype=np.int8) + self.DEFAULT_VALUE
            # nodes_values = np.zeros(shape=self.nodes_size, dtype=np.int8) + self.DEFAULT_VALUE
            if self.calc_all_possible_results:
                self.solve_all_forward_checking_rec(0)
            else:
                self.solve_forward_checking_rec(0)
            self.values_in_use_size += 1


# solves graph coloring problem for grid graph L(2,1) using forward checking
class GraphColoringForward(GraphForwardSolver):

    def __init__(self, double_adjacent_matrix, *args):
        super(GraphColoringForward, self).__init__(*args)
        self.min_distance = 1
        self.double_min_distance = 0
        self.values_in_use_size = 0
        self.double_adjacent_matrix = double_adjacent_matrix
        self.negate_double_adjacent_matrix = np.logical_not(double_adjacent_matrix)

    def remove_conflicts(self, n, nodes_values):
        self.remove_adjacency_conflits(n, nodes_values)
        self.remove_double_adjacency_conflits(n, nodes_values)

    def remove_adjacency_conflits(self, n, nodes_values):
        pass

    def remove_double_adjacency_conflits(self, n, nodes_values):
        pass

        # no_conflict = self.negate_double_adjacent_matrix[n] * (nodes_values[n] + 1)
        # return np.min(np.absolute(np.multiply(self.double_adjacent_matrix[n], nodes_values)
        #                           + no_conflict - nodes_values[n])) > self.double_min_distance

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