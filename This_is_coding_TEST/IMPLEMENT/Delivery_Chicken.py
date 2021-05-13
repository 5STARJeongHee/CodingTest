import math
from itertools import combinations
# 집들과 치킨집과의 최소 치킨 거리 구하기
def calDistance(home, chk):
    result = []
    temp = 1000
    for i in home:
        for j in chk:
            dist = abs(i[0]-j[0]) + abs(i[1]-j[1])
            if temp > dist:
                temp = dist
        result.append(temp)
        temp = 1000
    return sum(result)

n, m = map(int, input().split())
city = []
for i in range(n):
    city.append(list(map(int, input().split())))
home = []
chk = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i,j]) # 집의 위치 배열
        elif city[i][j] == 2:
            chk.append([i,j]) # 치킨 집 위치 배열

a = []
for j in list(combinations(chk,m)): # 치킨 집 중 m개만 선택
    a.append(j)
chk_distance = []

for i in a:
    chk_distance.append(calDistance(home,i)) # 선택된 치킨 집과의 최소 치킨 거리를 계산하여 거리 저장

print(min(chk_distance)) # 계산된 거리중 가장 적은 거리를  선택




    
