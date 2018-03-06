import numpy as np

from genetic_algorithm import data_loader
from genetic_algorithm.solvers import Population
from genetic_algorithm.solvers import SelectionType


class Simulation(object):
    POPULATIONS = 100
    GENERATIONS = 100
    PROBABILITY_BECOME_PARENT = 0.8
    PROBABILITY_DRAW = 1 - PROBABILITY_BECOME_PARENT
    PROBABILITY_MUTATE = 0.4
    TOURNAMENT_SIZE = 10

    def __init__(self, filename, pop_size=POPULATIONS, gen_size=GENERATIONS, prob_cross=PROBABILITY_BECOME_PARENT,
                 prob_mutate=PROBABILITY_MUTATE, save_best=False, selection_type=SelectionType.ROULETTE_TYPE,
                 tournament_size=TOURNAMENT_SIZE):
        self.n, self.m_flow, self.m_dist = data_loader.load(filename)
        self.filename = filename
        self.pop_size = pop_size
        self.gen_size = gen_size
        self.prob_cross = prob_cross
        self.prob_mutate = prob_mutate
        self.save_best = save_best
        self.list_populations = []
        self.list_results = np.empty(shape=(gen_size, 3))
        self.selection_type = selection_type
        self.tournament_size = tournament_size

    def run(self):
        self.list_populations = []
        self.list_populations.append(Population(n=self.n, m_flow=self.m_flow, m_dist=self.m_dist,
                                                pop_size=self.pop_size, prob_cross=self.prob_cross,
                                                prob_mutate=self.prob_mutate, save_best=self.save_best,
                                                selection_type=self.selection_type,
                                                tournament_size=self.tournament_size))
        self.list_populations[0].init_random_phenotypes()
        self.list_populations[0].calc_cost_fitness_results()
        self.update_results(0)

        for i in range(1, self.gen_size):
            self.list_populations.append(self.list_populations[i - 1].get_next_population())
            self.list_populations[i].calc_cost_fitness_results()
            self.update_results(i)
        return self.list_results

    def update_results(self, no_iter):
        self.list_results[no_iter] = self.list_populations[no_iter].get_result()
