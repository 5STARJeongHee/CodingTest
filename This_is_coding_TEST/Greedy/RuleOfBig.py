print("input N, M, K")
p = input().split()
p = [int(k) for k in p]
a = input().split()
b = [int(k) for k in a]

b = sorted(b, reverse=True)
print(b)
limit = 0
answer = 0
for i in range(p[1]):
    if limit != p[2]:
        answer = answer + b[0]
        limit += 1
        print("answer0 : " + str(answer))
    else:
        answer = answer + b[1]
        limit = 0
        print("answer1 : " + str(answer))
    
print(answer)
