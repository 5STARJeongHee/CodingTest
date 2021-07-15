import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
def find(s1):
    if parent[s1] != s1:
        parent[s1] =  find(parent[s1])
    return parent[s1]
def union(s1,s2):
    s1 = find(s1)
    s2 = find(s2)
    if s1 == s2:
        return True
    parent[s1] = s2
    return False

n,m = map(int, input().rstrip().split())
parent = [i for i in range(n+1)]
result = 0
for i in range(m):
    a,b = map(int, input().rstrip().split())
    if union(a,b):
        result = i + 1
        break
    
print(result)