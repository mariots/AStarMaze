# A* Search Algorithm
# Mario Jimenez


def AStarSearch(Maze):
    open, closed = [[mousePosition(M)]], [mousePosition(M)]
    # open is a list of paths, each of which begins at the mousePosition(M)
    # closed is a list of the cells we have found a shortest path to
    while len(open) > 0:
        path = open[0]
        destination = path[len(path) - 1]
        if Maze[destination[0]][destination[1]] == 'c':
            return path  # found the cheese
        open = open[1:]  # throw away the path we just tested
        # insert children of path into open list. Each child is a path.
        for cell in adjacentCells(destination, Maze):
            if cell not in closed:
                open = insert(path + [cell], open, cheesePosition(Maze))
        open = open[1:]  # throw away the path we just tested
        closed = closed + [destination]  # and add its last cell to closed list
    return None


def mousePosition(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'm':
                print("(i, j): ", i, j)
                return (i, j)


def cheesePosition(Maze):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'c':
                return (i, j)


def adjacentCells(destination, Maze):
    print("Destination: ", destination)
    print("Maze: ", Maze)
    return 1


def insert(path, open, cheesePosition):
    print("path: ", path)
    print("open: ", open)
    print("cheesePosition: ", cheesePosition)
    return 1


R0 = ['o', 'm', 'x', 'c']
R1 = ['o', 'o', 'x', 'o']
R2 = ['x', 'o', 'o', 'o']
R3 = ['o', 'x', 'o', 'x']
M = [R0, R1, R2, R3]

print(M)
AStarSearch(M)
