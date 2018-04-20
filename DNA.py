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
        return ''.join(random.choice(string.ascii_letters) for char in range(self.length))

    def mutate(self, mutation_rate):
        """
        :param mutation_rate: The probability of mutation
        :return: a DNA object with a mutated genetic code
        """
        """Changes a random character in the DNA's genetic code then updates its attributes"""
        if random.choice(range(2)) < mutation_rate:
            self.genes[random.choice(range(len(self.code)))] = random.choice(string.ascii_letters)
            self.code = ''.join(self.genes)

    def evaluate_fitness(self, target):
        """
        :param target: the phrase in which the evaluation of fitness will be based on
        :return: the fitness score of the DNA object
        """
        """Evaluates the fitness of this specific DNA based on the number of characters it had that matched up
            with the characters present in the target word or phrase"""
        score = sum(a == b for a, b in zip(self.code, target))

        self.fitness = int((score / len(target)) * 100)  # Although I can use floor here, more testing is needed

    def cross_over(self, partner):
        offspring = DNA()
        code_length = len(self.code)
        code_pool = self.genes + partner.genes
        for value in range(code_length):
            offspring.genes.append(code_pool[random.choice(range(len(code_pool)))])
        offspring.code = ''.join(offspring.genes)
        return offspring
