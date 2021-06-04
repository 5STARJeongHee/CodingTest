# https://www.acmicpc.net/problem/2667
from collections import deque
n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, list(input()))))

def bfs(g,s,num):
    x_dir = [0,0,1,-1]
    y_dir = [1,-1,0,0]
    g[s[0]][s[1]] = num + 1
    q = deque([s])
    cnt = 1
    while q:
        temp = q.popleft()
        for i in range(4):
            mx = temp[0] + x_dir[i]
            my = temp[1] + y_dir[i]
            if 0 <= mx <n and 0 <= my <n and g[mx][my] == 1:
                g[mx][my] = num + 1
                q.append((mx,my))
                cnt += 1
    return cnt


number = 0
result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            number += 1
            result.append(bfs(graph,(i,j),number))
result.sort()
print(len(result))
for i in result:
    print(i)
