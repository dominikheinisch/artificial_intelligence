import matplotlib.pyplot as plt
import numpy as np
from enum import Enum

from csp.simulations import SolutionType
from csp.simulations import SimulationGraphColoring
from csp.simulations import SimulationLatinSquare
from csp.printers import result_printer
from csp.utils import data_saver


class SimulationType(Enum):

    GRAPH_COLORING = 1
    LATIN_SQUARE = 2


class MultipleSimulation():

    FILENAME_COLORING = 'graph_coloring'
    FILENAME_LATIN_SQUARE = 'latin_square'

    def __init__(self, simulation_type, solution_type, min_side, max_side, calc_all_possible_results=False, plot=False):
        self.simulation_type = simulation_type
        self.solution_type = solution_type
        if simulation_type == SimulationType.GRAPH_COLORING:
            self.filename = self.FILENAME_COLORING
        elif simulation_type == SimulationType.LATIN_SQUARE:
            self.filename = self.FILENAME_LATIN_SQUARE
        self.min_side = min_side
        self.max_side = max_side
        self.calc_all_possible_results = calc_all_possible_results
        self.plot = plot
        if solution_type == SolutionType.BACKTRACKING:
            self.print_message = "_backtracking"
            self.plot_mesaage = " - backtracking"
        elif solution_type == SolutionType.FORWARD_CHECKING:
            self.print_message = "_forward_checking"
            self.plot_mesaage = " - _forward checking"
        if calc_all_possible_results:
            self.print_message += "_all_results_"
            self.plot_mesaage += " - all results"
        else:
            self.print_message += "_first_result_"
            self.plot_mesaage += " - first result"

    def run(self):
        results = np.empty(shape=(self.max_side - self.min_side, 4))
        j = 0
        for i in range(self.min_side, self.max_side):
            if self.simulation_type == SimulationType.GRAPH_COLORING:
                s = SimulationGraphColoring(i, self.filename + str(i), self.calc_all_possible_results, self.plot)
            elif self.simulation_type == SimulationType.FILENAME_LATIN_SQUARE:
                s = SimulationLatinSquare(i, self.filename + str(i), self.calc_all_possible_results, self.plot)
            s.run()
            results[j] = s.get_results()
            data_saver.save(s.solver.nodes_values_results, self.filename +
                            'backtracking_all_results_' + str(i) + '.txt')
            j += 1
        data_saver.save(results, self.filename + '.txt')
        print(results)

        sides = results[:, 0]
        times = results[:, 1]
        values_size = results[:, 2]
        print(times)

        result_printer.print_results(filename=(self.filename + self.print_message + '.png'),
                                     title=self.filename + self.plot_mesaage,
                                     sides=sides, times=times)

        result_printer.print_results_log(filename=(self.filename + self.print_message + 'log.png'),
                                         title=self.filename + self.plot_mesaage + ' - log time scale',
                                         sides=sides, times=times)
        plt.show()
