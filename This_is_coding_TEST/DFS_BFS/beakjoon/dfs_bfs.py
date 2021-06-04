# https://www.acmicpc.net/problem/1260
from collections import deque
N,M,v = map(int, input().split())

datas = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int, input().split())
    datas[a-1].append(b-1)
    datas[b-1].append(a-1)

for i in datas:
    i.sort()    
def dfs(g, s):
    v = [False for i in range(N)]
    q = deque([s-1])
    while q:
        temp = q.pop()
        if v[temp] == False:
            v[temp] = True
            print(temp+1, end=' ')
        for i in g[temp][-1::-1]:
            if not v[i]:
                q.append(i)
# def dfs(g,s,visit):
#     visit[s] = True
#     print(s+1,end=' ')
#     for i in g[s]:
#         if visit[i] == False:
#             dfs(g,i,visit)

def bfs(g, s):
    v = [False for i in range(N)]
    v[s-1] = True
    q = deque([s-1])
    while q:
        temp = q.popleft()
        print(temp+1, end=' ')
        for i in g[temp]:
            if not v[i]:
                v[i] = True
                q.append(i)
            
visited = [0 for i in range(N)]
# dfs(datas,v-1,visited)
dfs(datas,v)
print()
bfs(datas,v)
