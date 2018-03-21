import numpy as np

from constraint_satisfaction_problem.graph_coloring.solvers.graph_coloring_solver import GraphColoringSolver


class GraphBacktrackingSolver(GraphColoringSolver):
    def __init__(self, *args):
        super(GraphBacktrackingSolver, self).__init__(*args)
        self.min_distance = -1
        self.list_results = []

    def solve(self):
        self.solve_backtracking()

    def solve_backtracking(self):
        colors_in_use_size = self.colors_in_use_size
        while np.amin(self.nodes_colors) == -2:
            nodes_colors = np.zeros(shape=self.nodes_size, dtype=np.int8) + self.DEFAULT_COLOR
            colors_in_use_size += 1
            self.solve_backtracking_rec(0, colors_in_use_size, np.copy(nodes_colors))
            print('colors_in_use_size:', colors_in_use_size)
        self.colors_in_use_size = colors_in_use_size
        print(self.list_results)

    def adjacent_agreement(self, n, nodes_colors):
        no_conflict = np.logical_not(self.adjacency_matrix[n]) * (nodes_colors[n] + 2)
        return np.min(np.absolute(np.multiply(self.adjacency_matrix[n], nodes_colors)
                                  + no_conflict - nodes_colors[n])) > self.min_distance


# solves graph coloring problem for grid graph L(2,1) using backtracking
class GraphColoringBacktracking(GraphBacktrackingSolver):
    def __init__(self, double_adjacent_matrix, *args):
        super(GraphColoringBacktracking, self).__init__(*args)
        self.min_distance = 1
        self.colors_in_use_size = 0
        self.double_adjacent_matrix = double_adjacent_matrix

    def check_conflicts(self, n, nodes_colors):
        return self.adjacent_agreement(n, nodes_colors) and self.double_adjacent_agreement(n, nodes_colors)

    def double_adjacent_agreement(self, n, nodes_colors):
        no_conflict = np.logical_not(self.double_adjacent_matrix[n]) * (nodes_colors[n] + 1)
        return np.min(np.absolute(np.multiply(self.double_adjacent_matrix[n], nodes_colors)
                                  + no_conflict - nodes_colors[n])) > 0

    def solve_backtracking_rec(self, node, colors_in_use_size, nodes_colors):
        if node == self.nodes_size:
            self.nodes_colors = nodes_colors
            return True
        for c in range(colors_in_use_size):
            temp = nodes_colors[node]
            nodes_colors[node] = c
            if self.check_conflicts(node, nodes_colors):
                if self.solve_backtracking_rec(node + 1, colors_in_use_size, nodes_colors):
                    return True
            nodes_colors[node] = temp
        return False


class LatinSquareBacktracking(GraphBacktrackingSolver):
    def __init__(self, *args):
        super(LatinSquareBacktracking, self).__init__(*args)
        self.min_distance = 0
        self.colors_in_use_size = self.side - 1

    def check_conflicts(self, n, nodes_colors):
        return self.adjacent_agreement(n, nodes_colors)

    def solve_backtracking_rec(self, node, colors_in_use_size, nodes_colors):
        # print(nodes_colors)
        if node == self.nodes_size:
            self.nodes_colors = nodes_colors
            # TODO
            self.list_results.append(list(nodes_colors))
            # TODO
            # return True
        for c in range(colors_in_use_size):
            # TODO
            if node < self.nodes_size:
                temp = nodes_colors[node]
                nodes_colors[node] = c
                # TODO
                if self.check_conflicts(node, nodes_colors):
                    if self.solve_backtracking_rec(node + 1, colors_in_use_size, nodes_colors):
                    # TODO
                        # return True
                        pass
                    # TODO
                else:
                    nodes_colors[node] = temp
        return False