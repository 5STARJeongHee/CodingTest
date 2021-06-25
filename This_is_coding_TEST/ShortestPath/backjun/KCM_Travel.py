# https://www.acmicpc.net/board/view/40434
# 여러 글들을 읽어본 결과 파이썬만 다익스트라로 구현하지 못하고
# dp로만 풀어야하는 문제

# 아래는 다익스트라로 구현 했지만 메모리 초과가 난 풀이법
# import sys, heapq
# input = sys.stdin.readline
# INF = int(1e9)

# total = int(input())
# def dijkstra(n,m,graph,start):
#     dists = [[INF]*(m+1) for _ in range(n+1)]
    
#     dists[start][0] = 0
    
#     hq = []
#     heapq.heappush(hq,(0,0,start))

#     while hq:
#         distance, payment, cur = heapq.heappop(hq)
#         if cur == n: break
#         if dists[cur][payment] < distance: continue
#         for nxt in graph[cur]:
#             dist = distance + nxt[2]
#             cost = payment + nxt[1]
#             if cost > m: continue
#             if dists[nxt[0]][cost] > dist:
#                 dists[nxt[0]][cost] = dist
#                 heapq.heappush(hq,(dist,cost,nxt[0]))
#     return dists
# for _ in range(total):
#     n,m,k = map(int, input().rstrip().split())
    
#     graph = [[] for _ in range(n+1)]
#     for i in range(k):
#         a,b,c,d = map(int, input().split())
#         graph[a].append((b,c,d))

#     dists = dijkstra(n,m,graph,1)
    
#     if min(dists[n]) != INF:
#         print(dists[n][0])
#     else:
#         print('Poor KCM')

########
# 여기는 dp로만 푼 풀이법을 놓았음
import sys
 
T=int(input())
INF=sys.maxsize
 
for _ in range(T):
    N,M,K=map(int,sys.stdin.readline().split())#공항수,지원비용,티켓정보수
    ticket=[[] for _ in range(N+1)]
    for _ in range(K):
        u,v,c,d=map(int,sys.stdin.readline().split())#출발,도착,비용,소요시간
        ticket[u].append([v,c,d])
 
 
    DP=[[INF for _ in range(M+1)] for _ in range(N+1)]#열:비용 행:n까지갈때
    DP[1][0]=0#1->1로 갔을때 비용은0 시간도 0
 
    for c in range(M+1):
        for d in range(1,N+1):
            if DP[d][c]==INF:continue#c의 비용으로 d에 도착하는 경우가 없다면
            t=DP[d][c]#c의 비용으로 d에 도착햇을때의 소요시간
            for dv,dc,dd in ticket[d]:#d에서 출발하는 모든경우
                if dc+c>M:#비용이 초과될경우 넘어간다
                    continue
                DP[dv][dc+c]=min(DP[dv][dc+c],t+dd)#이전에 저장된값과 비교하여 작다면 갱신해준다
 
    result=min(DP[N])#N에 도착할때 최소소요시간
 
    if result==INF:
        print('Poor KCM')
    else:
        print(result)
