import random
import string


class DNA:
    """Gotta review my bio. Sorry for the incorrect usage of the terms (if any)"""
    def __init__(self, length=None):
        """
        Initializes a new DNA object
        :param length: An integer that acts as the maximum number of genes this DNA object would have
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
        Creates a random string of specified length
        :return A random string
        """
        character_pool = string.ascii_letters + " " + string.punctuation + string.digits
        character_pool = [char for char in character_pool]
        random.shuffle(character_pool)
        return ''.join(random.choice(character_pool) for char in range(self.length))

    def mutate(self, mutation_rate):
        """
        Changes a random gene of the DNA object
        :param mutation_rate: The probability of mutation
        :return a DNA object with mutated genes
        """
        if random.random() < mutation_rate:
            character_pool = string.ascii_letters + " " + string.punctuation + string.digits
            character_pool = [char for char in character_pool]
            random.shuffle(character_pool)
            self.genes[random.choice(range(len(self.code)))] = random.choice(character_pool)
            self.code = ''.join(self.genes)

    def evaluate_fitness(self, target):
        """
        Evaluates the fitness of this specific DNA based on how many times a character in its code matched up with
        the target's at the same position or index
        :param target: the phrase in which the evaluation of fitness will be based on
        :return the fitness score of the DNA object
        """
        score = sum(a == b for a, b in zip(self.code, target))

        self.fitness = int((score / len(target)) * 100)  # Gets the whole number from the computation

    def crossover(self, partner):
        """Does a crossover among this DNA and its partner
        :return a new DNA object with inherited attributes"""
        offspring = DNA()
        midpoint = int(len(self.code)/2)
        # Splitting up the parents' genes then adding them up seemed to produce better results
        # compared to adding their genes up then selecting a random character from that collection of genes
        offspring.genes = self.genes[:midpoint] + partner.genes[midpoint:]
        offspring.code = ''.join(offspring.genes)
        
        return offspring

    def print_fitness(self):
        print(self.fitness)
