# 그리드 문제 31분

S = input()
#입력
STT = []
for i in S:
    STT.append(int(i))

# def zero2one(ST):
#     temp = []
#     for i in ST:
#         temp.append(i or 1)
#     return temp
# def one2zero(ST):
#     temp = []
#     for i in ST:
#         temp.append(i and 0)
#     return temp

#0의 리스트, 1의 리스트, 모아서 넣어줄 temp 리스트
zero = []
one = []
temp = []

for i in range(len(STT)): # 이전 값과 달라지면 모아두었던 리스트를 넣어줌
    if STT[i] != STT[i-1] and i >0:
        if temp[0] == 0:
            zero.append(temp)
        else:
            one.append(temp)
        temp = []
    temp.append(STT[i]) # 현제 위치의 값을 temp에 넣어줌

    if i == len(STT)-1: # 마지막 인덱스에 도착했을 때 temp를 마저 넣어줌
        if temp[0] == 0:
            zero.append(temp)
        else:
            one.append(temp)
    
result = min(len(zero), len(one)) # 가장 적은 수의 그룹을 가진 것을 최소 변환 횟수라고 생각함

print(result)