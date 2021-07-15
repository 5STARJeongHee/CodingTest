# https://www.acmicpc.net/problem/10451
import sys
sys.setrecursionlimit(10**6)

t = int(input())

def dfs(u):
    if visited[u]: return #dfs로 사이클 찾았는데 또 방문시
    visited[u] = True
    global cycle
    for i in graph[u]:
        if not visited[i]: 
            dfs(i)
        else: # dfs로 탐색 중 cycle 발견시 count
            cycle += 1
for i in range(t):
    n = int(input())
    graph = [[] for i in range(n+1)]
    visited = [False] * (n+1)
    dst = list(map(int, input().split()))
    cycle = 0
    
    for s in range(n+1):
        graph[s].append(dst[s-1])

    for i in range(n+1):
        dfs(i)
    print(cycle)


