from DNA import DNA
import random


class Samples:
    def __init__(self, cap, mutation_rate, target):
        """
        :param cap: The maximum number of elements in the sample population
        :param mutation_rate: The probability that a member of the population is mutated
        :param target: The target phrase who's length will be the basis of the creation
        of the initial sample population
        """
        self.dna_pool = []
        self.mating_pool = []
        self.mutation_rate = mutation_rate * 100
        self.target = target
        self.max_fitness = 0
        self.cap = cap
        self.generation = 0
        self.best = ""

        for element in range(cap):
            self.dna_pool.append(DNA(len(target)))

    def evaluate_fitness(self):
        """Evaluates the fitness of each element in the DNA pool"""
        for dna in self.dna_pool:
            dna.evaluate_fitness(self.target)
            if self.max_fitness <= dna.fitness:
                self.max_fitness = dna.fitness
                self.best = dna.genetic_code

    def build_mating_pool(self):
        for dna in self.dna_pool:
            if dna.fitness > 15:
                for value in range(dna.fitness):
                    self.mating_pool.append(dna)

    def evolve(self):
        self.dna_pool = []
        confines = range(len(self.mating_pool))
        for value in range(self.cap):
            mother = self.mating_pool[random.choice(confines)]
            father = self.mating_pool[random.choice(confines)]
            child = mother.cross_over(father)
            child.mutate(self.mutation_rate)
            self.dna_pool.append(child)

    def evaluate(self)->bool:
        print("generation: {}; Best: {}; Fitness: {}".format(self.generation, self.best, self.max_fitness))
        if self.best == self.target:
            return False

        self.generation += 1
        return True
