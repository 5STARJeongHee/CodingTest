# 2 7
# 2 3 2 3 1 2 7
#2
N, K = map(int, input().split())
devices = list(map(int, input().split()))
charging = []
cnt = 0

if N >= K:
    print(cnt)
else:
    for i in range(len(devices)):
        d = devices[i]
        if len(charging) != N:        
            if d not in charging:
                charging.append(d)
        elif len(charging) == N:
            if d in charging: #콘센트에 이미 있는 경우
                continue
            else:
                reuse = [t in devices[i:] for t in charging]
            
                if False in reuse: # 재사용하지 않는 기구가 있을 때
                    k = reuse.index(False)    
                    charging.remove(charging[k])
                    charging.append(d)
                    cnt += 1
                else : # 모든 기구가 다시 사용
                    max = 0
                    for j in charging:
                        temp = devices[i:].index(j) # 제일 나중에 사용하는 것 고르기
                        if max < temp:
                            max =  temp
                    max += i #쪼개진 리스트에서 구한 index이므로 i를 더해줌
                    charging.remove(devices[max])
                    charging.append(d)
                    cnt += 1
    print(cnt)
            
# 다른 사람 풀이
# N, K = map(int, input().split())
# kind = list(map(int, input().split()))
# mul = []
# res = 0

# for i in range(K):
#     if kind[i] in mul: # 꽂혀있다면 계속
#         continue
#     if len(mul) < N: # 다 꽂혀있지 않다면 추가
#         mul.append(kind[i])
#         continue

#     idxs = []
#     for j in range(N):
#         try:
#             idx = kind[i:].index(mul[j]) #꽂혀있는것중 하나하나 재사용 index 확인
#         except:
#             idx = 101 # 재사용하지 않을 경우우 제일 멀리 둠
#         idxs.append(idx)

#     temp = idxs.index(max(idxs)) # 제일 멀리 있는 index를 뽑음
#     del mul[temp] # 제거
#     mul.append(kind[i]) 현제 장치 꽂음
#     res += 1 
# print(res)
