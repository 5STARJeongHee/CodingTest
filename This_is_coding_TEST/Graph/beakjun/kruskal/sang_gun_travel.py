# https://www.acmicpc.net/problem/9372

import sys
input = sys.stdin.readline

t = int(input())
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
    

for _ in range(t):
    n,m = map(int,input().rstrip().split())
    parent = [i for i in range(n+1)]
    cnt = 0
    for _ in range(m):
        a,b = map(int,input().rstrip().split())
        if find(a) != find(b):
            union(a,b)
            cnt += 1
    print(cnt)
