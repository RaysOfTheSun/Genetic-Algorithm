import random
import string


class DNA:
    """Gotta review my bio. Sorry for the incorrect usage of the terms (if any)"""
    def __init__(self, length=None):
        """
        :param length: the maximum length of the DNA's genetic code
        """
        if length is not None:
            self.length = length
            self.code = self.create()
            self.genes = [code for code in self.code]
        else:
            self.code = ""
            self.genes = []

        self.fitness = 0

    def create(self)->string:
        """
        :return: A new random phrase of type string
        """
        """Creates some random string that will serve as the DNA's genetic code
            Returns an object that is of type string"""
        character_pool = string.ascii_letters + " "
        return ''.join(random.choice(character_pool) for char in range(self.length))

    def mutate(self, mutation_rate):
        """
        :param mutation_rate: The probability of mutation
        :return: a DNA object with mutated genes
        """
        """Changes a random character in the DNA's genetic code then updates its attributes"""
        if random.random() < mutation_rate:
            character_pool = string.ascii_letters + " "
            self.genes[random.choice(range(len(self.code)))] = random.choice(character_pool)
            self.code = ''.join(self.genes)

    def evaluate_fitness(self, target):
        """
        :param target: the phrase in which the evaluation of fitness will be based on
        :return: the fitness score of the DNA object
        """
        """Evaluates the fitness of this specific DNA based on the number of characters it had that matched up
            with the characters present in the target word or phrase"""
        score = sum(a == b for a, b in zip(self.code, target))

        self.fitness = int((score / len(target)) * 100)  # Gets the whole number from the computation

    def crossover(self, partner):
        offspring = DNA()
        midpoint = int(len(self.code)/2)
        # Splitting up the parents' genes then adding them up seemed to produce better results
        # compared to adding their genes up then selecting a random character from that collection of genes
        offspring.genes = self.genes[:midpoint] + partner.genes[midpoint:]
        offspring.code = ''.join(offspring.genes)
        
        return offspring

    def print_fitness(self):
        print(self.fitness)
