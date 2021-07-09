import sys
input = sys.stdin.readline
n,m = map(int, input().split())

def grouping(parent,a,b):
    ap = find_team(parent,a)
    bp = find_team(parent,b)
    if ap < bp:
        parent[b] = ap
    else:
        parent[a] = bp

def find_team(parent,c):
    if parent[c] != c:
        parent[c] = find_team(parent,parent[c])
    return parent[c]

graph = []
parent = [i for i in range(n+1)]
for i in range(m):
    op,a,b = map(int, input().split())

    if op == 0:
        grouping(parent,a,b)
    else:
        ap = find_team(parent,a)
        bp = find_team(parent,b)

        if ap == bp:
            print('YES')
        else:
            print('NO')