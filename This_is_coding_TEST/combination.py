from itertools import combinations
# combinations 함수를 사용하는 경우 
# - input: list, 조합수 
# - output: 조합수 만큼의 조합을 반환
a = []

items = [1,2,3,4]
for i in range(1, len(items) +1 ):
    for j in list(combinations(items,i)):
        a.append(j)

print(a)

# 중복 조합 - 중복이 있는 값들에 대해서 중복 처리 하는 조합
from itertools import combinations_with_replacement
items = [1,2,3,4]
b=[]
for i in range(1, len(items) +1 ):
    for j in list(combinations_with_replacement(items,i)):
        b.append(j)
print(b)

#조합 구현
print("구현: ")
items = [3,3,2,1,4]
def comb(lst, n):
    ret = []
    if n > len(lst): return ret # 조합 수보다 리스트가 작은 경우는 존재 x 그냥 끝

    if n == 1: # 1개 뿐일 때
        for i in lst:
            ret.append([i])
#combination([1,2,3,4],2) = ([1] + combination([2,3,4],1)) and
# ([2] + combination([3,4],1)) and ([3] + combination([4],1))
# 위의 예시 처럼 2개인 경우는 위와 같은 케이스로 나뉜다.

    elif n > 1: # 조합수가 2 이상일 때 
        for i in range(len(lst)-n+1): # 리스트 길이에서 n개를 뺀 경우만큼 케이스가 나뉨
            for temp in comb(lst[i+1:],n-1): # 하나를 뽑고 다시 넣지 않고 제외한 리스트에서 n-1개를 뽑음
                ret.append([lst[i]]+temp) # 결국은 1개 뿐일 때 뽑는 것에 도착 후 
                                          # 스택을 타고 돌아와서 n 개 뽑는 것에 추가
    return ret

c = []
for i in range(1, len(items) +1 ):
    for j in list(comb(items,i)):
        c.append(j)

print(c)

#dfs 구현 방식

def dfs_comb(lst,n):
	ret = []
	idx = [i for i in range(len(lst))]

	stack  = []
	for i in idx[:len(lst)-n+1]:
		stack.append([i])
	
	while len(stack)!=0:
		cur = stack.pop()

		for i in range(cur[-1]+1,len(lst)-n+1+len(cur)):
			temp=cur+[i]
			if len(temp)==n:
				element = []
				for i in temp:
					element.append(lst[i])
				ret.append(element)
			else:
				stack.append(temp)
	return ret