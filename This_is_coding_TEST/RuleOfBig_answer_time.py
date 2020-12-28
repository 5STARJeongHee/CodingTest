n, m, k = map(int, intput().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m /(k+1))*k #큰수가 등장하는 횟수 \6665 -4개로 나누고, 큰수 등장 제한 횟수 곱함
count += m%(k+1) # 안나눠 떨어지는 부분의 큰수 등장 횟수 

result = 0
result += count*first
result += (m-count)*second # 전체 횟수에서 큰수 개수만 뺌

print(result)
