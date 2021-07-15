# https://www.acmicpc.net/problem/1197
import sys
import heapq  
input = sys.stdin.readline

def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]
def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n,m = map(int,input().rstrip().split())
parent = [i for i in range(n+1)]
edges = []
for _ in range(m):
    a,b,c = map(int,input().rstrip().split())
    heapq.heappush(edges,(c,a,b))
result = 0
while edges:
    c,a,b = heapq.heappop(edges)
    if find(a) != find(b):
        union(a,b)
        result += c
print(result)