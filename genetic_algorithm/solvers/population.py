import numpy as np
import random
import copy
from enum import Enum

from genetic_algorithm.solvers import Phenotype


class SelectionType(Enum):
    TOURNAMENT_TYPE = 1
    ROULETTE_TYPE = 2


class Population(object):
    def __init__(self, n, m_flow, m_dist, pop_size, prob_cross, prob_mutate, save_best, selection_type,
                 tournament_size, phenotypes=None):
        self.n, self.matrix_flow, self.matrix_distance = n, m_flow, m_dist
        self.selection_type = selection_type
        self.tournament_size = tournament_size
        self.pop_size = pop_size
        self.prob_cross = prob_cross
        self.prob_mutate = prob_mutate
        self.phenotypes = phenotypes
        self.save_best = save_best
        self.new_phenotypes = []
        self.iter_costs = []
        self.prob_list = []
        self.iter_fitness = None
        self.min_cost = -1
        self.avg_cost = -1
        self.max_cost = -1
        self.best_phenotype = None
        self.no_children = int(prob_cross * self.pop_size)
        self.no_draw_parents = self.pop_size - self.no_children

    def init_random_phenotypes(self):
        self.phenotypes = []
        for i in range(self.pop_size):
            self.phenotypes.append(Phenotype(size=self.n,
                                             m_flow=self.matrix_flow,
                                             m_dist=self.matrix_distance))

    def calc_cost_fitness_results(self):
        self.calc_fitness_and_cost_fun()
        self.calc_results()

    def calc_fitness_and_cost_fun(self):
        self.iter_costs = []
        for i in range(self.pop_size):
            self.phenotypes[i].calc_fitness_and_cost_fun()
            self.iter_costs.append(self.phenotypes[i].val_cost_fun)
        iter_fitness = np.asarray(self.iter_costs)
        val_max = np.amax(iter_fitness) * 1.01
        temp = (val_max - iter_fitness) / val_max
        self.iter_fitness = np.multiply(np.multiply(val_max * temp, temp), temp)

    def calc_results(self):
        _len = len(self.iter_costs)
        self.min_cost = min(self.iter_costs)
        self.avg_cost = int(sum(list(map(lambda x: x/_len, self.iter_costs))))
        self.max_cost = max(self.iter_costs)
        self.best_phenotype = np.ndarray.tolist(list(filter(
            lambda x: x.val_cost_fun == min(self.iter_costs), self.phenotypes))[0].factories)

    def get_next_population(self):
        if self.save_best:
            self.best_phenotype = copy.copy(min(self.phenotypes, key=lambda x: x.val_cost_fun))
        self.calc_prob_list()
        self.selection_phenotypes_to_copy()
        self.crossover()
        self.mutate_rand()
        if self.save_best:
            self.new_phenotypes[0] = self.best_phenotype
        return Population(n=self.n, m_flow=self.matrix_flow, m_dist=self.matrix_distance, pop_size=self.pop_size,
                          prob_cross=self.prob_cross, prob_mutate=self.prob_mutate,
                          phenotypes=self.new_phenotypes, save_best=self.save_best, selection_type=self.selection_type,
                          tournament_size=self.tournament_size)

    def calc_prob_list(self):
        sum_val_fitness_fun = np.sum(self.iter_fitness)
        self.prob_list = self.iter_fitness / sum_val_fitness_fun

    def crossover(self):
        for i in range(self.no_children):
            index_arr = self.selection_indexes(2)
            self.new_phenotypes.append(self.phenotypes[index_arr[0]].crossover(self.phenotypes[index_arr[1]]))

    def selection_phenotypes_to_copy(self):
        for i in range(self.no_draw_parents):
            index_arr = self.selection_indexes(1)
            self.new_phenotypes.append(self.phenotypes[index_arr[0]])

    def mutate_rand(self):
        for i in range(self.no_draw_parents):
            if random.random() < self.prob_mutate:
                self.phenotypes[i].mutate()

    def get_result(self):
        return np.array([self.min_cost, self.avg_cost, self.max_cost])

    def selection_indexes(self, no_phenotypes):
        if self.selection_type == SelectionType.TOURNAMENT_TYPE:
            indexes = np.random.choice(self.pop_size, self.tournament_size * no_phenotypes)
            len_ = indexes.shape[0]
            costs = [(self.phenotypes[indexes[i]], indexes[i]) for i in range(len_)]
            costs.sort(key=lambda x: x[0].val_cost_fun)
            if no_phenotypes == 2:
                return [costs[0][1], costs[1][1]]
            else:
                return [costs[0][1]]
        elif self.selection_type == SelectionType.ROULETTE_TYPE:
            return np.random.choice(self.pop_size, no_phenotypes, p=self.prob_list)
