# A* Search Algorithm
# Mario Jimenez


def AStarSearch(Maze):
    open, closed = [[mousePosition(M)]], [mousePosition(M)]
    cheese = cheesePosition(Maze)
    print("Open: ", open)
    print("Closed: ", closed)
    print("Cheese: ", cheese)
    # open is a list of paths, each of which begins at the mousePosition(M)
    # closed is a list of the cells we have found a shortest path to
    while len(open) > 0:
        path = open[0]
        destination = path[len(path) - 1]
        if Maze[destination[0]][destination[1]] == 'c':
            return path  # Found the cheese
        # throw away the path we just tested.
        open = open[1:]
        # insert children of path into open list. Each child is a path.
        for cell in adjacentCells(destination, Maze):
            if cell not in closed:
                # This line did not change the open list p
                # print("path + cell: ", path, [cell])
                # print("open: ", open)
                open = insert(path + [cell], open, cheese)
        closed = closed + [destination]  # and add its last cell to closed list
        print("Closed: ", closed)
    return None


# IF M is a maze, mousePosition(M) is the cell in M containing 'm'
def mousePosition(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'm':
                return (i, j)


def cheesePosition(Maze):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == 'c':
                return (i, j)


# adjacentCells: cell*maze -> list<cell>
# If c is a cell and M is a maze,
# adjacentCells(C,M) is a list of the cells adjacent to C in M.
def adjacentCells(destination, Maze):
    cells = []
    i, j = destination

    if(i > 0):
        if M[i - 1][j] != 'x':
            cells += [(i - 1, j)]
    if(j > 0):
        if M[i][j - 1] != 'x':
            cells += [(i, j - 1)]
    if(i < len(Maze) - 1):
        if M[i + 1][j] != 'x':
            cells += [(i + 1, j)]
    if(j < len(Maze) - 1):
        if M[i][j + 1] != 'x':
            cells += [(i, j + 1)]

    # print("Adjacent Cells: ", cells)
    return cells


# insert: path * list<path>  * cell -> list<path>
# If p is a path, L is a list of paths sorted in nondecreasing order
# by estimated total cost, and c is a cell, then insert(p,L,c) is the list
# obtained from L by inserting p so that the list remains sorted.
# The estimated total cost of a path is its length plus the manhattan distance
# from its last cell to c. For extra credit, write this so that it runs in time
# O(log(len(L))).
def insert(path, open, cheese):

    # The estimated total cost of a path is its length plus the manhattanD.
    # cost = length + manhattanD(?, cheesePosition)
    for i in range(0, len(open)):
        if len(path) + manhattanD(path[len(path) - 1], cheese) <= len(open) + manhattanD(open[i][i], cheese):
            return open[0:i] + [path] + open[i:len(open)]
    return open + [path]


# ManhattanD: cell*cell -> int
# manhattanD(c1,c2) is the Manhattan distance between c1 and c2
def manhattanD(c1, c2):
    i1, j1 = c1
    i2, j2 = c2
    return abs(i1 - i2) + abs(j1 - j2)


# R0 = ['o', 'm', 'x', 'c']
# R1 = ['o', 'o', 'x', 'o']
# R2 = ['x', 'o', 'o', 'o']
# R3 = ['o', 'x', 'o', 'x']
# M = [R0, R1, R2, R3]

R0 = ['o', 'o', 'o', 'o']
R1 = ['m', 'x', 'o', 'o']
R2 = ['x', 'x', 'o', 'o']
R3 = ['c', 'o', 'o', 'o']
M = [R0, R1, R2, R3]

print("Path to the cheese: ", AStarSearch(M))
