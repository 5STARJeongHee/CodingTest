import sys
from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    rank = list(map(int,input().split()))
    m = int(input())

    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    dq = deque()
    result = []
    # 이미 결정된 기존 그래프로 형태를 잡아줌
    for i in range(n-1):
        graph[rank[i]] = rank[i+1:]
        indegree[rank[i+1]] = i + 1 
    # 새로 결정된 상대 순위를 통해 기존 그래프, 진입 차수 변경
    for _ in range(m):
        a,b = map(int,input().split())
        
        if b in graph[a]:
            graph[b].append(a)
            graph[a].remove(b)
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a].append(b)
            graph[b].remove(a)
            indegree[b] += 1
            indegree[a] -= 1
    for j in rank:
        if indegree[j] == 0:
            dq.append(j)

    while dq:
        temp = dq.popleft()
        result.append(temp)
        for c in graph[temp]:
            indegree[c] -= 1
            if indegree[c] == 0:
                dq.append(c)
        
    if len(result) == n:
        s = ""
        for i in result:
            s += str(i) +" "
        print(s)
    else:
        print("IMPOSSIBLE")
