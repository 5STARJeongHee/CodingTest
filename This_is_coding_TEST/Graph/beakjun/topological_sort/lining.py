import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().rstrip().split())

indgree = [0] *(n+1)
q = deque()
graph = [[] for _ in range((n+1))]

for i in range(m):
    a,b = map(int, input().rstrip().split())
    graph[a].append(b)
    indgree[b] += 1
# 진입 차수 0인거 넣기
for i in range(1,n+1):
    if indgree[i] == 0:
        q.append(i)

result = []

while q:
    node = q.popleft()
    result.append(node)
    for i in graph[node]:
        indgree[i] -= 1
        if indgree[i] == 0:
            q.append(i)
s = ''
for i in result:
    s += str(i) +' '
print(s)

