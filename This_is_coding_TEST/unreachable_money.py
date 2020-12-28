# 그리드 문제
# N개의 동전을 가지고 만들 수 없는 금액 중 최소액은 어떤 것인가?
# 3원, 2원, 1원, 1원, 9원 -> 만들 수 없는 최소액은 8원
# 1원, 2원, 3원, 4원, 5원, 6원, 7원, 9원

N = int(input())

coins = list(map(int, input().split()))

coins.sort()
print(coins)
# 정렬된 동전을 최소 금액부터 차례대로 더해가면서 +1씩 다음 최소 금액을 정해주고
# 그 금액을 넘어버리면 만들 수 없다고도 볼 수 있다. 

least = 0

for i in range(len(coins)):
    least += 1
    if least+1 < least + i:
        least += i
    el
    



print(least)


