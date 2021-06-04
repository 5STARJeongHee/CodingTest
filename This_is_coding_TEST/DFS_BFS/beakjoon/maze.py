# https://www.acmicpc.net/problem/2178
from collections import deque
N,M = map(int,input().split())
maze = []
for i in range(N):
    maze.append(list(map(int, list(input()))))

def bfs(g,s):
    x_dir = [0,0,1,-1]
    y_dir = [1,-1,0,0]    
    g[s[0]][s[1]] += 1
    q = deque([s])

    while q:
        temp = q.popleft()
        for i in range(4):
            mx = temp[0] + x_dir[i]
            my = temp[1] + y_dir[i]
            if 0<= mx < N and 0 <= my < M and g[mx][my] == 1:
                g[mx][my] = g[temp[0]][temp[1]] + 1
                q.append((mx,my))
bfs(maze,(0,0))
print(maze[N-1][M-1]-1)
            
