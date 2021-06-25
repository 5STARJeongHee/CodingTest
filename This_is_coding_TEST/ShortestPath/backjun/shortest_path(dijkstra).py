import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
v,e = map(int, input().rstrip().split())
start = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist, cur = heapq.heappop(q) # 거치는 노드

        if dist > distance[cur]: 
            continue
        for node in graph[cur]: # 거치는 노드의 인접 노드
            cost = dist + node[1]
            if distance[node[0]] > cost:
                distance[node[0]] = cost
                heapq.heappush(q,(cost,node[0])) # 다음에 거칠 노드로 등록

dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])

