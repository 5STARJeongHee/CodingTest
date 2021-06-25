import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
v,e = map(int, input().rstrip().split())

graph = [[] for _ in range(v+1)]


for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int, input().split())
def dijkstra(start, end):
    distance = [INF] * (v+1)
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    
    while q:
        dist, cur = heapq.heappop(q)

        if cur == end:
            return dist
        if dist > distance[cur]:
            continue
        for node in graph[cur]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q,(cost,node[0]))
    return -1

dist1 = dijkstra(1,v1)
dist2 = dijkstra(1,v2)
dist3 = dijkstra(v1,v2)
dist4 = dijkstra(v1,v)
dist5 = dijkstra(v2,v)

if -1 in [dist1,dist2,dist3,dist4,dist5]:
    if -1 in [dist1,dist3,dist5] and -1 not in [dist2,dist3,dist4]:
        print(dist2+dist3+dist4)
    elif -1 in [dist2,dist3,dist4] and -1 not in [dist1,dist3,dist5]:
        print(dist1+dist3+dist5)
    else: print(-1)
else:
    print(min(dist1+dist3+dist5,dist2+dist3+dist4))