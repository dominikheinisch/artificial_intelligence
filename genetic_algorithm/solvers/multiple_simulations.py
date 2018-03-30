import numpy as np

from genetic_algorithm.solvers import Simulation
from genetic_algorithm.solvers import SelectionType
from genetic_algorithm import data_saver


class MultipleSimulation(Simulation):
    ITERATIONS_SIZE = 10

    def __init__(self, filename, result_filename, gen_size, no_iter=NO_ITERATIONS,
                 selection_type=SelectionType.ROULETTE_TYPE,
                 tournament_size=Simulation.TOURNAMENT_SIZE, *args, **kwargs):
        super(MultipleSimulation, self).__init__(filename=filename, gen_size=gen_size, *args, **kwargs)
        self.no_iter = no_iter
        self.arr_results = np.empty(shape=(gen_size, 3, no_iter))
        self.results_min_avg_max_std = np.empty(shape=(self.gen_size, 6))
        self.result_filename = result_filename
        self.selection_type = selection_type
        self.tournament_size = tournament_size

    def run(self):
        simulation = Simulation(self.filename, pop_size=self.pop_size, gen_size=self.gen_size,
                                prob_cross=self.prob_cross, prob_mutate=self.prob_mutate, save_best=False,
                                selection_type=self.selection_type, tournament_size=self.tournament_size)
        simulation.run()
        self.arr_results[:, :, 0] = simulation.list_results
        for i in range(1, self.no_iter):
            simulation.run()
            self.arr_results[:, :, i] = simulation.list_results
        print(self.arr_results)
        min_avg_max = np.sum(self.arr_results, axis=2) / self.no_iter
        std = np.std(self.arr_results, axis=2)
        self.results_min_avg_max_std[:, :3] = min_avg_max
        self.results_min_avg_max_std[:, 3:] = std
        self.results_min_avg_max_std = self.results_min_avg_max_std[:, np.array([0, 3, 1, 4, 2, 5])]
        data_saver.save(result=self.results_min_avg_max_std, filename=self.result_filename)

    def update_results(self, no_iter):
        self.list_results[no_iter] = self.list_populations[no_iter].get_result()



