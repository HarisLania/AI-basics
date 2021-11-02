import copy

#graph
graph = {
    'A':['B', 'D'],
    'B':['C', 'E'],
    'D':['G', 'H', 'E'],
    'E':['F', 'C'],
    'F':[],
    'G':['H'],
    'C':[],
    'H':[]
}

def get_neighbors(node):
    lst = []
    for i in graph[node]:
        lst.append(i)
    return lst



def BFS(start,goal):
    S = []
    path = []
    S.append(start)
    while S != []:
        path.append(list(S.pop(0)))
        node = path[-1][-1]
        n = get_neighbors(node)
        for i in n:
            newpath = list(copy.deepcopy(path[-1]))
            if i == goal:
                goal_path = copy.deepcopy(path[-1])
                goal_path.append(i)
                print(goal_path)
                return 'goal node found'

            newpath.append(i)
            S.append(newpath)


    return 'not found'

print(BFS('A', 'G'))