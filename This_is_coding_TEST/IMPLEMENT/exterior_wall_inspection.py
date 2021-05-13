# 테스트 케이스 2,3,4,6,7,9~13,15~24 통과 못함
def solution1(n, weak, dist):
    answer = 0

    w_dist = []
    dist = sorted(dist, reverse = True)
    for i in range(1,len(weak)):
        w_dist.append(weak[i] - weak[i-1])
    w_dist.append(n-weak[-1]+weak[0])

    size = len(weak)
    for i in dist:
        mpoint = 0
        t_dist = []
        if size == 0: break
        answer += 1

        for k in range(len(w_dist)):
            temp = i
            point = 1
            for j in w_dist:
                temp -= j
                if temp < 0:
                    break
                else:
                    point += 1
            if mpoint < point:
                mpoint = point
                t_dist = w_dist.copy()
            print(size,mpoint)
            print(w_dist)
            print('point',point)
            print('mp',mpoint)
            a = w_dist.pop(0)
            w_dist.append(a)
        w_dist = t_dist[:mpoint]
        size -= mpoint
        print('size',size)
    if size != 0: return -1    
    return answer

import sys
import os

def permutation(candidates, Prepermuation, res):
    if len(candidates) == 0: res.append(Prepermuation); return
    else:
        for i in range(len(candidates)):
            permutation(candidates[:i]+candidates[i+1:], Prepermuation + [ candidates[i] ], res)
        return

def solution(n, weak, dist):
    # complete search
    dist.sort(reverse = True)

    for i in range(1, len(dist)+1):
        permutations = []; permutation(dist[:i], [], permutations)
        for p in permutations:
            for start in range(len(weak)):
                _left = weak[:start]; _right = weak[start:]
                traverse_list = _right + [x+n for x in _left]; candidate = p.copy()
                while traverse_list and candidate:
                    cur = traverse_list.pop(0); d = candidate.pop(0);
                    Cover = cur + d
                    while traverse_list and traverse_list[0] <= Cover: traverse_list.pop(0)

                if not traverse_list:
                    return i
    return -1

from collections import deque

def best_solution(n, weak, dist):
    dist.sort(reverse=True)
    q = deque([weak]) #양쪽으로 삽입 삭제가 가능한 큐 - 방문하지 않은 점들의 리스트를 삽입 
    visited = set()
    visited.add(tuple(weak)) # 방문하지 않음 점들의 튜플 셋 추가
    for i in range(len(dist)): # 제일 거리가 긴 친구부터 하나씩 꺼냄 - 그리디
        d = dist[i] # 제일 거리가 긴친구부터 꺼냄
        print('d',d)
        for _ in range(len(q)):
            current = q.popleft() # 방문하지 않은 점들의 세트 하나를 꺼냄
            print(current) 
            for p in current: # 첫번째 점부터 차례대로 어디까지 거치는지
                l = p # 현제 시작점
                r = (p + d) % n # 현제 친구가 시작점부터 갈수 최대의 지점(시계방향만 고려- 반시계는 고려할 필요 없음 원이니까)
                if l < r:  
                    temp = tuple(filter(lambda x: x < l or x > r, current)) # 방문하지 않은 지점 찾기
                    print('test1')
                else:
                    temp = tuple(filter(lambda x: x < l and x > r, current)) # 방문하지 않은 지점 찾기
                    print('test2')
                print(l,r)
                print('temp',temp)

                if len(temp) == 0: # 방문하지 않은 지점이 없으므로 현제 인원수 리턴
                    return (i + 1)
                elif temp not in visited: # 방문하지 않은 지점 세트가 set에 없다면 추가
                    visited.add(temp)
                    q.append(list(temp)) # q에도 추가하여 다음 탐색지로 등록
                print('visited',visited)
                print('q',q)
    return -1

n1 = 12
weak1 = [1,5,6,10]
dist1 = [1,2,3,4]
# answer 2
n2 = 12
weak2 = [1,3,4,9,10]
dist2 = [3,5,7]
#answer 1
n3 = 200
weak3 = [0, 100]
dist3 = [1,1]
#answer = 2

n4 = 200
weak4 = [0, 10, 50, 80, 120, 160]
dist4 = [1, 10, 5, 40, 30]
# answ = 3

print(best_solution(n1,weak1,dist1))
