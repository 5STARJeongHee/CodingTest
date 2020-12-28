# 그리드 문제
# N개의 동전을 가지고 만들 수 없는 금액 중 최소액은 어떤 것인가?
# 3원, 2원, 1원, 1원, 9원 -> 만들 수 없는 최소액은 8원
# 1원, 2원, 3원, 4원, 5원, 6원, 7원, 9원

N = int(input())

coins = list(map(int, input().split()))
#화폐 단위 1부터 시작
coins.sort()
print(coins)

target = 1
now = 0
# 오름차순으로 정렬된 화폐로 target -1 까지 만들 수 있다고 가정하고,
# target의 화폐를 만들 수 있나 확인하는 방법으로 진행

for i in coins:

    if target < i: # 현재 target을 만들 수 있는가? 
                   # 현재는 target-1까지 만들 수 있다고 봄
                   # 가져온 화폐가 target보다 커버리면 target을 
                   # 만들지 못하고 넘어버리므로 지금의 target이 답이됨 
        break
    target += i # 현재 target 까지 만들 방법을 찾았고 
                # 가져온 화폐와의 조합으로 target + i -1 까지는 
                # 구할 수 있다. 다음 타겟을 업데이트



print(least)


