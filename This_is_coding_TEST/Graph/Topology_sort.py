# 위상 정렬
# 일련의 작업을 차례대로 수행해야 할 때 사용하는 알고리즘
# 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
# 예: 선서과목을 고려한 학습 순서 설정

# 진입차수 : 한 노드에 들어오는 간선의 개수
# 모든 노드를 확인하면서 해당 노드에서 출발하는 간선을 차례대로 제거해야함
# 시간 복잡도는 O(V + E)

# 1. 진입차수가 0인 노드를 큐에 넣는다.
# 2. 큐가 빌 때까지 다음의 과정을 반복한다.
# 2-1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
# 2-2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 발생한 것

from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # b의 진입 차수 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque()

    # 진입 차수가 0인 노드를 큐에 삽입하며 시작
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 진입 차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
        
    for i in result:
        print(i,end=' ')

topology_sort()