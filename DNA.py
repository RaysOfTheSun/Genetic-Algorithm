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
            self.molecules = [code for code in self.genetic_code]
        else:
            self.genetic_code = ""
            self.molecules = []

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
        if random.random() <= mutation_rate:
            self.molecules[random.choice(range(len(self.genetic_code)))] = random.choice(string.ascii_letters)
            self.genetic_code = ''.join(self.molecules)

    def evaluate_fitness(self, target):
        """
        :param target: the phrase in which the evaluation of fitness will be based on
        :return: the fitness score of the DNA object
        """
        """Evaluates the fitness of this specific DNA based on the number of characters it had that matched up
            with the characters present in the target word or phrase"""
        score = 0
        for self_code, target_code in zip(self.genetic_code, target):
            if self_code == target_code:
                score += 1

        self.fitness = int((score / len(target)) * 100)  # Although I can use floor here, more testing is needed

    def cross_over(self, partner):
        offspring = DNA()
        code_length = len(self.genetic_code)
        code_pool = self.molecules + partner.molecules
        for value in range(code_length):
            offspring.molecules.append(code_pool[random.choice(range(len(code_pool)))])
        offspring.genetic_code = ''.join(offspring.molecules)
        return offspring
