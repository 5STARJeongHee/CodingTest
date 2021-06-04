from collections import deque
N = int(input())
c = int(input())

network = [[] for i in range(N)]
for i in range(c):
    a,b = map(int, input().split())
    network[a-1].append(b-1)
    network[b-1].append(a-1)  

for i in network:
    i.sort()  

def bfs(g, s=1):
    v = [False for i in range(N)]
    v[s-1] = True

    q = deque([s-1])
    cnt = 0
    while q:
        temp = q.popleft()
        for i in g[temp]:
            if v[i] == False:
                q.append(i)
                v[i] = True
                cnt += 1
    return cnt

print(bfs(network))