#Non-recursive Backtracking maze solver
import numpy as np
import random


def solve_maze(maze):#, start, finish):
#CONSTRUCT THE SECOND LIST WITH SAME BARRIERS
    nrows = len(maze)                       #find dimension of maze
    ncols = len(maze[0])
    start = maze[0][0]
    end = maze[nrows-1][ncols-1]
    a = np.array(maze)               #convert maze to numpy array as variable numpyfin
    b = np.where(a==1)              #find indices where 1 is (barriers)
    comparr = np.arange(2,(nrows*ncols)+2).reshape(nrows,ncols)  #create a second array for reference 
    for i,j in zip(b[0],b[1]):
        comparr[i,j] = 1                            #put barriers on 

# CREATE NEIGHBOR LISTS 
    non_ones = []
    neighbors =  []                    #list of none_one values which are acceptable to have neighbors      
    for i in range(nrows):
        for j in range(ncols):
            if comparr[i][j] != 1:
                non_ones.append(comparr[i][j])
#CHECKING NEGHBORS OF CORNERS
                entry = []
                if (i == 0 and j == 0) or (i == 0 and j == ncols-1) or (i == nrows-1 and j == 0) or (i == nrows-1 and j == ncols-1):
                    if i == 0 and j == 0:       #if a corner, can at most have two neighbors
                        if comparr[i][j+1] != 1:
                            entry.append(comparr[i][j+1])
                        if comparr[i+1][j] != 1:
                            entry.append(comparr[i+1][j])
                    elif i == 0 and j == ncols-1: #if a corner, can at most have two neighbors
                        if comparr[i+1][j] != 1:
                            entry.append(comparr[i+1][j])
                        if comparr[i][j-1] != 1:
                            entry.append(comparr[i][j-1])
                    elif i == nrows-1 and j == 0:   #if a corner, can at most have two neighbors
                        if comparr[i-1][j] != 1:
                            entry.append(comparr[i-1][j])
                        if comparr[i][j+1] != 1:
                            entry.append(comparr[i][j+1])
                    elif i == nrows-1 and j == ncols-1:
                        if comparr[i-1][j] != 1:
                            entry.append(comparr[i-1][j])
                        if comparr[i][j-1] != 1:
                            entry.append(comparr[i][j-1])
####    CHECKING SIDES  #####
                elif (i == 0 and j != 0) or (j == 0 and i != 0) or (j == ncols-1 and i != 0) or (i == nrows-1 and j != 0):
                    if i == 0 and j !=0:
                        if comparr[i][j+1] != 1:
                            entry.append(comparr[i][j+1])
                        if comparr[i][j-1] != 1:
                            entry.append(comparr[i][j-1])
                        if comparr[i+1][j] != 1:
                            entry.append(comparr[i+1][j])
                    elif j == 0 and i != 0:
                        if comparr[i+1][j] != 1:
                            entry.append(comparr[i+1][j])
                        if comparr[i-1][j] != 1:
                            entry.append(comparr[i-1][j])
                        if comparr[i][j+1] != 1:
                            entry.append(comparr[i][j+1])
                    elif j == ncols-1 and i != 0:
                        if comparr[i+1][j] != 1:
                            entry.append(comparr[i+1][j])
                        if comparr[i-1][j] != 1:
                            entry.append(comparr[i-1][j])
                        if comparr[i][j-1] != 1:
                            entry.append(comparr[i][j-1])
                    elif i == nrows-1 and j != 0:
                        if comparr[i][j-1] != 1:
                            entry.append(comparr[i][j-1])
                        if comparr[i][j+1] != 1:
                            entry.append(comparr[i][j+1])
                        if comparr[i-1][j] != 1:
                            entry.append(comparr[i-1][j])
####  MIDDLE #####
                else:
                    if comparr[i+1][j] != 1:
                        entry.append(comparr[i+1][j])
                    if comparr[i][j+1] != 1:
                        entry.append(comparr[i][j+1])
                    if comparr[i-1][j] != 1:
                        entry.append(comparr[i-1][j])
                    if comparr[i][j-1] != 1:
                        entry.append(comparr[i][j-1])
                neighbors.append(entry)
    neighbors = dict(zip(non_ones,neighbors))
    #print(neighbors)

#MAKE A VISITED AND PATH LIST
    visited = [comparr[0][0]]
    path = [comparr[0][0]]
    i = 0
    j = 0
    start = comparr[i][j]
    end = comparr[nrows-1][ncols-1]
    if neighbors[start] != None:
        while path[-1] != end:
            if any(neighbor not in visited for neighbor in neighbors[path[i]]):
                aux = []
                for neighbor in neighbors[path[i]]:
                    if neighbor not in visited:
                        aux.append(neighbor)
                if len(aux) > 1:
                    rand_idx = random.randint(0, len(aux)-1) 
                    path_addition = aux[rand_idx]
                    path.append(path_addition)
                    visited.append(path_addition)
                else:
                    path.append(aux[0])
                    visited.append(aux[0])
                i += 1
            else:
                path.pop(-1)         
                i -= 1
    print(neighbors)
    return path

            
        
               



        
    




                    


                
                                     
    

m = [[0,0,0,0],
    [0,1,1,1],
    [0,0,0,0],
    [0,1,0,1],
    [0,1,0,0]]
#print(solve_maze(m))
m2 = [[0,0,0,1,1,1,1,1],
    [1,0,1,0,0,0,0,0],
    [0,0,0,0,1,1,1,1],
    [0,1,1,1,1,1,1,1],
    [0,0,0,1,1,0,1,1],
    [0,0,0,1,0,1,1,1],
    [0,1,0,1,0,1,1,1],
    [0,1,1,1,0,0,0,0],
    [0,0,0,0,0,1,1,0]]
print(solve_maze(m2))



