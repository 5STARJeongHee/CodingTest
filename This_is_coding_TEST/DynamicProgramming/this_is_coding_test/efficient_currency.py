n,m = map(int, input().split())
c = []
for i in range(n):
    c.append(int(input()))
c.sort()

d = [0]*10001
for i in c:
    d[i] = 1
for i in range(1, m+1):
    for j in c:
        if i - j >= 0 and d[i-j] != 0:
            d[i] = d[i-j] + 1

if d[m] == 0:
    print(-1)
else:
    print(d[m])
