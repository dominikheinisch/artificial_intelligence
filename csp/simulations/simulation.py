from enum import Enum

from csp.generators import generate_adjacency_matrix_graph_coloring
from csp.generators import generate_double_adjacency_matrix_graph_coloring
from csp.generators import generate_adjacency_matrix_latin_square
from csp.solvers import GraphColoringBacktracking
from csp.solvers import LatinSquareBacktracking
from csp.printers import grid_graph_printer


class SolutionType(Enum):
    FORWARD_CHECKING = 1
    BACKTRACKING = 2


class Simulation(object):
    SIDE = 3
    FILENAME = 'graph'

    def __init__(self, side=SIDE, filename=FILENAME, calc_all_possible_results=False, plot=False):
        self.side = side
        self.filename = filename
        self.adjacency_matrix = None
        self.solver = None
        self.calc_all_possible_results = calc_all_possible_results
        self.plot = plot

    def run(self):
        self.solver.run()
        if self.plot:
            grid_graph_printer.print_grid_graph(self.filename, self.solver.adjacency_matrix, (self.solver.nodes_values + 1))

    def get_results(self):
        return self.solver.get_solving_results()


class SimulationGraphColoring(Simulation):
    def __init__(self, *args):
        super(SimulationGraphColoring, self).__init__(*args)
        self.adjacency_matrix = generate_adjacency_matrix_graph_coloring(self.side)
        self.double_adjacent_matrix = generate_double_adjacency_matrix_graph_coloring(self.adjacency_matrix)
        self.solver = GraphColoringBacktracking(self.double_adjacent_matrix, self.side, self.adjacency_matrix,
                                                self.calc_all_possible_results)


class SimulationLatinSquare(Simulation):
    def __init__(self, *args):
        super(SimulationLatinSquare, self).__init__(*args)
        self.adjacency_matrix = generate_adjacency_matrix_latin_square(self.side)
        self.solver = LatinSquareBacktracking(self.side, self.adjacency_matrix, self.calc_all_possible_results)