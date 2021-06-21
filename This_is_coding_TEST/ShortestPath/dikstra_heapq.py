# 그리디 알고리즘
# 하나의 노드에서 갈수 있는 노드까지의 최단 거리
# 최소 힙을 이용하여 최단 경로 선택부분을 대체한 문제
# 힙 큐에서 빠져가면 더 이상 방문하지 않기에 visited 배열은 따로 없음
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 10억

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적이 리스트를 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q: # q가 비어있지 않다면
        dist, now = heapq.heappop(q)
        print('now:',now,'dist:',dist)
        if distance[now] < dist: # 현제 노드가 이미 최단거리로 처리된적 있다면 그냥 넘어감
            print(now,dist)
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                print(q)

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
