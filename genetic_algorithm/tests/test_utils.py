import random
import unittest
import os
from unittest import makeSuite

import numpy as np

# from ai.genetic_algorithm import phenotype
from genetic_algorithm import data_loader
from genetic_algorithm.solvers.phenotype import Phenotype

n, matrix_flow, matrix_distance = data_loader.load('had20.dat', '..')
assignment_had20 = Phenotype(size=n, m_flow=matrix_flow, m_dist=matrix_distance)


class TestSuite(unittest.TestSuite):
    def __init__(self):
        super(TestSuite, self).__init__()
        self.addTest(makeSuite(TestDataLoader))


class TestDataLoader(unittest.TestCase):
    def test_matrix_flow_size(self):
        self.assertEqual(n, matrix_flow.shape[0])

    def test_matrix_distance_size(self):
        self.assertEqual(n, matrix_flow.shape[1])
