import numpy as np

def objective_function(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

def initialize_population(size, dimension, bounds):
    return np.random.uniform(bounds[0], bounds[1], (size, dimension))

def evaluate(population):
    return np.array([objective_function(ind) for ind in population])

def select(population, fitness, num_selected):
    idx = np.argsort(fitness)
    return population[idx[:num_selected]]

def clone(antibodies, clone_factor):
    clones = []
    for antibody in antibodies:
        for _ in range(clone_factor):
            clones.append(antibody.copy())
    return np.array(clones)

def mutate(clones, mutation_rate=0.1):
    return clones + mutation_rate * np.random.randn(*clones.shape)

def clonal_selection(pop_size=30, dim=2, bounds=(-5, 5), generations=50,
                     num_selected=5, clone_factor=5, mutation_rate=0.1):

    population = initialize_population(pop_size, dim, bounds)

    for gen in range(generations):
        fitness = evaluate(population)
        selected = select(population, fitness, num_selected)
        clones = clone(selected, clone_factor)
        mutated = mutate(clones, mutation_rate)
        combined = np.vstack((population, mutated))
        combined_fitness = evaluate(combined)
        best_indices = np.argsort(combined_fitness)[:pop_size]
        population = combined[best_indices]

        best = population[0]
        print(f"Generation {gen+1}: Best = {best}, Fitness = {objective_function(best):.4f}")

    return population[0], objective_function(population[0])

best_solution, best_value = clonal_selection()
print("\nBest Solution:", best_solution)
print("Best Objective Value:", best_value)
