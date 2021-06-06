# https://www.acmicpc.net/problem/1300
def bsearch(lst,target):
    start  = 1
    end = N*N
    min_value = 1000000001
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for i in range(1,N+1):
            temp += min(mid//i,N) # i 번째 행에서 mid보다 작은 개수- i*j - > j개, i행에서 N보다 클수 없으므로 넘어가면 N개
        if temp < target:
            start = mid + 1
        else:
            if min_value > mid:
                min_value = mid
            end = mid - 1
    return min_value

N = int(input())
k = int(input())
B = []

print(bsearch(N,k))
