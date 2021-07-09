# 단방향의 그래프 인경우 
# dfs로 사이클 정보 얻기 -> 탐색 중 방문한 곳이 후보에 
# 다시 나온 경우 해당 경우는 원래 dfs에서 무시 했었지만
# 사이클을 보기 위해 해당 경우에는 cycle을 카운트 했음
def dfs(u):
    visited[u] = True
    global cycle
    for i in graph[u]:
        if not visited[i]:
            dfs(i)
        else:
            cycle += 1
cycle = 0    
graph = [
    [],
    [2, 3, 8],
    [1 , 7],
    [1 , 4, 5],
    [3, 5],
    [3, 4 ],
    [7],
    [2, 6, 8],
    [1 , 7]
]
# 각 노드가 방문된 정보
visited = [False] * 9
dfs(1)
print(cycle)