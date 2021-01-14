N = int(input())

meet_times = []
cnt = 0
now = 0

for i in range(N):
    meet_times.append(list(map(int, input().split())))

meet_times.sort(key = lambda x:x[0])
meet_times.sort(key = lambda x:x[1])

for i in range(N):
    if now <= meet_times[i][0]:
            now = meet_times[i][1]
            cnt += 1            
print(cnt)