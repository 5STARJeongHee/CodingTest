# https://www.acmicpc.net/problem/2565
import sys
input = sys.stdin.readline
n = int(input().rstrip())
lines = [-1] * 501
max_line = 0
for i in range(n):
    a,b = map(int, input().split())
    max_line = max(a,b,max_line)
    lines[a] = b
dp = [1] * 501
# 문제 풀이의 최대 힌트는 현제 전기줄에서 이전 전기줄과 겹치지 않는 최대 수를 구하는 것         
for i in range(2,max_line+1):
    for j in range(i):
        if lines[i] != -1 and lines[j] != -1:
            if lines[i] >lines[j]:
                dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
        
