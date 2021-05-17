N = int(input())
d = list(map(int, input().split()))[:N]

for i in range(N-1):
    mi = i
    for j in range(i+1,N):
        if d[mi] > d[j]:
            mi = j
    d[i], d[mi] = d[mi], d[i]
    
    for j in d:
        print(j,end=' ')
    print()


