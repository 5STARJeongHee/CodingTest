# 최대 100,000 개 까지 입력되므로 , N^2 알고리즘은 10000개 이하 데이터 일때
# 지금은 10만이 넘으므로 nlogn이 보장되는 알고리즘을 쓰는걸 추천
# 계수 정렬이나 nloln을 지원하는 파이썬 라이브러리 활용 

N = int(input())
arr = []
for i in range(N):
    name, score = input().split()
    arr.append([name,int(score)])
# 계수 정렬 풀이
carr = []
for i in range(101):
    carr.append([])

for i in arr:
    carr[i[1]].append(i[0])

for i in carr:
    if len(i):
        print(i[0], end=' ')

# 파이썬 라이브러리 사용 풀이
# arr = sorted(arr, key=lambda x:x[1]) 이거 하나면 끝임 ㅋㅋ
