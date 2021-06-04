# https://www.acmicpc.net/problem/15651
from collections import deque
from sys import stdin
import sys
N,M = map(int, stdin.readline().split())

out = deque()

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        out.append(i+1)
        solve(depth+1, N, M) # depth 0 부터 M까지 그려진 가지는 출력후 pop으로 버림
        print(out.pop())
        
solve(0, N, M)

# s=''
# for i in result:
#     for j in i:
#         s += str(j)+' '
#     s += '\n'
# sys.stdout.write(s)
            