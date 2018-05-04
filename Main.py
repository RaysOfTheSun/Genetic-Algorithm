from Samples import Samples
sample = Samples(500, 50, "if name == '__main__': print('Hello, world!')")

while sample.evaluate():
    sample.evaluate_fitness()
    sample.build_mating_pool()
    sample.evolve()