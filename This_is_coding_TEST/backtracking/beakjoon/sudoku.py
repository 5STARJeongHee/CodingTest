# https://www.acmicpc.net/problem/2580
def check(m,y,x,d):
    x_group = x//3
    y_group = y//3

    for i in range(9):
        if d == m[y][i]:
            return False
        if d == m[i][x]:
            return False
    for i in range(3):
        for j in range(3):
            if d == m[y_group*3+i][x_group*3+j]:
                return False
    return True
def dfs(graph,m):
    zero = True
    for i in m:
        if 0 in i:
            zero = zero and False
    if zero == True:
        return
    for i in range(len(graph)):
        for k in range(1,10):
            if check(m,graph[i][0],graph[i][1],k):
                m[graph[i][0]][graph[i][1]] = k
                dfs(graph[i+1:],m)
sudoku = []
for i in range(9):
    sudoku.append(list(map(int,input().split())))
tree = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            tree.append((i,j))
dfs(tree, sudoku)
for i in sudoku:
    print(' '.join(map(str,i)))

    
        



