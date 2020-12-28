# 예시 입력
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque

N, M = map(int, input().split())

maze = []
#움직임을 위한 방향 상하 좌우 
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 지도 생성
for i in range(N):
    maze.append(list(map(int, input())))
print(maze)
# for i in range(N):
#     temp_str = input()
#     temp_int = []
#     for j in range(M):
#         temp_int.append(int(temp_str[i]))
#     maze.append(temp_int)



# 1,1 에서 N,M까지 이동하는 최소 거리를 구하는 문제, 
# bfs의 경우 끝에 다다른 경로가 최단임을 알 수 있음(가까운것 부터 차근 차근 다가가기 때문)
# dfs 일 경우 최단 경로가 아니더라도 끝까지 갔다가 다른 경로를 탐색함
x = 0
y = 0

def bfs(y,x):
    queue = deque()
    queue.append((x,y))
    
    while queue:#큐가 빌때까지
        x,y = queue.popleft()
        
        # 4방향
        for i in range(4):        
            nx = x + dx[i]
            ny = y + dy[i]

            if ny <0 or ny >=M or nx < 0 or nx >=N: #외벽
                continue
            # 벽
            if maze[nx][ny] == 0:
                continue
            
            if maze[nx][ny] == 1:#첫 방문지 첫방문지가 아니면 거리값임

                maze[nx][ny] = maze[x][y] + 1 # 방문 처리 및 현제에서 다음 노드까지 거리 추가
                # 다음 노드
                queue.append((nx,ny)) 
            
        
    return maze[N-1][M-1]

print(bfs(0,0))    
