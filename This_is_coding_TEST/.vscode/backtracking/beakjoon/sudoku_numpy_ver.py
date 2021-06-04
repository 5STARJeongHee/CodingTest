import numpy as np

sudoku = []
for i in range(9):
    sudoku.append(list(map(int,input().split())))

sudoku = np.array(sudoku)
tree = []
for i in range(9):
    for j in range(9):
        if sudoku[i,j] == 0:
            tree.append((i,j))
def check(m,y,x,d):
    x_group = x//3
    y_group = y//3
    if d in m[y,:] or d in m[:,x] or d in m[y_group*3:y_group*3 + 3,x_group*3:x_group*3 + 3]:
        return False
    return True

def dfs(graph,m):
    if 0 not in m:
        return
    for i in range(len(graph)):
        print(graph[i])
        for k in range(1,10):
            if check(m,graph[i][0],graph[i][1],k):
                m[graph[i][0],graph[i][1]] = k
                dfs(graph[i+1:],m)

dfs(tree, sudoku)

for i in sudoku:
    print(' '.join(map(str,i)))

    
        



