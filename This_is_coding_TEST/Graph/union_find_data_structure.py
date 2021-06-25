# 서로소 집합이란 공통 원소가 없는 두 집합을 의미한다.
# 서로소 집합 자료구조는 서로소 부분 집합들로 나누어진 원소들의
# 데이터를 처리하기 위한 자료 구조다.
#
# 사용처: 사이클 판별
# 방향 그래프의 경우 dfs로도 사이클 판별 가능
#
# 서로소 집합 자료구조는 스택 큐가 push,pop 연산으로 
# 동작되듯이 union, find 2개의 연산으로 이루어진 자료구조다
# union : 2개의 원소가 포함된 집합을 하나의 집합으로 합침
# find : 특정 원소가 속한 집합이 어떤 집합인지 알려주는 연산
# 
# 트리 자료구조를 이용
# 동작 과정
# 1. union 연산 -> 연결된 두 노드 A,B를 확인
# 1-1. A와 B의 루트 노드 A',B'를 각각 찾음
# 1-2. A'를 B'의 부모 노드로 설정한다(B'가 A'를 가르키도록 한다.)
# 2. 모든 union(합집합) 연산을 처리할 때까지 1번 과정을 반복한다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x): # 현재 방식은 현재 노드부터 계속 거슬러 올라가므로 최악의 경우 O(V) 걸림
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return x
def compress_path_find_parent(parent,x): # 위의 단점을 보완한 경로 압축 방식
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x]) # 루트노드가 바로 부모 노드가 됨
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    # a = find_parent(parent, a)
    # b = find_parent(parent, b)
    a = compress_path_find_parent(parent,a)
    b = compress_path_find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 1. 노드의 개수(V) 크기의 부모 테이블을 초기화
# 모든 원소가 자기 자신을 부모로 가지도록 설정
v,e = map(int, input().split()) # v: 노드수,e: 간선수
parent = [0] * (v + 1) 
for i in range(1,v+1):
    parent[i] = i

# 2. union 연산을 각각 수행
# for i in range(e):
#     a,b = map(int, input().split())
#     union_parent(parent,a,b)

# print('각 원소가 속한 집합: ', end='')
# for i in range(1, v + 1):
#     print(find_parent(parent, i ), end=' ')
# print()

# print('부모 테이블 : ',end='')
# for i in range(1, v + 1):
#     print(parent[i],end=' ')


# 서로소 집합을 활용한 사이클 판별법
# 무방향 그래프의 사이클 판별
# 1. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산 수행
# 2. 루트 노드가 서로 같다면 사이클(cycle)이 발생한 것
# 모든 간선에 대해 1~2번 과정 반복

cycle = False # 사이클 발생 여부

for i in range(e):
    a,b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if compress_path_find_parent(parent,a) == compress_path_find_parent(parent,b):
        cycle = True
        break
    # 사이클 발생하지 않은 경우 합집합 수행
    else:
        union_parent(parent,a,b)

if cycle:
    print('사이클 발생')
else:
    print('사이클 발생 하지 않음')
