from DNA import DNA


class Samples:
    def __init__(self, cap, mutation_rate, target):
        """
        :param cap: The maximum number of elements in the population
        :param mutation_rate: The probability that a member of the population is mutated
        :param target: The target phrase that will be the basis of the base population
        """
        self.pool = []
        self.mutation_rate = mutation_rate
        self.target = target
        self.max_fitness = 0
        self.mating_pool = []

        for generation in range(cap):
            self.pool.append(DNA(len(target)))
