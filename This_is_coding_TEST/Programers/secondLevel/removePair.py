# https://programmers.co.kr/learn/courses/30/lessons/12973
# 바로 붙어 있는걸 비교할 때 stack이 상당히 ㄱㅊ다.
def solution(s):
    answer = -1
    answer = find_pair(s)
    return answer

def find_pair(s):
    stack = []
    idx = 0
    while idx != len(s):
        if not stack:
            stack.append(s[idx])
        elif stack[-1] != s[idx]:
            stack.append(s[idx])
        else:
            stack.pop()
        idx += 1
        
    if stack:
        return 0
    else:
        return 1
    
    
    
print(solution("abccaabaa"))