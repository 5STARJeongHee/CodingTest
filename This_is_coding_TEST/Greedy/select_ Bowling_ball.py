N,M = map(int, input().split())
ball = list(map(int,input().split()))

ball.sort()

def bfs(L,num):
    temp = list()
    if num > len(L): return temp

    if num == 1:
        for i in L:
            temp.append([i])
        
        

    elif num > 1:
        for  i in range(len(L)-num+1):
            for t in bfs(L[i+1:],num-1):
                temp.append([L[i]]+t)
    return temp

K = bfs(ball, 2)



for i in K:
    if i[0] == i[1]:
        K.remove(i)

result = len(K)
print(K)