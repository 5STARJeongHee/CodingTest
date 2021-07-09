# https://www.acmicpc.net/problem/1976
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b
    
    
n = int(input())
m = int(input())
city = []
for i in range(n):
    city.append(list(map(int, input().split())))

test = list(map(int, input().split()))

parent = [i for i in range(201)]

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            union(i,j)
p = parent[test[0]-1]
status = 0
for i in test:
    if p != parent[i-1]:
        print("NO")
        status = 1
        break
if status == 0:
    print("YES")
