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

visited = []
path = []

def DFS(node,goal):
    global visited
    global path
    path.append(list(node)) 
    n = get_neighbors(path[-1][-1])
    for i in n:
        if i not in visited:
            newpath = copy.deepcopy(path[-1])
            if i == goal:
                goal_path = path[-1]
                goal_path.append(goal)
                print(goal_path)
                print('found the goal node')
                return
            newpath.append(i)
            visited.append(node)
            DFS(newpath, goal)
    print(path)
    path.pop()

print(DFS('A', 'G'))