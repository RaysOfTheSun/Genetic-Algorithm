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
            self.genetic_code = self.create()
        else:
            self.genetic_code = ""

        self.fitness = 0.0
        self.molecules = [code for code in self.genetic_code]

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
            self.molecules[random.choice(range(len(self.genetic_code)))] = random.choice(string.ascii_letters)
            self.genetic_code = ''.join(self.molecules)

    def evaluate_fitness(self, target):
        """
        :param target: the phrase in which the evaluation of fitness will be based on
        :return: the fitness score of the DNA object
        """
        """Evaluates the fitness of this specific DNA based on the number of characters it had that matched up
            with the characters present in the target word or phrase"""
        score = 0.0
        for index in range(len(target)):
            if self.molecules[index] == target[index]:
                score += 1

        self.fitness = (score / len(target)) * 100  # Although I can use floor here, more testing is needed
        self.fitness = int(self.fitness)

    def cross_over(self, partner):
        offspring = DNA()
        code_length = len(self.genetic_code)
        for value in range(code_length):
            offspring.molecules.append(self.molecules[random.choice(range(code_length))])
            offspring.molecules.append(partner.molecules[random.choice(range(code_length))])
            offspring.genetic_code = ''.join(offspring.molecules)

        return offspring
