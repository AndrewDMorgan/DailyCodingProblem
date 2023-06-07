
# the maze
maze = [
    [False, False, False, False],
    [True , True , False, True ],
    [False, False, False, False],
    [False, False, False, False]
]

# the length of the maze
mazeLength = [len(maze[0]), len(maze)]


# generate the shortest path for the matrix
def GeneratePath(pos: tuple, dest: tuple, path: list=[]) -> list:
    if pos == dest: return path  # ending the search if at the destination

    # looping through the possible paths and finding the best one
    i = -1
    paths = []
    best = [1000000, -1]  # length, index
    for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        # getting the new position
        newPos = (pos[0] + direction[0], pos[1] + direction[1])
        
        # checking that the position is in the matrix
        if newPos[0] < 0 or newPos[0] >= mazeLength[0] or newPos[1] < 0 or newPos[1] >= mazeLength[1]:
            continue
        
        # checking that the position isn't a wall and hasn't been walked on
        if maze[newPos[1]][newPos[0]] or newPos in path:
            continue
        
        # generating the path and checking if it's better then the previous ones
        finalPath = GeneratePath(newPos, dest, path + [newPos])
        if finalPath:
            i += 1
            paths.append(finalPath)
            pathLength = len(finalPath)
            if best[0] > pathLength:
                best = [pathLength, i]
    
    # checking for the lowest path (if none then None)
    return paths[best[1]] if (best[1] > -1) else None


# testing it (should be a length of 7 which it is)
print(GeneratePath((0, 3), (0, 0)))
