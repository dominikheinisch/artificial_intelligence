from enum import Enum

from constraint_satisfaction_problem.graph_coloring import generate_adjacency_matrix_graph_coloring
from constraint_satisfaction_problem.graph_coloring import generate_double_adjacency_matrix_graph_coloring
from constraint_satisfaction_problem.graph_coloring import generate_adjacency_matrix_latin_square
from constraint_satisfaction_problem.graph_coloring import GraphColoringBacktracking
from constraint_satisfaction_problem.graph_coloring import LatinSquareBacktracking
from constraint_satisfaction_problem.graph_coloring import print_grid_graph


class SolutionType(Enum):
    FORWARD_CHECKING = 1
    BACKTRACKING = 2


class Simulation(object):
    SIDE = 3

    def __init__(self, side=SIDE):
        self.side = side
        self.adjacency_matrix = None
        self.solver = None

    def run(self):
        self.solver.run()
        print_grid_graph(self.solver.adjacency_matrix, (self.solver.nodes_colors + 1))
        return self.solver.colors_in_use_size, self.solver.nodes_colors, self.solver.simulation_time


class SimulationGraphColoring(Simulation):
    def __init__(self, *args):
        super(SimulationGraphColoring, self).__init__(*args)
        self.adjacency_matrix = generate_adjacency_matrix_graph_coloring(self.side)
        self.double_adjacent_matrix = generate_double_adjacency_matrix_graph_coloring(self.adjacency_matrix)
        self.solver = GraphColoringBacktracking(self.double_adjacent_matrix, self.side, self.adjacency_matrix)


class SimulationLatinSquare(Simulation):
    def __init__(self, *args):
        super(SimulationLatinSquare, self).__init__(*args)
        self.adjacency_matrix = generate_adjacency_matrix_latin_square(self.side)
        self.solver = LatinSquareBacktracking(self.side, self.adjacency_matrix)
