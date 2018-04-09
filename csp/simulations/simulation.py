from enum import Enum

from csp.generators import generate_adjacency_matrix_graph_coloring
from csp.generators import generate_double_adjacency_matrix_graph_coloring
from csp.generators import generate_adjacency_matrix_latin_square
from csp.solvers import GraphColoringBacktracking, GraphColoringForward
from csp.solvers import LatinSquareBacktracking, LatinSquareForward
from csp.printers import grid_graph_printer


class SolutionType(Enum):

    BACKTRACKING = 1
    FORWARD_CHECKING = 2


class Simulation:
    SIDE = 3
    FILENAME = 'graph'

    def __init__(self, side=SIDE, filename=FILENAME, solution_type=SolutionType.BACKTRACKING, calc_all_possible_results=False, plot=False):
        self.side = side
        self.filename = filename
        self.solution_type = solution_type
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

    def get_nodes_values_results(self):
        return self.solver.get_nodes_values_results()


class SimulationGraphColoring(Simulation):
    def __init__(self, *args):
        super(SimulationGraphColoring, self).__init__(*args)
        self.adjacency_matrix = generate_adjacency_matrix_graph_coloring(self.side)
        self.double_adjacent_matrix = generate_double_adjacency_matrix_graph_coloring(self.adjacency_matrix)
        if self.solution_type == SolutionType.BACKTRACKING:
            self.solver = GraphColoringBacktracking(self.double_adjacent_matrix, self.side, self.adjacency_matrix,
                                                    self.calc_all_possible_results)
        elif self.solution_type == SolutionType.FORWARD_CHECKING:
            self.solver = GraphColoringForward(self.double_adjacent_matrix, self.side, self.adjacency_matrix,
                                                    self.calc_all_possible_results)


class SimulationLatinSquare(Simulation):
    def __init__(self, *args):
        super(SimulationLatinSquare, self).__init__(*args)
        self.adjacency_matrix = generate_adjacency_matrix_latin_square(self.side)
        # if self.solution_type == SolutionType.BACKTRACKING:
        #     self.solver = LatinSquareBacktracking(self.side, self.adjacency_matrix, self.calc_all_possible_results)
        # elif self.solution_type == SolutionType.FORWARD_CHECKING:
        #     self.solver = LatinSquareForward(self.side, self.adjacency_matrix, self.calc_all_possible_results)
        print(self.solution_type)
        self.solver = LatinSquareForward(self.side, self.adjacency_matrix, self.calc_all_possible_results)