N = int(input())

dir_x = [0,0,1,-1]
dir_y = [1,-1,0,0]
m = []
visited = []
info = dict()

def dfs(visited, start,mark):
    if not visited[start[0]][start[1]]:
        return False
    
    visited[start[0]][start[1]] = False
    info[mark] = info.get(mark,0) + 1
    
    for i in range(4):
        mx = start[0] + dir_x[i]
        my = start[1] + dir_y[i]
        if 0 <= mx < N and 0 <= my <N:
            dfs(visited,(mx,my),mark)

    return True

for i in range(N):
    m.append(list(map(int, list(input()))))
    visited.append(list(map(bool,m[i])))

mark = 1
for i in range(N):
    for j in range(N):
        if dfs(visited,(i,j),mark):
            mark += 1

result = []
for i in range(len(info)):
    result.append(info[i+1])
result.sort()

print(len(result))
for i in result:
    print(i)
