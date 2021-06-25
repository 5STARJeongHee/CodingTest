# https://www.acmicpc.net/problem/9370
# 이 문제에 최대 문제점은 g,h를 지나는 경우와 지나지 않는 경우가
# 거리가 같은 경우에 지나지 않는 경우가 먼저 업데이트 되어 g,h를 지나지 않은채 
# 진행되는 부분을 해결해야만 한다.
# 여러 사람들의 풀이들의 핵심 적인 방법들은 다음과 같다
# 1. 가중치 값을 변경 (ex - g,h에 대한 가중치 하나만 홀수, 나머지는 짝수로 바꾸어 경로가 홀수인가 아닌가에 따라 gh를 다녀왔는지 판단)
# (ex - g,h 가중치에서 0.1를 빼어 최단 경로 값이 float인 경우 gh를 다녀왔다고 판단)
# 2. isVia라는 배열을 두어 현재 경로가 g,h를 지나온 경로인지 아닌지를 체크하는 방법 (ex - 경로 업데이트 시 isVia 배열을 업데이트하여
# gh를 다녀온 경우의 경로들은 계속해서 isVia 가 True가 되도록 하며, 같은 길이의 경로 일때도 경로 갱신을 해주어 
# gh를 지나지 않은 경우를 덮어 버림) - 이거로는 해결을 못했음
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

total = int(input())
# result = ''
def dijkstra(n,graph, start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    
    while q:
        dist, cur = heapq.heappop(q)
        if dist > distance[cur]:
            continue
        for node in graph[cur]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q,(cost,node[0]))
    return distance

for _ in range(total):
    n,m,t = map(int, input().rstrip().split())
    s,g,h = map(int, input().rstrip().split())
    graph = [[] for _ in range(n+1)]
    target = []
    for i in range(m):
        a,b,c = map(int, input().split())
        if (a,b) == (g,h) or (a,b) == (h,g):
            c = c * 2 - 1
        else:
            c = c * 2
        graph[a].append((b,c))
        graph[b].append((a,c))
    for i in range(t):
        target.append(int(input()))
    target.sort()

    dists = dijkstra(n,graph,s)
    
    for t in target:
        if dists[t] % 2 == 1:
            print(t,end=' ')
    print()
