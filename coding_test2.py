import re

def solution(s):
    answer = []
    
    answer.append(0)
    answer.append(0)

    
    while len(s) !=1:
        #0 제거
        for i in range(len(s)):
            if s[i] == '0':
                answer[1] +=1
        s = re.sub(r'[^1]','',s)
        
        #이진 변환
        temp = bin(len(s))
        s = temp[2:]
        answer[0] +=1
        
    return answer

a = "110010101001"


print(solution(a))