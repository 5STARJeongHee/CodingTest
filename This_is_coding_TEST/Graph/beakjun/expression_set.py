# https://www.acmicpc.net/problem/1717
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5) # 재귀로 인한 런타임 에러시 재귀 리밋 해제, 메모리 초과문제
n, m = map(int, input().rstrip().split())

parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a

for _ in range(m):
    o, a, b = map(int, input().rstrip().split())
    if o:
        if parent[a] == parent[b]:
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)
        
    