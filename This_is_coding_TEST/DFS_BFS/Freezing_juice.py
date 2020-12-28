# 4 5
# 0 0 1 1 0
# 0 0 0 1 1
# 1 1 1 1 1
# 0 0 0 0 0
N, M = map(int, input().split())

ice_map = []
# 얼음 틀 초기화
for i in range(N):
    ice_map.append(list(map(int,input().split())))

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

print(dfs(0,0))
# # 모든 노드에 대하여 음료수 채우기
# result = 0
# for i in range(N):
#     for j in range(M):
#         if dfs(i, j ) == True:
#             result += 1
# print(result)