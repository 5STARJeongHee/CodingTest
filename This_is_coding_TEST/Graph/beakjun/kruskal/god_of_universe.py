# https://www.acmicpc.net/problem/1774
import sys
import heapq
from itertools import combinations  
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

def calc_dist(u,v):
    return ((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2) ** 0.5

n,m = map(int,input().rstrip().split())
parent = [i for i in range(n+1)]
points = []
edges = []
for _ in range(n):
    x,y = map(int,input().rstrip().split())
    points.append((x,y))
temp = []
for _ in range(m):
    a,b = map(int,input().rstrip().split())
    dist = calc_dist(points[a-1],points[b-1])
    heapq.heappush(edges,(dist,a,b))


while edges:
    d,a,b = heapq.heappop(edges)
    if find(a) != find(b):
        union(a,b)


comb = list(combinations([i+1 for i in range(n)],2))
for i in comb:
    dist = calc_dist(points[i[0]-1],points[i[1]-1])
    heapq.heappush(edges,(dist,i[0],i[1]))
result = 0
while edges:
    d,a,b = heapq.heappop(edges)
    if find(a) != find(b):
        union(a,b)
        result += d

print(f'%.2f'%(result))