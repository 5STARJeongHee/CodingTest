# 정수 x를 1로 만들기까지 4가지 연산만 가능, 연산 횟수 최솟값을 구하세요
from collections import deque
x = int(input())

q = deque()
q.append((x,0))
result = 0
while q:
    temp = q.popleft()
    print(temp)
    if temp[0] == 1:
        result = temp[1]
        break
    if temp[0] % 2 == 0:
        q.append((temp[0]//2,temp[1] + 1))
    if temp[0] % 3 == 0:
        q.append((temp[0]//3,temp[1] + 1))
    if temp[0] % 5 == 0:
        q.append((temp[0]//5,temp[1] + 1))
    if temp[0] - 1 != 0:
        q.append((temp[0] - 1, temp[1] + 1))

print(result)

# 이것이 코테 답안
x = int(input())

d = [0] * 30001

for i in range(2, x+1): # 바텀업 방식(작은 거부터 큰거까지- 반복문)
    d[i] = d[i - 1] + 1 # 1빼는 방식은 이전 dp배열에서 1씩 카운트

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1) # 앞에서 2로 나눠떨어진 수가 있다면 해당 수의 방식에서 카운트한 값을 가져옴
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] == min(d[i], d[i//5] + 1)
print(d[x])