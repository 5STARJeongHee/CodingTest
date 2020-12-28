N, K = map(int,input().split())

result=0

# def minus(num):
#     return num-1

# def devide(num):
#     return N/K

while True:
    if N%K == 0:
        N = N/K
        result+=1
    else:
        N = N-1
        result+=1
    if N == 1:
        break
print(result)