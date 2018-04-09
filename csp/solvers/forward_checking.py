import numpy as np

from csp.solvers.graph_coloring_solver import GraphColoringSolver


# solves graph coloring problem for grid graph L(2,1) using backtracking
class GraphForwardSolver(GraphColoringSolver):

    FORWARD_DEFAULT_VALUE = 0
    FORWARD_BANNED_VALUE = -1
    FORWARD_INSERTED_VALUE = 1

    def __init__(self, *args):
        super(GraphForwardSolver, self).__init__(*args)
        self.min_distance = -1
        self.values_in_use_size = 1

    def solve(self):
        self.solve_forward_checking()

    def solve_forward_checking(self):
        while not self.nodes_values_results:
            forward_matrix = np.zeros(shape=(self.values_in_use_size, self.nodes_size), dtype=np.int8) + self.FORWARD_DEFAULT_VALUE
            nodes_values = np.zeros(shape=self.nodes_size, dtype=np.int8) + self.DEFAULT_VALUE
            if self.calc_all_possible_results:
                self.solve_all_forward_checking_rec(0, np.copy(nodes_values), np.copy(forward_matrix))
            else:
                self.solve_forward_checking_rec(0, np.copy(nodes_values), np.copy(forward_matrix))
            self.values_in_use_size += 1
            # TODO remove
            # print("iter", self.values_in_use_size)


# solves graph coloring problem for grid graph L(2,1) using forward checking
class GraphColoringForward(GraphForwardSolver):

    def __init__(self, double_adjacent_matrix, *args):
        super(GraphColoringForward, self).__init__(*args)
        self.min_distance = 1
        self.double_min_distance = 0
        self.values_in_use_size = 0
        self.double_adjacent_matrix = double_adjacent_matrix
        self.negate_double_adjacent_matrix = np.logical_not(double_adjacent_matrix)
        self.temp = 0

    def remove_conflicts(self, n, value, forward_matrix):
        forward_matrix[:, n] += np.zeros(shape=(self.values_in_use_size), dtype=np.int8) + self.FORWARD_BANNED_VALUE
        self.remove_adjacency_conflits(n, value, forward_matrix)
        self.remove_double_adjacency_conflits(n, value, forward_matrix)
        forward_matrix[value, n] = self.FORWARD_INSERTED_VALUE
        # TODO remove
        # print("matr\n", forward_matrix, '\n')

    def remove_adjacency_conflits(self, n, value, forward_matrix):
        # values_size = forward_matrix.shape[0]
        row = np.copy(self.adjacency_matrix[n]) * self.FORWARD_BANNED_VALUE
        forward_matrix[value] += np.copy(row)
        if value > 0:
            forward_matrix[value - 1] += np.copy(row)
        if value < self.values_in_use_size - 1:
            forward_matrix[value + 1] += np.copy(row)


    def remove_double_adjacency_conflits(self, n, value, forward_matrix):
        double_adj_row = np.copy(self.double_adjacent_matrix[n]) * self.FORWARD_BANNED_VALUE
        forward_matrix[value] += double_adj_row

    def solve_forward_checking_rec(self, node, nodes_values, forward_matrix):
        if node == self.nodes_size:
            self.nodes_values = nodes_values
            self.nodes_values_results.append(list(nodes_values))
            return True
        for val in range(self.values_in_use_size):
            if forward_matrix[val, node] == self.FORWARD_DEFAULT_VALUE:
                temp = nodes_values[node]
                temp_row_min_1 = np.copy(forward_matrix[val - 1])
                temp_row = np.copy(forward_matrix[val])
                temp_row_plus_1 = np.copy(forward_matrix[(val + 1) if val < self.values_in_use_size - 1 else val])
                col = np.copy(forward_matrix[:, node])
                nodes_values[node] = val
                self.remove_conflicts(node, val, forward_matrix)
                if self.solve_forward_checking_rec(node + 1, np.copy(nodes_values), np.copy(forward_matrix)):
                    return True
                nodes_values[node] = temp
                forward_matrix[val - 1] = temp_row_min_1
                forward_matrix[val] = temp_row
                forward_matrix[(val + 1) if val < self.values_in_use_size - 1 else val] = temp_row_plus_1
                forward_matrix[:, node] = col
        return False

    def solve_all_forward_checking_rec(self, node, nodes_values, forward_matrix):
        if node == self.nodes_size:
            self.nodes_values = nodes_values
            self.nodes_values_results.append(list(nodes_values))
            return
        for val in range(self.values_in_use_size):
            if forward_matrix[val, node] == self.FORWARD_DEFAULT_VALUE:
                temp = nodes_values[node]
                temp_row_min_1 = np.copy(forward_matrix[val - 1])
                temp_row = np.copy(forward_matrix[val])
                temp_row_plus_1 = np.copy(forward_matrix[(val + 1) if val < self.values_in_use_size - 1 else val])
                col = np.copy(forward_matrix[:, node])
                nodes_values[node] = val
                self.remove_conflicts(node, val, forward_matrix)
                self.solve_all_forward_checking_rec(node + 1, np.copy(nodes_values), np.copy(forward_matrix))
                nodes_values[node] = temp
                forward_matrix[val - 1] = temp_row_min_1
                forward_matrix[val] = temp_row
                forward_matrix[(val + 1) if val < self.values_in_use_size - 1 else val] = temp_row_plus_1
                forward_matrix[:, node] = col
        return


    def calc_curr_index(self,i):
        return -2 * i % 2 + i


    def solve_all_forward_checking_heuristic_rec(self, node, nodes_values):
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
