from DNA import DNA
import random


class Samples:
    def __init__(self, cap, mutation_rate, target):
        """
        Initializes a new Samples object
        :param cap: The maximum number of elements in the sample population
        :param mutation_rate: A whole number that represents the probability that a member of the population is mutated
        :param target: The target phrase who's length will be the basis of the creation
        of the initial sample population (dna pool)
        """

        if not isinstance(target, str):
            target = str(target)  # Just convert it to a string. I don't think it's a big deal
        if not isinstance(cap, int):
            raise TypeError("Parameter \"cap\" should be an integer.")
        if not isinstance(mutation_rate, int):
            raise TypeError("The parameter \"mutation_rate\" should be an integer")
        self.__dna_pool = []
        self.__mating_pool = []
        self.__mutation_rate = mutation_rate / 100
        self.__target = target
        self.__max_fitness = 0
        self.__cap = cap  # The maximum number of elements in the dna pool
        self.__generation = 0
        self.__fittest = ""
        self.__average_fitness = 0

        self.__dna_pool = [DNA(len(target)) for x in enumerate(range(cap))]

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
        """Creates a mating pool that would contain the top 20% of the fittest elements in the dna pool"""
        self.__mating_pool = []
        # Sort the dna_pool in ascending order by fitness
        list.sort(self.__dna_pool, key=lambda y: y.fitness, reverse=True)
        for dna in self.__dna_pool[:int((len(self.__dna_pool)*0.2))]:  # Only grab the top 20% of the elements
            if dna.fitness != 0:
                for x in range(dna.fitness):
                    self.__mating_pool.append(dna)

    def evolve(self):
        """Performs crossover and mutation on the elements present in the mating pool"""
        self.__dna_pool = []
        for value in range(self.__cap):
            mother = random.choice(self.__mating_pool)
            father = random.choice(self.__mating_pool)
            while mother == father:  # Always make sure that the mother and father are different entities
                mother = random.choice(self.__mating_pool)
            child = mother.crossover(father)
            child.mutate(self.__mutation_rate)
            self.__dna_pool.append(child)

    def evaluate(self)->bool:
        """Checks if the fittest element matches up with the target
        :return true if the fittest element matches up with the target"""
        print("generation: {}; fittest: {}; Fitness: {}%; Average Fitness: {}%; MR: {}%".format(
            self.__generation, self.__fittest, self.__max_fitness, self.__average_fitness, int(self.__mutation_rate*100)
        ))
        if self.__fittest == self.__target:
            return False

        self.__generation += 1
        return True
