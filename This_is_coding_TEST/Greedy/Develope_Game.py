# N E S W 이동 방향
x = [0, 1, 0, -1]
y = [-1, 0, 1, 0]


N, M = map(int, input().split())
c_loc = list(map(int, input().split()))

map_info = [[0 for col in range(M)] for row in range(N)]

for i in range(N):
    map_info[i] = list(map(int, input().split()))

#방문 기록
visit = map_info.copy()

# 첫 방문은 현제 위치, 4방이 막혔는지 체크용
result = 1
state = 0
visit[c_loc[0]][c_loc[1]] = 1

while True:
    #step 1 - 현제에서 왼쪽 방향 계산
    d = (4 + (c_loc[2] -1))%4
    #step 2 - 왼쪽에 갈 수 있다면 가고 아니면 방향만 왼쪽으로
    # 현제 코드 단점 : 반복되는 코드가 많다. 하나의 변수에 넣어서 사용하는게 좋다.
    # 반복되던 걸 변수로 정리하여 넣어줌 - 가독성 ++
    nx = c_loc[0] + x[d]
    ny = c_loc[1] + y[d]
    if visit[nx][ny] == 0 and state < 4:
        visit[nx][ny] = 1
        c_loc[0] = c_loc[0] + x[d]
        c_loc[1] = c_loc[1] + y[d]
        c_loc[2] = d
        result += 1
        state = 0
    elif visit[nx][ny] == 1 and state < 4:
        c_loc[2] = d
        state += 1
        #step 3 - 모든 방향이 막혀서 뒤로 가거나 갈 수도 없다면 끝냄
    else:
        bx = c_loc[0] + x[(c_loc[2] + 2)%4]
        by = c_loc[1] + y[(c_loc[2] + 2)%4]
        if map_info[bx][by] == 1:
            break
        else:
            c_loc[0] = bx
            c_loc[1] = by
    print(visit)
print(result)