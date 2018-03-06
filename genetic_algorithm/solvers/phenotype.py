import numpy as np
import random


class Phenotype(object):
    NUMBER_OF_DIVISIONS = 1
    NUMBER_OF_MUTATIONS = 1

    def __init__(self, size, m_flow, m_dist, factories=None, no_divisions=NUMBER_OF_DIVISIONS,
                 no_mutations=NUMBER_OF_MUTATIONS):
        self.size = size
        self.factories = factories
        self.val_fitness_fun = -1
        self.val_cost_fun = -1
        self.m_flow = m_flow
        self.m_dist = m_dist
        self.probability_selection = 0
        self.no_divisions = no_divisions
        self.no_mutations = no_mutations
        if factories is None:
            self.factories = np.arange(self.size)
            self.random_assign()

    def random_assign(self):
        random.shuffle(self.factories)

    def mutate(self):
        for i in range(self.no_mutations):
            j = random.randrange(self.size)
            k = random.randrange(self.size)
            self.factories[j], self.factories[k] = self.factories[k], self.factories[j]

    def crossover(self, parent):
        # 0. 2 3. 6 1. 4 5   +
        # 5. 4 1. 6 4. 3 2   ==
        # 0. 4 1. 6 1. 3 2   repair eg.
        # 0. 4 5. 6 1. 3 2
        divide_points = random.sample(range(self.size), self.no_divisions)
        divide_points.extend([0, self.size])
        divide_points.sort()
        dp = divide_points
        switch = True
        temp = np.array([], dtype=int)
        for i in range(self.no_divisions + 1):
            if switch:
                temp = np.append(temp, self.factories[dp[i]:dp[i + 1]])
            else:
                temp = np.append(temp, parent.factories[dp[i]:dp[i + 1]])
            switch = not switch
        child = Phenotype(size=self.size, factories=temp, m_flow=self.m_flow, m_dist=self.m_dist)
        child.repair_genome()
        return child

    def repair_genome(self):
        temp = np.copy(self.factories)
        temp.sort()
        list_not_contains = []
        list_twice_contains = []
        for i in range(self.size - 1):
            if i not in temp:
                list_not_contains.append(i)
            if temp[i] == temp[i + 1]:
                list_twice_contains.append(temp[i])
        if not self.size - 1 in temp:
            list_not_contains.append(self.size - 1)
        random.shuffle(list_not_contains)
        for i in range(self.size - 1):
            if self.factories[i] in list_twice_contains:
                list_twice_contains.remove(self.factories[i])
                self.factories[i] = list_not_contains.pop(0)

    def calc_fitness_and_cost_fun(self):
        new_m_dist = self.m_dist[:, self.factories][self.factories]
        self.val_cost_fun = np.sum(np.multiply(self.m_flow, new_m_dist))
