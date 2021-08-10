def solution(priorities, location):
    answer = -1

    p = list(set(priorities))
    p.sort()
    q = [0]
    temp = 0
    for i in reversed(p):
        cnt = 0
        index = q.pop()
        while cnt != len(priorities):
            print(i,index)
            if priorities[index] == i:
                q.append(index)
                print(q)
                temp += 1
                if index == location:
                    answer = temp 
                    break
            index = (index + 1) % len(priorities)
            cnt += 1
        if answer != -1:
            break
        
    return answer
### 다른 사람 풀이
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue): # 현제 우선순위 값이 다른 우선 순위보다 하나라도 작다면
            queue.append(cur) # 뒤로 미룸
        else: # 현제 값이 모든 다른 우선순위보다 크거나 같은 경우 (q에 들어가지 않고 순서카운트를 한다.)
            answer += 1
            if cur[0] == location:
                return answer

pr = [1, 1, 9, 1, 1, 1]
l = 0
print(solution(pr,l))