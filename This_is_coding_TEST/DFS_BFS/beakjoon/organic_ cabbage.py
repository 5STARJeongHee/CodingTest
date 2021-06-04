# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10000)
test_case = int(input())

x_dir = [0,0,1,-1]
y_dir = [1,-1,0,0]

def dfs(g,s,num):
    g[s[0]][s[1]] = num + 1
    for i in range(4):
        mx = s[1] + x_dir[i]
        my = s[0] + y_dir[i]
        if 0 <= mx < M and 0 <= my < N and g[my][mx] == 1:
            dfs(g,(my,mx),num)

for i in range(test_case):
    M,N,K = map(int, input().split())
    m = [[0]*M for i in range(N)]
    for j in range(K):
        x,y = map(int, input().split())
        m[y][x] = 1
    cnt = 0
    for j in range(N):
        for z in range(M):
            if m[j][z] == 1:
                cnt += 1
                dfs(m,(j,z),cnt)
    print(cnt)
