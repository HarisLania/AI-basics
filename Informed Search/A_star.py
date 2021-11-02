import copy
romania = {
    'Arad':{'Sibiu':140,'Zerind':75,'Timisoara':118},
    'Sibiu':{'Arad':140,'Fagaras':99,'Oradea':151,'Rimnicu Vilcea':80},
    'Zerind':{'Arad':75,'Oradea':71},
    'Timisoara':{'Arad':118,'Lugoj':111},
    'Fagaras':{'Sibiu':99,'Bucharest':211},
    'Oradea':{'Zerind':71,'Sibiu':151},
    'Rimnicu Vilcea':{'Sibiu':80,'Pitesti':97,'Craiova':146},
    'Bucharest':{'Fagaras':211,'Pitesti':101,'Urziceni':85,'Giurgui':90},
    'Pitesti':{'Rimnicu Vilcea':97,'Bucharest':101,'Craiova':138},
    'Craiova':{'Rimnicu Vilcea':146,'Pitesti':138,'Dobreta':120},
    'Urziceni':{'Bucharest':85,'Hirsova':98,'Vasiui':142},
    'Giurgui':{'Bucharest':90},
    'Hirsova':{'Urziceni':98,'Eforie':86},
    'Vasiui':{'Urziceni':142,'Iasi':92},
    'Eforie':{'Hirsova':86},
    'Iasi':{'Vasiui':92,'Neamt':87},
    'Neamt':{'Iasi':87},
    'Lugoj':{'Timisoara':111,'Mehadia':70},
    'Mehadia':{'Lugoj':70,'Dobreta':75},
    'Dobreta':{'Craiova':120,'Mehadia':75}
}

h = {'Arad':366,
    'Bucharest':0,
    'Craiova':160,
    'Dobreta':242,
    'Eforie':161,
    'Fagaras':176,
    'Giurgui':77,
    'Hirsova':151,
    'Iasi':226,
    'Lugoj':244,
    'Mehadia':241,
    'Neamt':234,
    'Oradea':380,
    'Pitesti':100,
    'Rimnicu Vilcea':193,
    'Sibiu':253,
    'Timisoara':329,
    'Urziceni':80,
    'Vasiui':199,
    'Zerind':374
}

def get_neighbours(node):
    node = node[0][-1]
    n = romania[node]
    heuristic = []
    lst = []
    cost = []
    for i, j in n.items():
        lst.append(i)
        cost.append(j)
        heuristic.append(h[i])
    return lst, cost, heuristic


def A_Star(initial, final):
    S = [[[initial], 0, 0]]
    path = []
    a = 0
    visited = []
    while S:
        path.append(S.pop(0))
        n, cost, heuristic = get_neighbours(path[-1])
        node = path[-1][0][-1]
        visited.append(node)
        if node == final:
            return path[-1]
        for i in range(len(n)):
            newpath = copy.deepcopy(path[-1])
            if n[i] not in visited:
                newpath[0].append(n[i])
                newpath[1] += cost[i]
                newpath[2] = heuristic[i]
                S.append(newpath)

        S.sort(key=lambda x:x[1]+x[2])
        
    return 'Not found'

print(A_Star('Arad', 'Bucharest'))