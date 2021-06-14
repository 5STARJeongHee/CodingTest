# https://www.acmicpc.net/problem/10844

N = int(input())
d= [[0] * 10 for i in range(101)]
div = 1000000000
for i in range(1,len(d[1])):
    d[1][i] = 1
for i in range(2,N+1):
    for j in range(10):
        if j == 0 :
            d[i][j] = d[i-1][j+1] % div
        elif j == 9 :
            d[i][j] = d[i-1][j-1] % div
        else:
            d[i][j] = (d[i-1][j-1] + d[i-1][j+1]) % div

print(sum(d[N])%div)