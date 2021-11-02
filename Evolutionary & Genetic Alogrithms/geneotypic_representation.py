import random
import EA_operators
import GA_operators

# creating the population of 10
pop = [i for i in range(10)]

for i in range(10):
    # adding choromoses in the population
    # pop[i] = EA_operators.chromosome(-5,5,-2,2) if using evolutionary
    pop[i] = GA_operators.chromosome(8, -2, 2, -1, 3)


#population
print('     genes              fitness')
for chromo in pop:
    print(chromo.genes, chromo.fitness)

for i in range(10):
    new_pop = []

    for i in range(0, len(pop), 2):
        parents = EA_operators.post_select.select_best(pop, 2)
        child1, child2 = GA_operators.crossover.two_point(parents[0], parents[1])
        GA_operators.mutation.flip_mutation(child1)
        GA_operators.mutation.flip_mutation(child2)
        new_pop.append(child1)
        new_pop.append(child2)


    print('------------------------------------')
    print('     genes              fitness')
    for chromo in new_pop:
        print(chromo.genes, chromo.fitness)


    pop = EA_operators.parent_selection.binary_tournament(pop+new_pop, 8, len(pop))
    print('---------after post select----------')
    print('     genes            fitness')  
    for chromo in pop:
        print(chromo.genes, chromo.fitness)


