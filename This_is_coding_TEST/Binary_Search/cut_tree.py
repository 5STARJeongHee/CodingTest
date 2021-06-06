import sys

def bsearch(lst,t):
    start = 0
    end = lst[0]
    result = []
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for i in lst:
            if i >= mid:
                temp += (i - mid)
        if temp >= t:
            result.append(mid)
            start = mid + 1
        else:
            end = mid - 1
    result.sort(reverse=True)

    return result[0]

N,M = map(int,sys.stdin.readline().rstrip().split())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))

n_list.sort(reverse=True)
print(bsearch(n_list,M))