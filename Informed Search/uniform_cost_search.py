#UCS on graph
#Initial state: A
#final state - B
import copy
graph = {
    'A': {'O': 146, 'S':140, 'C':494},
    'O': {'A': 146, 'S': 151},
    'C': {'R': 146, 'P':138, 'A':494},
    'S': {'A':140, 'O':151, 'F':99, 'R':80},
    'R': {'S':80, 'C':146, 'P':97},
    'P': {'R': 97, 'C':138, 'B':101},
    'F': {'B':221, 'S':99},
    'B': {'F': 221, 'P':101}
}


def get_neighbours(node):
    node = node[0][-1]
    n = graph[node]
    lst = []
    cost = []
    for i, j in n.items():
        lst.append(i)
        cost.append(j)
    return lst, cost


def UCS(initial, final):
    S = [[[initial], 0]]
    path = []
    a = 0
    visited = []
    while S:
        path.append(S.pop(0))
        n, cost = get_neighbours(path[-1])
        node = path[-1][0][-1]
        visited.append(node)
        if node == final:
            return path[-1]
        for i in range(len(n)):
            newpath = copy.deepcopy(path[-1])
            if n[i] not in visited:
                newpath[0].append(n[i])
                newpath[1] += cost[i]
                S.append(newpath)

        S.sort(key=lambda x:x[1])
    return 'Not found'

print(UCS('A', 'B'))