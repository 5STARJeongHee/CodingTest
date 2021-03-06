# 플로이드 워셜 알고리즘:
# 모든 노드에서 다른 노드로 가는 최단 거리를 구함
# O(N^3) 시간이 걸림
# N개의 중간 길(k)에 대한 2 차원 배열의 모든 조합 a->k->b
# 다이나믹 프로그래밍 - 점화식 : min(D_ab,D_ak + D_kb)
INF = int(1e9)

n = int(input())
m = int(input())

# 그래프를 만들고 모두 무한으로 초기화
graph = [[INF] *(n+1) for _ in range(n+1)]
# 자기 자신에게 가는 비용은 0으로
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1): # 어딜 거치는 정점
    for a in range(1, n+1): # 현제 정점
        for b in range(1, n+1): # 다음 정점
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print() 