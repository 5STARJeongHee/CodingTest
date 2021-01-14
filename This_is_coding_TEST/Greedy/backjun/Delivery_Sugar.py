N = int(input())

ret = 0

while N != 0:
    
    if N < 3 and N >0:
        
        ret = -1
        break
    if N % 5 == 0:
        ret += int(N/5)
        N = int(N%5)
    else:
        N -= 3
        ret +=1
print(ret)