import random
import string


class DNA:
    def __init__(self, length):
        self.length = length
        self.genetic_code = self.create()
        self.molecules = [code for code in self.genetic_code]
        self.fitness = 0

    def create(self)->string:
        return ''.join(random.choice(string.ascii_letters) for char in range(self.length))

    def mutate(self, mutation_rate):
        if random.choice(range(0, 2)) < mutation_rate:
            self.molecules[random.choice(range(0, len(self.genetic_code) + 1))] = random.choice(string.ascii_letters)
            self.genetic_code = ''.join(self.molecules)
