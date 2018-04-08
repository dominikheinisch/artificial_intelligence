import matplotlib.pyplot as plt
import numpy as np
from enum import Enum

from csp.simulations import SimulationGraphColoring
from csp.simulations import SimulationLatinSquare
from csp.printers import result_printer
from csp.utils import data_saver


class SimulationType(Enum):

    GRAPH_COLORING = 1
    LATIN_SQUARE = 2


class SolutionType(Enum):

    BACKTRACKING = 1
    FORWARD_CHECKING = 2


class MultipleSimulation:

    def __init__(self, simulation_type, solution_type, min_side, max_side, calc_all_possible_results=False, plot=False):
        self.simulation_type = simulation_type
        self.solution_type = solution_type
        self.min_side = min_side
        self.max_side = max_side
        self.calc_all_possible_results = calc_all_possible_results
        self.plot = plot
        if simulation_type == SimulationType.GRAPH_COLORING:
            self.filename = 'graph_coloring'
        elif simulation_type == SimulationType.LATIN_SQUARE:
            self.filename = 'latin_square'
        self.plot_message = self.filename
        if solution_type == SolutionType.BACKTRACKING:
            self.filename += "_backtracking"
            self.plot_message += " - backtracking"
        elif solution_type == SolutionType.FORWARD_CHECKING:
            self.filename += "_forward_checking"
            self.plot_message += " - _forward checking"
        if calc_all_possible_results:
            self.filename += "_all_results_"
            self.plot_message += " - all results"
        else:
            self.filename += "_first_result_"
            self.plot_message += " - first result"

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
            data_saver.save(s.solver.nodes_values_results, self.filename + str(i) + '.txt')
            j += 1
        data_saver.save(results, self.filename + '.txt')
        print(results)

        sides = results[:, 0]
        times = results[:, 1]
        possible_results = results[:, 3]
        result_printer.print_results(filename=(self.filename + '.png'),
                                     title=self.plot_message,
                                     sides=sides, times=times)

        result_printer.print_results_log(filename=(self.filename + 'log.png'),
                                         title=self.plot_message + ' - log time scale',
                                         sides=sides, times=times)
        if self.calc_all_possible_results:
            result_printer.print_possible_results(filename=(self.filename + '_possibilities.png'),
                                                  title=self.plot_message+ ' - possibilities',
                                                  sides=sides, results=possible_results)
        plt.show()
