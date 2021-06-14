# https://www.acmicpc.net/problem/1463
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
x = int(input())
d = [0] * 1000001
for i in range(2,x+1):
    cur = i
    minimum = 1000001
    if cur % 3 == 0:
        if d[cur//3] < minimum:
            minimum = d[cur//3]
    if cur % 2 == 0:
        if d[cur//2] < minimum:
            minimum = d[cur//2]
    if d[cur-1] < minimum:
        minimum = d[cur-1]
    
    d[i] = minimum + 1

print(d[x])
