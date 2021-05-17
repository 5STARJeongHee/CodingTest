N = int(input())
d = list(map(int, input().split()))[:N]

for i in range(1,N):
    for j in range(i,0,-1):
        if d[j] < d[j-1]:
            d[j], d[j-1] = d[j-1],d[j]
        else:
            break
    for j in d:
        print(j,end=' ')
    print()
