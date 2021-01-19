s = input() # 문자열 입력
unit_limit = len(s) # 문자열 길이
length = 1000000000 # 제일 압축 잘된 길이-초기값 무한
for i in range(1,int(unit_limit/2)+1): #길이의 절반까지가 최고 단위
    index = list(range(0,unit_limit,i)) # 단위별 index를 쪼갬
    index.remove(0) # 0은 안쓰니까 제거
    
    temp = [] # 쪼갠 문자열 담을 임시 배열
    for unit in index:
        temp.append(s[unit-i:unit]) #문자열 쪼개 담기

    if index[len(index)-1] < len(s):
        temp.append(s[index[len(index)-1]:])# 나머지 문자열 담기
    
    k = '' # 비교할 문자열을 넣을 곳
    cnt = unit_limit # 전체 문자열 길이
    first = 0 #flag - 처음으로 같은게 나올 때
    for t in temp:
        if k == '': # 첫 문자열은 그냥 받아 넘김
            k = t
        elif k == t: # 현재 비교할 문자열이 같은 경우
            cnt -= i # 문자열 단위 만큼 길이를 뺌
            if first == 0: # 만약 처음으로 같은 문자열일 경우 카운트를 붙이므로 1 더함
                cnt += 1
                first = 1
        elif k != t: # 다른 경우 flag 초기화, 다른 문자열 넣어주기
            first = 0
            k = t
    if length > cnt: # 
        length = cnt

print(length)

