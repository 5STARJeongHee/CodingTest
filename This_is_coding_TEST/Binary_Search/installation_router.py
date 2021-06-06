# https://www.acmicpc.net/problem/2110
import sys

def bsearch(lst,C):
    result = 0
    start = 0
    end = lst[len(lst)-1]
    while start <= end:
        mid = (start + end) // 2 # 기준 거리, 해당 거리보다 좌표 사이의 거리가 같거나 더 길어야됨
        cnt = 1
        cur_dist = int(mid)
        
        for i in range(len(lst)-1):
            t_dist = lst[i+1] - lst[i]
            if cur_dist - t_dist > 0: # 기준 거리가 실제 좌표 사이거리보다 기므로 남은 거리를 다음 좌표로 넘김
                cur_dist -= t_dist
            else: # 기준거리와 같거나 더 긴 실제 좌표 사이 거리가 있다면 또는 남은 거리가 조건에 맞는다면 공유기 설치
                cnt+=1
                cur_dist = int(mid)
        
        if cnt >= C:
            if result < mid:
                result = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return result

N,C = map(int,sys.stdin.readline().rstrip().split())
n_list = []

for i in range(N):
    n_list.append(int(sys.stdin.readline().rstrip()))
n_list.sort()
print(bsearch(n_list,C))