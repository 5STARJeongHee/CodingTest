from collections import deque
from sys import stdin
import sys

N,M = map(int, stdin.readline().split())

q = []

def nandm4(q, N, M):
    if len(q) == M:
        print(' '.join(map(str,q)))
        return
    
    for i in range(N):
        before = 0
        if len(q) > 0:
            before = q[len(q)-1]
            # print(before,q)
        if before <= i+1:
            q.append(i+1)
            nandm4(q,N,M)
            q.pop()

nandm4(q,N,M)