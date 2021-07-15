def find_parent(friend):
    if parent[friend] != friend:
        parent[friend] = find_parent(parent[friend])
    return parent[friend]

def union(f1, f2):
    f1 = find_parent(f1)
    f2 = find_parent(f2)
    if f1 != f2:
        parent[f1] = f2
        set_num[f1] += set_num[f2]
        set_num[f2] = set_num[f1]
        

case = int(input())

for _ in range(case):
    parent = {}
    set_num = {}
    r = int(input())
    for i in range(r):
        f = list(map(str,input().split()))
        for i in range(2):
            if f[i] not in parent.keys():
                parent[f[i]] = f[i]
                set_num[f[i]] = 1
        union(f[0],f[1])
        print(parent)
        print(set_num[find_parent(f[0])])