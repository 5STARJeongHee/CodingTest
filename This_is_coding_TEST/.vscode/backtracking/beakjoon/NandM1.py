# https://www.acmicpc.net/problem/15649
N,M = map(int, input().split())

k = [i for i in range(1,N+1)]

def permutation(lst, M):
    ret = []

    if len(lst) < M:
        return ret

    if M == 1:
        for i in lst:
            ret.append([i])
    elif M > 1:
        for i in range(len(lst)):
            temp = [i for i in lst]
            temp.remove(lst[i])
            for p in permutation(temp,M-1):
                ret.append([lst[i]] + p)
    return ret

result = permutation(k,M)
for i in result:
    for j in i:
        print(j,end=' ')
    print()

    

    
    




