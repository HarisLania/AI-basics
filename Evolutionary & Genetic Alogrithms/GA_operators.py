# geneotypic representation range x = (-5,5) y = (-2, 2)
# since the highest number in range is 5 so we will use 3 bit representation and 1 bit for sign
# 0 = +, 1 = -
# function -> 𝒇(𝒙, 𝒚) = (𝟏 − 𝒙)^𝟐 + 𝟏𝟎𝟎(𝒚 − 𝒙^2)^2

import random
import copy
import math

class chromosome:
    def __init__(self, length, x1, x2, y1, y2):
        self.genes = [random.randint(0,1) for i in range(length)]
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.length = length
        self.genes = self.check_range()
        self.fitness = self.evaluate()

    
    def decode(self):
        # check sign from 1st bit, 4 * 2nd bit + 2 * 3rd bit + 1 * 4th bit
        x = 4 * self.genes[1] + 2 * self.genes[2] + 1 * self.genes[3]
        y = 4 * self.genes[-3] + 2 * self.genes[-2] + 1 * self.genes[-1]

        if self.genes[0]:
            x *= -1
        
        if self.genes[-4]:
            y *= -1
        
        return x, y


    def check_range(self):
        check_x, check_y = True, True
        while check_x or check_y:
            x, y = self.decode()
            if check_x == True:
                if x > self.x1 and x < self.x2:
                    check_x = False
                else:
                    for i in range(self.length//2):
                        self.genes[i] = random.randint(0,1)

            if check_y == True:
                if y > self.y1 and y < self.y2:
                    check_y = False
                else:
                    for i in range((self.length//2), self.length):
                        self.genes[i] = random.randint(0,1)
        
        return self.genes

 

    def evaluate(self):
        #to evaluate fitness of genes we first need to decode it
        x, y = self.decode()
        # return math.exp(-(pow(x,2) + pow(y,2)))
        return (1 - x) ** 2 + 100 * ((y - x**2)**2)


class crossover:
    
    def one_point(parent1, parent2): 
        crossover_point = random.randint(0, len(parent1.genes))
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)
        child1.genes[crossover_point:] = parent2.genes[crossover_point:]
        child2.genes[crossover_point:] = parent1.genes[crossover_point:]
        child1_x, child1_y = child1.decode()
        child2_x, child2_y = child2.decode()
        if child1_x < child1.x1 or child1_x > child1.x2 or child1_y < child1.y1 or child1_y > child1.y2:
            child1.genes[crossover_point:] = parent1.genes[crossover_point:]
        if child2_x < child1.x1 or child2_x > child1.x2 or child2_y < child1.y1 or child2_y > child1.y2:
            child2.genes[crossover_point:] = parent2.genes[crossover_point:]
        
        child1.fitness = child1.evaluate()
        child2.fitness = child2.evaluate()
        return child1, child2
    

    def two_point(parent1, parent2):
        crossover_point1 = random.randint(0, len(parent1.genes))
        crossover_point2 = random.randint(0, len(parent1.genes))
        if crossover_point1 > crossover_point2:
            crossover_point1, crossover_point2 = crossover_point2, crossover_point1
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)
        child1.genes[crossover_point1:crossover_point2] = parent2.genes[crossover_point1:crossover_point2]
        child2.genes[crossover_point1:crossover_point2] = parent1.genes[crossover_point1:crossover_point2]
        child1_x, child1_y = child1.decode()
        child2_x, child2_y = child2.decode()
        if child1_x < child1.x1 or child1_x > child1.x2 or child1_y < child1.y1 or child1_y > child1.y2:
            child1.genes[crossover_point1:crossover_point2] = parent1.genes[crossover_point1:crossover_point2]
        if child2_x < child1.x1 or child2_x > child1.x2 or child2_y < child1.y1 or child2_y > child1.y2:
            child2.genes[crossover_point1:crossover_point2] = parent2.genes[crossover_point1:crossover_point2]
        
        child1.fitness = child1.evaluate()
        child2.fitness = child2.evaluate()

        return child1, child2
    

class mutation:

    def flip_mutation(chromo):
        if random.random() < .2:
            index = random.randint(0,(len(chromo.genes)-1))
            if chromo.genes[index]:
                chromo.genes[index] = 0
                x, y = chromo.decode()
                if x < chromo.x1 or x > chromo.x2 or y < chromo.y1 or y > chromo.y2:
                    chromo.genes[index] = 1
            else:
                chromo.genes[index] = 1
                x, y = chromo.decode()
                if x < chromo.x1 or x > chromo.x2 or y < chromo.y1 or y > chromo.y2:
                    chromo.genes[index] = 0
        
            chromo.fitness = chromo.evaluate()
        
        return chromo