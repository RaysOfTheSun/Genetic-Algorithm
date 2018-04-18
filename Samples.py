from DNA import DNA


class Samples:
    def __init__(self, cap, mutation_rate, target):
        self.pool = []
        self.mutation_rate = mutation_rate
        self.target = target
        self.mating_pool = []

        for generation in range(0, cap + 1):
            self.pool.append(DNA(len(target)))
