import random
import os
import unittest
from unittest import makeSuite
import numpy as np

from genetic_algorithm import data_loader
from genetic_algorithm.solvers.phenotype import Phenotype


n, matrix_flow, matrix_distance = data_loader.load('had20.dat', '..')
assignment_had20 = Phenotype(size=n, m_flow=matrix_flow, m_dist=matrix_distance)


class TestSuite(unittest.TestSuite):
    def __init__(self):
        super(TestSuite, self).__init__()
        self.addTest(makeSuite(TestPhenotype))


class TestPhenotype(unittest.TestCase):

    def test_calc_cost_function_had12(self):
        size, m_flow, m_distance = data_loader.load('had12.dat', '..')
        assignment_had12 = Phenotype(size=size, m_flow=m_flow, m_dist=m_distance)
        factory = np.array([3, 10, 11, 2, 12, 5, 6, 7, 8, 1, 4, 9])
        assignment_had12.factories = list(map(lambda x: x - 1, factory))
        assignment_had12.calc_fitness_and_cost_fun()
        print(assignment_had12.m_dist[:, assignment_had12.factories][assignment_had12.factories])
        self.assertEqual(1652, assignment_had12.val_cost_fun)

    def test_calc_cost_function_had20(self):
        factory = np.array([8, 15, 16, 14, 19, 6, 7, 17, 1, 12, 10, 11, 5, 20, 2, 3, 4, 9, 18, 13])
        assignment_had20.factories = list(map(lambda x: x - 1, factory))
        assignment_had20.calc_fitness_and_cost_fun()
        self.assertEqual(6922, assignment_had20.val_cost_fun)

    def test_calc_cost_function_chr25a(self):
        size, m_flow, m_distance = data_loader.load('chr25a.dat', '..')
        assignment_chr25a = Phenotype(size=size, m_flow=m_flow, m_dist=m_distance)
        factory = np.array([25, 12, 5, 3, 18, 4, 16, 8, 20, 10, 14, 6, 15, 23, 24, 19, 13, 1, 21, 11, 17, 2, 22, 7, 9])
        assignment_chr25a.factories = list(map(lambda x: x - 1, factory))
        assignment_chr25a.calc_fitness_and_cost_fun()
        self.assertEqual(3796, assignment_chr25a.val_cost_fun)

    def test_random_assign(self):
        size = 10
        a = Phenotype(size=size, m_flow=matrix_flow, m_dist=matrix_distance, factories=np.arange(size))
        a.random_assign()
        random.seed(1)
        self.assertEqual(all(np.arange(10) == a.factories), False)
        a.factories.sort()
        self.assertEqual(all(np.arange(10) == a.factories), True)

    def test_mutate(self):
        a = Phenotype(size=3, m_flow=matrix_flow, m_dist=matrix_distance,
                      factories=np.array([0, 2, 1]), no_mutations=1)
        random.seed(1)
        # next random.randrange(size=3) == 0, then next random.randrange(size=3) == 2
        a.mutate()
        # switch 0th and 2nd elements in factories
        self.assertEqual(all(np.array([1, 2, 0]) == a.factories), True)

    def test_repair_genome(self):
        a = Phenotype(size=8, m_flow=matrix_flow, m_dist=matrix_distance, factories=np.array([0, 1, 2, 6, 6, 0, 5, 2]))
        random.seed(1)
        # list_not_contains=[3, 4, 7] then list_not_contains=[4, 7, 3]
        a.repair_genome()
        self.assertEqual(all(np.array([4, 1, 7, 3, 6, 0, 5, 2]) == a.factories), True)

    def test_crossover(self):
        a = Phenotype(size=4, m_flow=matrix_flow, m_dist=matrix_distance,
                      factories=np.array([0, 2, 1, 3]), no_divisions=1)
        b = Phenotype(size=4, m_flow=matrix_flow, m_dist=matrix_distance,
                      factories=np.array([2, 1, 3, 0]), no_divisions=1)
        random.seed(7)
        # next random.sample(4, 1) == 2
        child = a.crossover(b)
        print(child.factories)
        self.assertEqual(all(np.array([1, 2, 3, 0]) == child.factories), True)
