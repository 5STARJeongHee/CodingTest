# 다익스트라 알고리즘을 적용하는 문제
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n,m,c = map(int, input().rstrip().split())

graph = [[] for _ in range(n+1)]

dist = [INF] * (n+1)
for _ in range(m):
    a,b,d = map(int,input().rstrip().split())
    graph[a].append((b,d))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dist[start] = 0
    while q: # q가 비어있지 않다면
        d, now = heapq.heappop(q)

        if dist[now] < d:#
            print('hi')
            continue
        for i in graph[now]:
            cost = d + i[1]

            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)
cnt = 0
t = 0
print(dist)
for i in dist:
    if i != INF and i > 0:
        cnt += 1
        t = max(t,i)
print(cnt,t)
