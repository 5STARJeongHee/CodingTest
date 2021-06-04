from collections import deque
def bfs(g,s_list):
    x_dir = [0,0,1,-1]
    y_dir = [1,-1,0,0]    
    q = deque(s_list)
    max_dates = 1
    while q:
        temp = q.popleft()
        for i in range(4):
            mx = temp[0] + x_dir[i]
            my = temp[1] + y_dir[i]
            if 0<= mx < N and 0 <= my < M and g[mx][my] == 0:
                g[mx][my] = g[temp[0]][temp[1]] + 1
                q.append((mx,my))
                max_dates = g[mx][my]
    for i in range(N):
        for j in range(M):
            if g[i][j] == 0:
                return -1
    return max_dates - 1

M,N = map(int,input().split())
tomatoes = []
for i in range(N):
    tomatoes.append(list(map(int, input().split())))

ripen_tomatoes = []

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            ripen_tomatoes.append((i,j))

result = bfs(tomatoes, ripen_tomatoes)
print(result)



