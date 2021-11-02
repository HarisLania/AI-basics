# evaluating function = (x^2 + y^2)
import random
import copy

class chromosome:
    def __init__(self, x1, x2, y1, y2):
        self.x = random.uniform(x1,x2)
        self.y = random.uniform(y1,y2)
        self.fitness = self.evaluate()
    
    def evaluate(self):
        return self.x**2 + self.y**2


class parent_selection:

    def binary_tournament(pop, tour_size, parent_count):
        parent_list = []
        for i in range(parent_count):
            teams = []
            for j in range(tour_size):
                val = random.choice(pop)
                teams.append(val)
                
            sorted(teams, key=lambda x:x.fitness, reverse=True)
            parent_list.append(teams[0])
        
        return parent_list

    def select_best(pop,parent_count):
        pop = sorted(pop, key=lambda x:x.fitness, reverse=True)
        parents = []
        for i in range(parent_count):
            parents.append(pop[i])
        
        return parents
    
    def random(pop, parent_count):
        parents = []
        for i in range(parent_count):
            parents.append(random.choice(pop))
        
        return parents

class crossover:
    def one_point(parent1,parent2):
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)
        if random.random() < .8:
            child1.y = parent2.y
            child2.y = parent1.y
            
        child1.fitness = child1.evaluate()
        child2.fitness = child2.evaluate()
        return child1, child2


class mutation:
    def mutate(chromo):
        if random.random() < .2:
            print('mutation before x:{}, y:{}, fitness:{}'.format(chromo.x, chromo.y, chromo.fitness))
            if random.random() < .5:
                if random.random() < .5:
                    if (chromo.x + .2) < 5 and (chromo.x + .2) > -5:
                        chromo.x += .2
                else:
                    if (chromo.x - .2) < 5 and (chromo.x - .2) > -5:
                        chromo.x -= .2
            else:
                if random.random() < .5:
                    if (chromo.y + .2) < 2 and (chromo.y + .2) > -2:
                        chromo.y += .2
                else:
                    if (chromo.y - .2) < 2 and (chromo.y - .2) > -2:
                        chromo.y -= .2

            chromo.fitness = chromo.evaluate()
            print('mutation after x:{}, y:{}, fitness:{}'.format(chromo.x, chromo.y, chromo.fitness))

class post_select:
    def select_best(pop,count):
        pop = sorted(pop, key=lambda x:x.fitness, reverse=True)
        parents = []
        for i in range(count):
            parents.append(pop[i])
        
        return parents