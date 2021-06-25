# 신장 트리
# 하나의 그래프가 있을 때 모든 노드를 포함하면서 
# 사이클이 존재하지 않는 부분 그래프를 의미
# 트리의 성립 조건이기도 함 -> 신장 트리라고도 함
#
# 예: N개 도시가 존재하고 두 도시 사이에 도로를 놓아
# 전체 도시가 서로 연결 될 수 있게 도로를 설치하는 경우
# 이때 가장 적은 비용으로 연결할 때 최소 비용의 신장트리를 
# 찾는다.
#
# 위의 예처럼 최소 비용의 신장 트리를 찾는 알고리즘을
# '최소 신장 트리 알고리즘'이라고 함 그중 대표적인 
# 알고리즘은 '크루스칼 알고리즘'이라 한다.
# 크루스칼 알고리즘은 모든 간선에 대하여 정렬을 수행한뒤
# 가장 거리가 짧은 간선부터 포함시키면서 진행되므로 
# 그리디 알고리즘으로 분류된다.
#
# 시간 복잡도 O(ElogE)
## 동작 과정 ##
# 1. 간선 데이터를 비용에 따라 오름차순 정렬
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생
# 시키는지 확인
# 2-1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
# 2-2. 사이클 발생시 최소 신장 트리에 포함시킴
# 3. 2번 과정을 반복

# find 함수
def find_parent(parent,x):
    # 연결된 모든 노드들의 루트 노드를 갱신
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클 발생하지 않는 경우만 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
print(result)