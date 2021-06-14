import sys
n = int(sys.stdin.readline().rstrip())

wines = []
dp = [0] * 10001
for i in range(n):
    wines.append(int(sys.stdin.readline().rstrip()))
if n <= 2:
    print(sum(wines))
else:
    dp[1] = wines[0]
    dp[2] = dp[1] + wines[1]

    for i in range(3, n+1):
        dp[i] = max(dp[i-3] + wines[i-2] + wines[i-1],dp[i-2] + wines[i-1],dp[i-1])
    print(dp[n])
# 문제 해결 과정
"""
1,2 번째 와인잔은 그냥 다 더하면 되는데 3번째 부터는 연속할 수 없으므로
이 때부터 dp가 적용되는 문제가 된다.
dp 문제는 이전 항과의 관계를 찾는 문제이므로 
이전까지 골랐던 최대 와인잔들에서 현제 고르려는 와인잔들간의 관계를 찾으면 된다.
그림을 예로 들자면
dp o o o - dp가 이전, o가 와인일 때 
와인을 고르는 방법은 연속 3개의 와인을 선택하지 못하므로
dp x o o, 
dp x o, 
dp x
3가지 경우가 있고 이를 점화식으로 최대값을 찾는 방식으로 진행하면 된다.
"""


