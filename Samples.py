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
        self.__dna_pool = []
        self.__mating_pool = []
        self.__mutation_rate = mutation_rate
        self.__target = target
        self.__max_fitness = 0
        self.__cap = cap
        self.__generation = 0
        self.__fittest = ""
        self.__average_fitness = 0

        for element in range(cap):
            self.__dna_pool.append(DNA(len(target)))

    def evaluate_fitness(self):
        """Evaluates the fitness of each element in the DNA pool"""
        self.__average_fitness = 0
        for dna in self.__dna_pool:
            dna.evaluate_fitness(self.__target)
            self.__average_fitness += dna.fitness
            if self.__max_fitness <= dna.fitness:
                self.__max_fitness = dna.fitness
                self.__fittest = dna.code
        # Complete the computation of the average fitness for this generation
        self.__average_fitness = int((self.__average_fitness / self.__cap))

    def build_mating_pool(self):
        self.__mating_pool = []
        for dna in self.__dna_pool:
            if dna.fitness != 0:
                for x in range(dna.fitness):
                    self.__mating_pool.append(dna)

    def evolve(self):
        self.__dna_pool = []
        for value in range(self.__cap):
            mother = random.choice(self.__mating_pool)
            father = random.choice(self.__mating_pool)
            while mother == father:
                mother = random.choice(self.__mating_pool)
            child = mother.crossover(father)
            child.mutate(self.__mutation_rate)
            self.__dna_pool.append(child)

    def evaluate(self)->bool:
        print("generation: {}; fittest: {}; Fitness: {}%; Average Fitness: {}%; MR: {}%".format(
            self.__generation, self.__fittest, self.__max_fitness, self.__average_fitness, self.__mutation_rate * 100
        ))
        if self.__fittest == self.__target:
            return False

        self.__generation += 1
        return True
