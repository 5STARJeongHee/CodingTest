# https://www.acmicpc.net/problem/11053
import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

dp = [1] * 10000

for i in range(1,n): # i는 현제항
    for j in range(i):
        if arr[j] < arr[i]: # j는 비교하는 이전 항들
            dp[i] = max(dp[i],dp[j] + 1) # 이전항들의 dp에서 현제항을 포함한 경우들 중 제일 큰걸 찾아냄
print(max(dp)) # 증가하지 않는 부분은 그냥 넘어 가므로 최댓값을 찾는다
# 풀이 과정
"""
가장 긴 증가 수열을 찾는 문제로
주어진 수열 A의 부분 수열 중 증가 수열로 가장 긴 것의 길이를 찾는 문제
반복적으로 수열 A의 일부를 보며 가장 긴 증가 수열을 찾아야 하므로 dp 문제로 볼 수 있음
현제 수열의 항을 보며 가장 긴 증가 수열에 넣을 수 있는가를 볼 때
바로 이전과 이전이전만 보면서 풀던 문제와 다르게 어떤 상황이 베스트가 될지 모르므로 뒤의 모든 항을 
봐야한다. 그 중 증가하는 수열 일 경우에만 현제 항에 대해서 계산 할 수 있으므로 
현제 항보다 작은 곳들에서 계산된 dp에서 현제 항을 포함할 경우 가장 긴걸 찾아서 엄데이트 해준다.
"""
