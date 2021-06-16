# https://www.acmicpc.net/problem/11054
import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

dp = [1] * 1001
for i in range(1,n): # 가장 긴 수열을 찾는다.
    for idx in range(i):
        if arr[idx] < arr[i]:
            dp[i] = max(dp[i],dp[idx] + 1)

for i in range(1,n): # 가장 긴 수열이 찾아진 상황에서 작은 수열을 찾으면 긴수열에 이어 붙인 작은 수열까지의 길이가 최대인 것으로 업데이트됨
    for idx in range(i):
        if arr[idx] > arr[i]:
            dp[i] = max(dp[i],dp[idx] + 1)
print(max(dp))
