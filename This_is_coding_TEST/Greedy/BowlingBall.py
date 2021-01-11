N, M = map(int, input().split())
K = list(map(int, input().split()))


K.sort()
def comb(lst, n):
    ret = []

    if n > len(lst):
        return ret
    
    if n == 1:
        for i in lst:
            ret.append([i])
        

    elif n > 1:
        for i in range(len(lst)-n+1):
            for temp in comb(lst[i+1:],n-1):
                ret.append([lst[i]]+temp)
    return ret

result = comb(K,2)

s = set()

for i in result:
    if i[0] == i[1]:
        result.remove(i)
    s.add(tuple(i)) # set에 리스트 넣는 법

print(s)
print(len(result))

