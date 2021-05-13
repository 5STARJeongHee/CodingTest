# 4 5
# 0 0 1 1 0
# 0 0 0 1 1
# 1 1 1 1 1
# 0 0 0 0 0
# 4 5
# 00110
# 00011
# 11111
# 00000
from collections import deque

N, M = map(int, input().split())

ice_map = []
# 얼음 틀 초기화
for i in range(N):
    a = input()
    if(len(a) == M):
        temp = []
        for j in a:
            temp.append(bool(int(j)))
        ice_map.append(temp)
# print('ice_map',ice_map)

def dfs(x,y):
    # 범위 벗어날 시 종료
    print(x,y)
    if x <=-1 or x >N-1 or y<=-1 or y >M-1:
        return False

    if ice_map[x][y] == 0:
        ice_map[x][y] = 1
        # 상하좌우
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    return False
def bfs0(ice_map,s):
    x = [-1,1,0,0]
    y = [0,0,-1,1]
    q = deque()
    q.append(s)
    ice_map[s[0]][s[1]] = True
    
    while q:
        v = q.popleft()
        print('v',v)
        for i in range(4):
            mx = v[0] + x[i]
            my = v[1] + y[i]
            if 0 <= mx < M and 0 <= my < N:
                if not ice_map[my][mx]:
                    q.append((my,mx))
                    ice_map[my][mx] = True
    return 1

def solution(N,M,ice_map):
    result = 0
    for i in range(N):
        for j in range(M):
            if ice_map[i][j] == False:
                result += bfs0(ice_map,(i,j))
    return result

print('answer',solution(N,M,ice_map))
# # 모든 노드에 대하여 음료수 채우기
# result = 0
# for i in range(N):
#     for j in range(M):
#         if dfs(i, j ) == True:
#             result += 1
# print(result)