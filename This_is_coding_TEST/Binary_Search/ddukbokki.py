import sys
"""
[] - 4k >= M
k는 [] 중에 가장 큰수 보다는 작고
0 보다는 커야됨
"""
N, M = map(int, sys.stdin.readline().rstrip().split())
d_list = list(map(int, sys.stdin.readline().rstrip().split()))

def check_target(lst,lng , target):
    sum = 0
    for i in lst:
        if lng < i:
            sum += (i - lng)
    if sum >= target:
        return True
    else:
        return False

def binaray_search(lst, start, end, target):
    result_list = []
    while start <= end:
        mid = (start + end) // 2
        if start > end:
            return None
        elif check_target(lst, mid, target):
            result_list.append(mid)
            print(result_list)
            start = mid + 1
        else:
            print(result_list)
            end = mid - 1
    result_list.sort(reverse=True)
    return result_list[0]

print(binaray_search(d_list,0,max(d_list),M))

        



"""
4 6
19 15 10 17
"""
