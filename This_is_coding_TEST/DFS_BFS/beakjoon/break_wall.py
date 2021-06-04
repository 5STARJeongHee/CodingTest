# https://www.acmicpc.net/problem/2206
from collections import deque
import copy
import sys
# 최단 거리를 찾는 문제인데, 최단 거리 도중 벽을 부셔서 최단거리가 된다면
# 하나의 벽은 부서도 된다는 문제다.
# 해당 문제의 핵심은 
# 3차원 배열로 벽을 하나 부순 방문 지도와 벽을 하나도 부수지 않은 방문지도
# 2개로 탐색해나가는 것
# 벽을 부수지 않은 배열에서 벽을 만날 때마다 벽을 부순배열에 해당 벽을 부쉈다면 
# 최단 거리를 써주고 해당 좌표로 벽을 부순 것을 큐에 추가 하면 
# 벽을 부순 배열에서도 BFS가 동작한다.

N,M = map(int,sys.stdin.readline().rstrip().split())
maze = []
for i in range(N):
    maze.append(list(map(int, list(sys.stdin.readline().rstrip()))))
x_dir = [0,0,1,-1]
y_dir = [1,-1,0,0]

def bfs(g,s):#v[2][N][M] 방문 지도 2장을 만듬
    v = [[[0 for i in range(M)] for j in range(N)] for k in range(2)]
    v[1][s[0]][s[1]] = 1 # 첫칸은 일단 방문했다고 함
    v[0][s[0]][s[1]] = 1
    q = deque()
    q.append((1,s[0],s[1])) # 1이 벽을 부수지 않은 지도, 0이 벽을 부순 지도
    while q:
        temp = q.popleft()
        print(temp)
        if temp[1] == N-1 and temp[2] == M-1:
            return v[temp[0]][temp[1]][temp[2]]

        for i in range(4):
            mx = temp[1] + x_dir[i]
            my = temp[2] + y_dir[i]
            if  mx <0 or mx >= N or my <0 or my >= M:
                continue
            if temp[0] and g[mx][my] == 1: 
                # 벽을 부수지 않은 경우, 
                # 벽을 만났다면 벽을 부순 지도에 새로운 경우의 최단 거리 추가
                v[temp[0]-1][mx][my] = v[temp[0]][temp[1]][temp[2]] + 1
                q.append((temp[0]-1,mx,my))
            elif g[mx][my] == 0 and v[temp[0]][mx][my] == 0: 
                #벽을 부순 경우라면 벽을 부순 배열의 최단거리 갱신,
                #벽을 부수지 않은 경우라면 벽을 안 부순 배열의 최단 거리 갱신
                v[temp[0]][mx][my] = v[temp[0]][temp[1]][temp[2]] + 1
                q.append((temp[0],mx,my))
        for i in v[0]:
            print(i)
        print()
    return -1           
result = bfs(maze,(0,0))
print(result)