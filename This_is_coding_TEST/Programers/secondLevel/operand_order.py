# https://programmers.co.kr/learn/courses/30/lessons/67257
import re
from itertools import permutations
from collections import deque
import heapq
def solution(expression):
    answer = 0
    exp = list(re.findall('\d+|\D',expression)) # 숫자와 연산자 분리
    
    exp_lst = list(set(re.findall('\D',expression))) # 연산자만 분리
    exp_order = list(permutations(exp_lst,len(exp_lst))) # 순열로 조합한 우선순위 조합들을 배열로
    result = []
    for e in exp_order:
        d = calc_postfix(toPostfix(exp,e))
        heapq.heappush(result,-abs(d))
    answer = -heapq.heappop(result)
    return answer
def toPostfix(s,order):
    # 우선순위 딕셔너리 -> 우선순위값 받아오기위해 만듬
    prior_dic = {order[-(i+1)]:i for i in range(len(order))}
    
    postfix = [] # postfix로 바꾼 결과를 담기
    op_stack = [] # 연산자 전용 스택
    for token in s: # 문자열로 된 '숫자' , '연산자'를 토큰으로 꺼내옴
        if re.findall('\d+',token): # '숫자'인 경우 postfix에 바로 출력
            postfix.append(token)
        elif token == ')': # ')' 연산자를 만난경우 '('를 만날때까지 연산자 스택을 비움
            while op_stack[-1] != '(':
                postfix.append(op_stack.pop())
            op_stack.pop() # '(' 제거 
        elif token =='(': # '(' 연산자 우선 순위 최상위 이지만 딱히 비교에 쓰지 않으므로 따로 추가함
             op_stack.append('(')
        else: # '연산자' 인경우
            # 연산자 스택이 비어 있지 않고 스택 상단의 op가 새로 온 op보다 우선순위가 높거나 같다면 
            # 빼서 출력한다. 그 뒤 새로 온 연산자를 넣는다. '('에 대해서는 빼면 안되므로 조건에 추가
            # '('는 스택에 있을 시 가장 낮은 우선 순위이지만 새로 들어올때는 우선순위가 최상위이므로 
            # 들어올땐 무조건 추가, 새로 연산자를 추가할 때는 비교에 넣지 않고 그대로 연산자를 추가하도록 함
            while op_stack and op_stack[-1] != '(' and prior_dic[op_stack[-1]] >= prior_dic[token]: 
                postfix.append(op_stack.pop())
            op_stack.append(token)
    while op_stack:
        postfix.append(op_stack.pop())
    return postfix 

def calc_postfix(arr):
    stack = []
    result = 0
    # print(arr)
    for i in arr:
        if i.isdecimal():
            stack.append(int(i))
        else:
            b = stack.pop()
            a = stack.pop()
            r = 0
            if i == '+':
                r += (a + b)
            elif i == '-':
                r += (a - b)
            elif i == '*':
                r += (a * b)
            elif i == '/':
                r += (a // b)
            stack.append(r)
    return stack[0]
print(solution("100-200*300-500+20"))