import matplotlib.pyplot as plt
import numpy as np

from csp.simulations import SimulationGraphColoring
from csp.simulations import SimulationLatinSquare
from csp.printers import result_printer
from csp.utils import data_saver
from csp.simulations import MultipleSimulation, SimulationType, SolutionType


if __name__ == "__main__":
    sim = MultipleSimulation(SimulationType.GRAPH_COLORING, SolutionType.BACKTRACKING, 3, 9, False, False)
    sim.run()

    # filename_coloring = 'graph_coloring'
    # filename_latin_square = 'latin_square'
    # filename = filename_coloring
    # min_side = 1
    # max_side = 9
    # results = np.empty(shape=(max_side - min_side, 3))
    # j = 0
    # for i in range(min_side, max_side):
    #     s = SimulationGraphColoring(i, filename_coloring + str(i), True, False)
    #     s.run()
    #     results[j] = s.get_results()
    #     print(results[j])
    #     data_saver.save(s.solver.nodes_values_results, filename + 'backtracking_all_results_' + str(i) + '.txt')
    #     print(s.solver.nodes_values_results)
    #     j += 1
    # data_saver.save(results, filename + '.txt')
    # print(results)
    #
    # sides = results[:, 0]
    # times = results[:, 1]
    # values_size = results[:, 2]
    # print(times)
    #
    # result_printer.print_results(filename=(filename + 'backtracking_all_results__.png'),
    #                              title=filename + ' - backtracking - all results',
    #                              sides=sides, times=times)
    #
    # result_printer.print_results_log(filename=(filename + 'backtracking_all_results__log.png'),
    #                                  title=filename + ' - backtracking - all results - log time scale',
    #                                  sides=sides, times=times)
    # plt.show()

    # results = []
    # for i in range(16, 17):
    #     s = SimulationLatinSquare(i, filename_latin_square + str(i), False, True)
    #     s.run()
    #     print("len", len(s.solver.nodes_values_results))
    #     r = s.get_results()
    #     results.append((i, s.get_results()))
    #     print(r)
    # data_saver.save(results, filename_latin_square + '.txt')
