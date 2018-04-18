import random
import string


class DNA:
    """Gotta review my bio. Sorry for the incorrect usage of the terms"""
    def __init__(self, length):
        self.length = length
        self.genetic_code = self.create()
        self.molecules = [code for code in self.genetic_code]
        self.fitness = 0

    def create(self)->string:
        """Creates some random string that will serve as the DNA's genetic code
            Returns an object that is of type string"""
        return ''.join(random.choice(string.ascii_letters) for char in range(self.length))

    def mutate(self, mutation_rate):
        """Changes a random character in the DNA's genetic code then updates its attributes"""
        if random.choice(range(2)) < mutation_rate:
            self.molecules[random.choice(range(len(self.genetic_code)))] = random.choice(string.ascii_letters)
            self.genetic_code = ''.join(self.molecules)
