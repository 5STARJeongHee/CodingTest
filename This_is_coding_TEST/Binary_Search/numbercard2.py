# https://www.acmicpc.net/problem/10816
import sys

def bsearch(lst, target):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) //2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            start = mid +1
        else:
            end = mid -1
    return False

N = int(sys.stdin.readline().rstrip())
n_lst = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
m_lst = list(map(int, sys.stdin.readline().rstrip().split()))

n_lst.sort()
n_map = {}
for i in n_lst:
    if not(i in n_map):
        n_map[i] = 1
    else:
        n_map[i] += 1
result = []
for i in m_lst:
    if bsearch(n_lst,i):
        result.append(n_map[i])
    else:
        result.append(0)
r = ''
for i in result:
    r += str(i) +' '
print(r)


