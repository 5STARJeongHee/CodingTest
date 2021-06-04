# https://www.acmicpc.net/problem/15650
N,M = map(int, input().split())

k = [i for i in range(1,N+1)]

def perm(lst, M):
    ret = []

    if len(lst) < M:
        return ret

    if M == 1:
        for i in lst:
            ret.append([i])
    elif M > 1:
        for i in range(len(lst)):
            temp = [j for j in lst]
            temp.remove(lst[i])
            for p in perm(temp, M-1):
                if lst[i] < p[0]:
                    ret.append([lst[i]] + p)
    return ret

result = perm(k,M)

for i in result:
    for j in i:
        print(j,end=' ')
    print()
            