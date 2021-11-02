import random

def fitness(x, y):
    val = (1-(x**2)) + 100 * (y - (x**2))**2
    return val


def generate_neighbors(x,y):
    x_y = random.randint(0,1)
    if x_y == 1:
        add_sub = random.randint(0,1)
        if add_sub == 0:
            if (x + 1) < 2 and (x + 1) > -2:
                x = x + 1
        else:
            if (x - 1) < 2 and (x - 1) > -2:
                x = x - 1
    else:
        add_sub = random.randint(0,1)
        if add_sub == 0:
            if (y + 1) < 3 and (y + 1) > -1:
                y = y + 1
        else:
            if (y - 1) < -1 and (y - 1) > 3:
                y = y - 1

        
    return x,y


x = random.uniform(-2,2)
y = random.uniform(-1,3)
best_fit = fitness(x,y)
print('initial x: {}, y: {}, fitness: {}'.format(x,y,best_fit))
stuck_counter = 0
peak = []
while True:
    x_new, y_new = generate_neighbors(x,y)
    fit = fitness(x_new, y_new)
    if fit > best_fit:
        x, y = x_new, y_new
        best_fit = fit
        stuck_counter = 0
        print('new x: {}, y: {}, fitness: {}'.format(x,y,best_fit))
    else:
        stuck_counter += 1

    if stuck_counter == 1000 and len(peak) == 10:
        print(peak)
        break
    
    else:
        peak.append(best_fit)
        x = random.uniform(-2,2)
        y = random.uniform(-1,3)



