from DNA import DNA


class Samples:
    def __init__(self, cap, mutation_rate, target):
        """
        :param cap: The maximum number of elements in the population
        :param mutation_rate: The probability that a member of the population is mutated
        :param target: The target phrase that will be the basis of the base population
        """
        self.dna_pool = []
        self.mutation_rate = mutation_rate
        self.target = target
        self.max_fitness = 0
        self.mating_pool = []

        for element in range(cap):
            self.dna_pool.append(DNA(len(target)))

    def evaluate_fitness(self):
        """Evaluates the fitness of each element in the DNA pool"""
        for dna in self.dna_pool:
            dna.evaluate_fitness(self.target)
            if self.max_fitness == 0:
                self.max_fitness = dna.fitness
            elif self.max_fitness < dna.fitness:
                self.max_fitness = dna.fitness
