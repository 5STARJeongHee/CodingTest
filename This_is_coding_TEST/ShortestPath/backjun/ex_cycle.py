# https://www.acmicpc.net/problem/1956
# 이문제는 플로이드 와샬 알고리즘을 사용하여
# 모든 정점이 모든 정점에 대한 경로 길이를 구하여
# 두 정점 사이의 편도 거리를 더했을 때 가장 적은 왕복 거리를 가진
# 것을 찾으면 된다.
# 시간이 꽤나 걸려서 python으로는 안되는 듯? pypy3 로 했음
import sys
input = sys.stdin.readline
INF = int(1e9)
v,e = map(int, input().split())
graph = [[INF]*(v+1) for _ in range(v+1)]
for i in range(1,v+1):
    graph[i][i] = 0
for i in range(e):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for k in range(1,v+1):
    for a in range(1,v+1):
        for b in range(1,v+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

result = INF
for i in range(1,v+1):
    for j in range(1,v+1):
        if i != j:
            if result > graph[i][j] + graph[j][i]:
                result = graph[i][j] + graph[j][i]
if result != INF:
    print(result)
else:
    print(-1)





