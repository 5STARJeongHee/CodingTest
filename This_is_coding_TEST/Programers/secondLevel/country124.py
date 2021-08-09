# https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ''
    d = {0:4,1:1,2:2}

    remain = []
    while n != 0:
        remain.append(n%3)
        n //= 3
        if remain[-1] == 0:
            n -= 1
    
    for i in remain:
        answer = str(d[i]) + answer    

    return answer
print(solution(10))