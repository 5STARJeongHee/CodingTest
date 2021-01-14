N = int(input())
P = list(map(int, input().split()))
P.sort()
s = 0
ret = 0
for i in P:
    s += i
    ret += s
print(ret)