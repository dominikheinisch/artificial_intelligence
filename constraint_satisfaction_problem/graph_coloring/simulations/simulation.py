from enum import Enum

from constraint_satisfaction_problem.graph_coloring import generate_grid_graph
from constraint_satisfaction_problem.graph_coloring import GraphColoringBacktracking
from constraint_satisfaction_problem.graph_coloring import print_grid_graph


class SolutionType(Enum):
    FORWARD_CHECKING = 1
    BACKTRACKING = 2


class Simulation(object):
    SIDE = 3

    def __init__(self, side=SIDE):
        self.side = side

    def run(self):
        adjacency_matrix = generate_grid_graph(self.side)
        gc = GraphColoringBacktracking(self.side, adjacency_matrix)
        gc.run()
        print(gc.nodes_colors)
        print_grid_graph(gc.adjacency_matrix.tolist(), (gc.nodes_colors / 2 + 1))
        return gc.min_colors_size, gc.nodes_colors, gc.simulation_time
