N,K = map(int, input().split())
coins = []
for i in range(N):
    coins.append(int(input()))

now = len(coins) - 1
ret = 0
while K !=0:
    if K >= coins[now]:
        n = int(K/coins[now])
        K -= n*coins[now]
        ret += n
    else:
        now -= 1
print(ret)