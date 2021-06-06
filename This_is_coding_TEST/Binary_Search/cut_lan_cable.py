# https://www.acmicpc.net/problem/1654

import sys

def bsearch(lst,t):
    result = []
    start = 1
    end = lst[0]
    while start <= end:
        mid = (start + end) // 2

        temp = 0
        for i in lst:
            temp += (i // mid)
        
        if temp >=t:
            result.append(mid)
            start = mid + 1
        else:
            end = mid - 1
    result.sort(reverse = True)
    return result[0]

K,N= map(int,sys.stdin.readline().rstrip().split())
k_list = []
for i in range(K):
    k_list.append(int(sys.stdin.readline().rstrip()))
k_list.sort(reverse=True)
print(bsearch(k_list,N))