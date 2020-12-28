up = [0,-1]
down = [0,1]
left = [-1,0]
right = [1,0]

start = [1,1]

N = int(input())
command = list(map(str, input().split()))

for c in command:
    if c == 'R':
        start[0] = start[0] + right[0]
        if start[0] > N:
            start[0] = start[0] + left[0]
    if c == 'L':
        start[0] = start[0] + left[0]
        if start[0] < 1:
            start[0] = start[0] + right[0]
    if c == 'U':
        start[1] = start[1] + up[1]
        if start[1] < 1:
            start[1] = start[1] + down[1]
    if c == 'D':
        start[1] = start[1] + down[1]
        if start[1] > N:
            start[1] + up[1]
print(start)
########################################### 위가 나의 풀이
# N 을 입력받기
# n = int(input())
# x, y = 1, 1
# plans = input().split()

# # L, R, U, D 에 따른 이동 방향

# dx = [0 , 0, -1 , 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L','R','U','D' ]

# # 이동 계획을 하나씩 확인
# for plan in plans:
#     # 이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 공간을 벗어나는 정우 무시
#             if nx < 1 or ny < 1 or nx > n or ny > n:
#                 continue
#             # 이동 수행
#             x, y = nx, ny
# print(x, y) 