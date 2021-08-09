# https://programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    answer = []
    status = 0
    size = (n+1)*n//2

    temp = [[0]*(n) for _ in range(n)]

    num = 1
    y,x = 0,0
    
    temp[y][x] = num
    while num < size:
        
        while y+1<n and temp[y+1][x] ==0: # 아래 내려가는
            num += 1
            y += 1
            temp[y][x] = num
    
        while x+1<n and temp[y][x+1] ==0: # 오른쪽
            num += 1
            x += 1
            temp[y][x] = num
        
        while y-1<n and x-1<n and temp[y-1][x-1] ==0:# 왼쪽 대각
            num += 1
            x -= 1
            y -= 1
            temp[y][x] = num 
    for i in range(n):
        for j in range(n):
            if temp[i][j] !=0:
                answer.append(temp[i][j])
           
    return answer

print(solution(4))
