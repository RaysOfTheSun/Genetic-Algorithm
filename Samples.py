from DNA import DNA


class Samples:
    def __init__(self, cap, mutation_rate, target):
        self.pool = []
        self.mutation_rate = mutation_rate
        self.target = target
        self.max_fitness = 0
        self.mating_pool = []

        for generation in range(cap):
            self.pool.append(DNA(len(target)))
