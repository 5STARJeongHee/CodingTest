# https://www.acmicpc.net/problem/2579
N = int(input())
stairs = []
for i in range(N):
    stairs.append(int(input()))
d = [0]*301
if N <= 2:
    print(sum(stairs))
else:
    d[1] = stairs[0]
    d[2] = d[1] + stairs[1]
    for i in range(3,N+1):
        d[i] = max(stairs[i-2]+d[i-3],d[i-2]) + stairs[i-1]
    print(d[N])
