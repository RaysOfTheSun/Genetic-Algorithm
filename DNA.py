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
