import random
import string
from DNA import DNA


class Samples:
    def __init__(self, generations, mutation_rate, target):
        self.pool = []
        self.mutation_rate = mutation_rate
        self.target = target
        self.generations = generations

        for generation in range(0, generations + 1):
            self.pool.append(DNA(len(target)))

    @staticmethod
    def mutate(dna)->DNA:
        """Accepts an argument of type DNA.
           This would help achieve variation in our samples"""
        char = random.choice(string.ascii_letters)
        dna.molecules[random.choice(range(0, len(dna.genetic_code)))] = char
        dna.genetic_code = ''.join(dna.molecules)
        return dna
