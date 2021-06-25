# 시작 정점에서 다른 정점까지의
# 최단 거리를 찾는 알고리즘
# 다익스트라와 비슷하지만
# 다른 점은 음수 가중치가 있는 그래프에서도 적용가능하며 음수 사이클 존재의 여부를 알 수 있다.
# 또한 매 순간 짧은 거리의 인접 노드를 선택해서 이동하는 그리드 방식
# 을 사용하는 다익스트라와 달리 매번 정점수 만큼 반복
# 정점 개수가 v 일 때 시작 정점에서 다른 정점으로 가는데 필요한 
# 최대 간선 수는 v-1개 인데 특정 정점으로 가는데 필요한 간선의 개수가
# v가 되는 순간 사이클이 생겼다고 본다.
# 시간 복잡도는 O(VE)
# 1. 시작 정점을 결정한다.
# 2. 시작 정점에서 각각 다른 정점까지의 거리 값을 무한대로 초기화한다.
# 3. (시작 정점이 a라면, distance[b] = a->b의 거리를 뜻함)
# 4. 시작 정점 -> 시작 정점은 0으로 초기화한다.
# 5. 현재 정점에서 모든 인접 정점들을 탐색하며, 기존에 저장되어 있는 인접 정점까지의 거리(distance[a])보다 현재 정점을 거쳐 인접 정점에 도달하는 거리가 더 짧을 경우 짧은 거리로 갱신해준다.
# 6. 3번의 과정을 V-1번 반복한다.
# 7. 위 과정을 모두 마치고 난 후 거리가 갱신되는 경우가 생긴다면 그래프에 음수 사이클이 존재한다는 것이다. 
#
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
graph = []
dists = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph.append((a,b,c))

def bellman_ford(graph, start):
    dists[start] = 0
    for i in range(n-1): # 정점수-1 만큼 반복
        for u,v,w in graph:# 모든 간선을 살펴봄
            # 현제 정점이 연결이 되어 있고 다음 정점 v까지 거리와 현제 정점까지 거리의 v까지 거리와 비교
            # 했을 때 현제 정점에서 v까지의 거리가 짧다면 갱신   
            if dists[u] != INF and dists[u]+w < dists[v]: 
                dists[v] = dists[u]+w
    
    # 벨만포드 알고리즘은 음의 사이클 일 경우 무한 루프를 돌게 되므로 
    # 사이클의 존재 여부를 파악해야 함
    cycle = 0
    for u,v,w in graph:
        if dists[u] != INF and dists[u] + w < dists[v]:
            cycle = 1
            # 한사이클이 더 돌았음 즉 간선이 더 추가되었고
            # 이는 사이클이 있다는 점
            break
    if cycle == 0:
        for i in range(2,len(dists)):
            if dists[i] != INF:
                print(dists[i])
            else:
                print(-1)
    else:
        print(-1)
bellman_ford(graph,1)