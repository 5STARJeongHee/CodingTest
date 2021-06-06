# https://www.acmicpc.net/problem/1920
import sys
def bsearch(lst, target):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) //2
        if lst[mid] == target:
            return 1
        elif lst[mid] < target:
            start = mid +1
        else:
            end = mid -1
    return 0

N = int(sys.stdin.readline().rstrip())
s_lst = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
t_lst = list(map(int, sys.stdin.readline().rstrip().split()))

result = []
s_lst.sort()
for i in t_lst:
    result.append(bsearch(s_lst,i))

for i in result:
    print(i)

        