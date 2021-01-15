import sys
N = int(input())
d = list(map(int, input().split()))
c = list(map(int, input().split()))


min_cost = c[0]
total = 0
for i in range(len(d)):
    if min_cost > c[i]:#시작:첫 가격그대로, 내려가는 순간 그가격으로
        min_cost = c[i]
    total += (min_cost * d[i])
print(total)

# min_cost = 0
# cur = 0
# length = len(c)
# while cur != length-1:    
#     next = length-1
#     for j in range(cur+1, length-1):#다음 최소 비용의 도시
#         if c[cur] > c[j]:
#             next = j
#             break
#     for k in range(cur,next):#비용계산
#         min_cost += c[cur]*d[k]
#     cur = next
# print(min_cost)