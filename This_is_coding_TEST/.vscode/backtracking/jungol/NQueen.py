# N X N 크기의 정방형 체스판이 주어졌다. 

# 우리는 거기에 N개의 queen을 배치하려고 하는데, 모든 queen들은 서로 잡아먹을 수 없어야 한다. 

# 그렇다면 queen들을 어떻게 배치해야만 할까? 
import sys

N = int(sys.stdin.readline().rstrip())
cnt = 0
board = [0] * N

def promising(cdx):
    for i in range(cdx): # board[cdx] 열비교, cdx - i 행 비교 == 열이 같거나 행과 열이 동시 같으면 퀸의 경로상에 있다는 말임
        if board[cdx] == board[i] or cdx - i == abs(board[cdx] - board[i]):
            return False
    return True

def nqueen(cdx):
    if cdx == N: # N개를 놓음 방법 카운트 1 추가 한다
        global cnt
        cnt +=1
        return
    
    for i in range(N): # cdx - 행, i 열
        board[cdx] = i # 퀸 두기 - 유망성 실패시 여기로 와서 현제 행에서 다른 퀸을 둔다
        if promising(cdx): # 현제 둔 퀸 위치의 유망성 검사를 함 
            nqueen(cdx + 1) # 성공이면 현제 퀸을 두고 다음 퀸 두기로 넘어간다


nqueen(0)
print(cnt)
