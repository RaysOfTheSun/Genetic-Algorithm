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
        self.mutation_rate = mutation_rate
        self.target = target
        self.max_fitness = 0
        self.cap = cap
        self.generation = 0
        self.fittest = ""

        for element in range(cap):
            self.dna_pool.append(DNA(len(target)))

    def evaluate_fitness(self):
        """Evaluates the fitness of each element in the DNA pool"""
        for dna in self.dna_pool:
            dna.evaluate_fitness(self.target)
            if self.max_fitness <= dna.fitness:
                self.max_fitness = dna.fitness
                self.fittest = dna.code

    def build_mating_pool(self):
        self.mating_pool = []
        for dna in self.dna_pool:
            if dna.fitness > 0:
                for x in range(dna.fitness):
                    self.mating_pool.append(dna)

    def evolve(self):
        self.dna_pool = []
        for value in range(self.cap):
            mother = random.choice(self.mating_pool)
            father = random.choice(self.mating_pool)
            child = mother.crossover(father)
            child.mutate(self.mutation_rate)
            self.dna_pool.append(child)

    def get_average_fitness(self):
        total = 0
        for dna in self.dna_pool:
            total += dna.fitness
        return total

    def evaluate(self)->bool:
        print("generation: {}; fittest: {}; Fitness: {}%; Average Fitness:{}%".format(
            self.generation, self.fittest, self.max_fitness, self.get_average_fitness()
        ))
        if self.fittest == self.target:
            return False

        self.generation += 1
        return True
