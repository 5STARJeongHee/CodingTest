N = int(input())
K = int(input())

apple_loc = []

for i in range(K):
    apple_loc.append(list(map(int, input().split())))

L = int(input())
X=[]
C=[]
for i in range(L):
    a,b = input().split()
    X.append(int(a))
    C.append(b)
    
def print_key(k):
    for i in k:
        print(i)
    print()

def snake_game(N,K,apple_loc, X, C):
    body_len = 1
    c = [1,0,-1,0] #90도씩 움직이려면 index를 움직임
    r = [0,1,0,-1]
    index = 0 # 첫 방향은 오른쪽

    # 게임판 제작
    board = [[0] * N for _ in range(N)]
    for i in apple_loc:
        board[i[0]-1][i[1]-1] = 2
    
    # 게임말 두기
    board[0][0] = 1
    head_loc = [0,0]
    body = []
    body.append([0,0])
    dir = 0
    time = 0
    while True:
        time += 1 # 시간 시작

        head_loc[0] += r[dir] # 현재 방향으로 머리 늘리기
        head_loc[1] += c[dir] # 현재 방향으로 머리 늘리기

        body.append(head_loc.copy()) # 늘어난 머리 추가 - copy하지 않으면 같은 주소를 가리켜서 같이 증가됨
        
        if head_loc[0] < 0 or head_loc[0] == N or head_loc[1] < 0 or head_loc[1] == N: # 게임 판 탈출시 게임 오버
            return time
            
        if board[head_loc[0]][head_loc[1]] == 2: # 사과를 만날시
            board[head_loc[0]][head_loc[1]] = 1 # 늘어난 머리를 게임판에 표시
        
        elif board[head_loc[0]][head_loc[1]] == 0: # 빈칸    
            temp = body.pop(0) # 꼬리 빼기
            board[temp[0]][temp[1]] = 0 # 꼬리 부분 게임판에서 없애기
            board[head_loc[0]][head_loc[1]] = 1 # 머리부분 게임판에 표시
        elif board[head_loc[0]][head_loc[1]] == 1: # 꼬리를 만날시 게임 끝
            return time
        # 지시 사항이 있는 동안에 시간에 따른 방향 전환
        if len(X) != 0:
            if X[0] == time:
                if C[0] == 'L':
                    dir -= 1
                    if dir == -1:
                        dir = 3
                elif C[0] == 'D':
                    dir += 1
                    dir %= 4
                C.pop(0)
                X.pop(0)
        print_key(board) # 게임판 관찰하기
print(snake_game(N,K,apple_loc, X, C))

    
